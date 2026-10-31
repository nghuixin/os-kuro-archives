# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = [
#   "ultralytics>=8.3",
#   "rapidocr-onnxruntime>=1.3",
#   "pillow",
# ]
# ///
"""Label each raw image as medical, dog, exclude (licence plates), other or unsure.

Runs fully offline: YOLO for dogs and vehicles, RapidOCR for text.
Writes data/derived/image_index.csv and a review gallery; moves nothing.

    uv run scripts/triage_images.py [--limit N]
"""

import argparse
import csv
import html
import re
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps
from rapidocr_onnxruntime import RapidOCR
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "whatsapp"
OUT = ROOT / "data" / "derived"
OVERRIDES = ROOT / "data" / "labels" / "image_overrides.csv"  # file,label,note — hand corrections win
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_SIDE = 1600

COCO_DOG = 16
COCO_VEHICLES = {2, 3, 5, 7}  # car, motorcycle, bus, truck
DET_CONF = 0.35

TEXT_HEAVY = 15  # OCR words; report pages have hundreds, photos almost none

MEDICAL_TERMS = [
    r"mg/dl", r"g/dl", r"u/l", r"iu/l", r"mmol/l", r"[uµ]mol/l", r"x ?10\^?\d",
    r"wbc", r"rbc", r"hct", r"hgb", r"plt", r"mcv", r"mchc?", r"neutrophils?", r"lymphocytes?",
    r"alt", r"alkp", r"alp", r"ast", r"ggt", r"bun", r"urea", r"crea", r"creatinine",
    r"glucose", r"albumin", r"globulin", r"bilirubin", r"cholesterol", r"phosphorus",
    r"calcium", r"sodium", r"potassium", r"chloride", r"sdma", r"t4", r"lipase",
    r"reference", r"ref\.? range", r"cbc", r"chemistry", r"ha?ematology", r"urinalysis",
    r"canine", r"patient", r"species", r"veterinary", r"diagnosis", r"prescription",
    r"dosage", r"tablets?", r"vaccin\w*", r"x-?ray", r"radiograph\w*", r"ultrasound",
]
# OCR often runs words together (PREDNISOLONESMGPERTAB), so these match anywhere in the text
MEDICAL_SUBSTRINGS = [
    "veterinar", "animaluse", "animal use", "medicine", "tablet", "capsule", "timesdaily", "times daily",
    "kalisehari", "kali sehari", "selepasmakan", "selepas makan", "aftermeal", "after meal", "afterfood",
    "injection", "vaccination", "deworm", "prednisolone", "protexin", "catalyst", "idexx", "supplement",
    "ingredients", "painrelief", "pain relief", "invoice", "treatment", "dog&cat", "furkids", "petcare",
    "asiapaws", "asia paws", "dosage", "antibiotic", "probiotic",
]
MEDICAL_RE = re.compile(
    r"\b(?:" + "|".join(MEDICAL_TERMS) + r")\b|" + "|".join(re.escape(s) for s in MEDICAL_SUBSTRINGS),
    re.IGNORECASE,
)

# SG/MY style (SBA1234A, WXY123) and US style (8ABC123, ABC1234)
PLATE_RE = re.compile(r"^(?:[A-Z]{2,3}\d{3,4}[A-Z]?|\d[A-Z]{3}\d{3})$")
# Look like plates but aren't: ringgit amounts (RM174), month-year stamps (MAY2025)
NOT_PLATE_RE = re.compile(r"^(?:RM\d+|(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)20\d\d)$")


def load(path: Path) -> np.ndarray:
    img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    img.thumbnail((MAX_SIDE, MAX_SIDE))
    return np.asarray(img)


def plate_tokens(lines: list[str]) -> list[str]:
    hits = []
    for line in lines:
        compact = re.sub(r"[\s\-·.]", "", line.upper())
        candidates = [compact] + re.sub(r"[\-·.]", "", line.upper()).split()
        hits += [c for c in candidates if PLATE_RE.match(c) and not NOT_PLATE_RE.match(c)]
    return sorted(set(hits))


def classify(dog: float, vehicle: float, words: int, medical: int, plates: list[str]) -> str:
    if plates and (vehicle or medical < 3):
        return "exclude"
    if plates:
        return "unsure"
    if medical >= 2:  # labels and packaging carry few words but strong terms
        return "medical"
    if dog and words < TEXT_HEAVY:
        return "dog"
    if words >= TEXT_HEAVY or medical:
        return "unsure"
    return "other"


def write_gallery(rows: list[dict], path: Path) -> None:
    order = ["unsure", "exclude", "medical", "dog", "other"]
    sections = []
    for label in order:
        group = [r for r in rows if r["label"] == label]
        if not group:
            continue
        cards = "".join(
            f'<figure><a href="{html.escape(r["rel"])}" target="_blank">'
            f'<img loading="lazy" src="{html.escape(r["rel"])}"></a>'
            f'<figcaption>{html.escape(r["file"])}<br>{r["date"]} · words {r["ocr_words"]}'
            f' · med {r["medical_hits"]} · dog {r["dog_conf"]} · veh {r["vehicle_conf"]}'
            f'{" · plate " + html.escape(r["plates"]) if r["plates"] else ""}</figcaption></figure>'
            for r in group
        )
        sections.append(f'<h2 id="{label}">{label} ({len(group)})</h2><div class="grid">{cards}</div>')
    nav = " · ".join(f'<a href="#{l}">{l}</a>' for l in order)
    path.write_text(
        "<!doctype html><meta charset=utf-8><title>Image triage</title><style>"
        "body{font:13px system-ui;margin:16px;background:#fafafa}"
        ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}"
        "figure{margin:0;background:#fff;border:1px solid #ddd;padding:6px}"
        "img{width:100%;height:180px;object-fit:cover}figcaption{color:#555;word-break:break-all}"
        f"</style><p>{nav}</p>{''.join(sections)}",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, help="only process the first N images")
    args = parser.parse_args()

    images = sorted(p for p in RAW.rglob("*") if p.suffix.lower() in IMAGE_EXTS)[: args.limit]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "models").mkdir(exist_ok=True)

    overrides = {}
    if OVERRIDES.exists():
        with open(OVERRIDES, newline="", encoding="utf-8") as f:
            overrides = {r["file"]: r["label"] for r in csv.DictReader(f)}

    detector = YOLO(str(OUT / "models" / "yolov8n.pt"))
    ocr = RapidOCR()

    rows = []
    start = time.time()
    for i, path in enumerate(images, 1):
        img = load(path)

        det = detector(img, conf=DET_CONF, verbose=False)[0]
        classes = det.boxes.cls.tolist()
        confs = det.boxes.conf.tolist()
        dog = max((c for k, c in zip(classes, confs) if k == COCO_DOG), default=0.0)
        vehicle = max((c for k, c in zip(classes, confs) if k in COCO_VEHICLES), default=0.0)

        result, _ = ocr(img)
        lines = [text for _, text, _ in (result or [])]
        words = sum(len(t.split()) for t in lines)
        medical = len(MEDICAL_RE.findall(" ".join(lines)))
        plates = plate_tokens(lines)

        m = re.search(r"(\d{4})(\d{2})(\d{2})", path.name)
        auto = classify(dog, vehicle, words, medical, plates)
        rows.append({
            "file": path.name,
            "date": f"{m[1]}-{m[2]}-{m[3]}" if m else "",
            "label": overrides.get(path.name, auto),
            "auto_label": auto,
            "ocr_words": words,
            "medical_hits": medical,
            "dog_conf": round(dog, 2),
            "vehicle_conf": round(vehicle, 2),
            "plates": " ".join(plates),
            "ocr_text": " | ".join(lines),
            "rel": (Path("..") / path.relative_to(ROOT / "data")).as_posix(),  # from data/derived/
        })
        if i % 25 == 0 or i == len(images):
            print(f"{i}/{len(images)}  {time.time() - start:.0f}s", flush=True)

    fields = ["file", "date", "label", "auto_label", "ocr_words", "medical_hits", "dog_conf",
              "vehicle_conf", "plates", "ocr_text"]
    with open(OUT / "image_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    write_gallery(rows, OUT / "image_review.html")

    counts = {}
    for r in rows:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    print("labels:", counts)


if __name__ == "__main__":
    main()
