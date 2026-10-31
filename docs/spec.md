# Canine Health Atlas — Spec

A local-first tool that turns a folder of one dog's veterinary records into a reviewed, source-linked dataset and a dashboard that charts each measurement, explains what it measures, and opens the page it came from.

The repo has two layers:

- **Archive** (built, public): Kuro's records extracted into CSVs in `data/processed/`, with a written summary in `docs/`. This is the reference dataset and the source of the gold set.
- **Atlas** (not yet built): the software below, which reproduces the archive automatically from raw records and adds review, charts and explainers.

**Feature test (Atlas):** does it help an owner understand a number and bring it to their vet, *without* telling them what the number means for their dog? If not, cut it.

## Principles

1. **The Atlas explains the measurement; it never diagnoses, interprets or alerts.** Archive documents that assess something (e.g. `docs/diet-critique.md`) are labelled as reviews and are not part of the Atlas UI.
2. Every chart point links to the exact page, and the region on that page, it came from.
3. Never plot a value that isn't grounded on a page. Unreviewed values look visibly different.
4. Reference intervals are per lab and per measurement, never one band across a chart.
5. **Raw records never enter Git.** Extracted values may be published in the archive layer only after a personal-details scan (names, addresses, phone numbers, client and patient IDs, plates, bank details). Page images may be sent to a vision API; the owner has accepted this for Kuro's records.

## Scope

**Atlas MVP:** text-layer lab PDFs first, then photographed and scanned lab reports; body weight; a reviewed measurement table; per-analyte charts; explainers for common chemistry and CBC analytes; page-level source viewing.

**Archive only (out of Atlas MVP):** medications and prescriptions, narrative findings, imaging, chat messages, invoices, diet. These are captured by hand in the archive CSVs. First post-MVP Atlas addition: an events timeline built from `health_events.csv` and `visits.csv`.

**Out entirely:** multi-dog, cloud hosting, accounts, interpretation or alerting.

## Audiences

| | Owner (personal) | Next dog owner (case study) |
|---|---|---|
| Data | Kuro's raw records in `ATLAS_DATA_DIR` (outside Git); extracted values in `data/processed/` | `data/synthetic/`: one fictional dog, 6 visits, 2 labs, text PDFs plus phone photos and 1 scan |
| Runs | Full stack locally, own API key | Same stack, or the static demo on GitHub Pages |
| Success | Every lab value charted, source page one click away | Fresh clone → synthetic dashboard in < 15 min |

## What the archive taught us

Findings from extracting Kuro's records by hand (Oct 2026) that the design below relies on:

- **Lab data is mostly text-layer PDFs, not photos.** Of 43 analyzer runs, 29 came from IDEXX report PDFs and 14 from photos. `pdfplumber` parsed all 10 PDFs with no unread lines. The no-API-key path covers most lab data.
- **Reports carry the previous result.** Each IDEXX report prints the prior run beside the current one, which added 10+ test dates with no report of their own. Both become measurements, marked by `basis`.
- **Photos need triage first.** WhatsApp exports mix lab printouts and medicine labels with dog photos, payment screenshots and photos showing vehicle plates. They must be sorted before extraction, and plate photos excluded.
- **Dates have different bases.** Report headers, invoices and image headers carry local dates; WhatsApp chat timestamps ran about 15 hours behind Malaysia time, so a daytime visit can appear a day early.
- **File hashes don't catch all duplicates.** Re-downloaded invoices (`INV-123-1.pdf`, `INV-123 (1).pdf`) had different bytes. Documents also need de-duplication by their own identifier (invoice number, report run time).
- **Report-header weights can be stale.** The weight printed on a lab report sometimes predates that day's weighing.
- **Analyzer flags matter.** Values marked `*` (e.g. a clumped platelet count of 3) must be kept but flagged, not charted as normal values.

## Architecture

One `atlas` CLI, one small API, one static dashboard.

```
ingest → triage → pages → extract → ground → normalize → review → export → static dashboard
```

- **ingest:** register each file with its sha256 and source (chat folder, clinic). De-duplicate by hash and by document identifier.
- **triage:** label every image `medical`, `dog`, `exclude` (plates, payments) or `unsure`, using object detection (YOLO) and OCR keyword density. Hand corrections in an overrides file always win. Only `medical` images go on. (Prototype: `scripts/triage_images.py`.)
- **pages:** every input becomes page PNGs plus a word list with bounding boxes. PDFs use `pdftoppm` and `pdfplumber`. Photos are fixed for EXIF rotation, deskewed and perspective-corrected, then OCR'd.
- **extract:** an `Extractor` protocol with two adapters, chosen per document.
  - `rules` (primary): `pdfplumber` plus parsers for known layouts (IDEXX ProCyte, Catalyst, SNAP; US and day-first date formats). Emits current and previous-result values. This is the CI path and needs no API key.
  - `vision` (for photos and scans): a vision model returns JSON matching a Pydantic schema. The prompt and schema are versioned in `extraction/prompts/`.
- **ground:** fuzzy-match each value to the page's words and attach its bbox. Values with no match are stored as `unverified` and never plotted, until a reviewer draws the box by hand on the review page (`grounded = manual`). Text-layer PDFs ground exactly.
- **normalize:** map labels through `knowledge/terminology.yaml` (explicit, never fuzzy; unknown labels are listed). Convert units only where a factor is defined. Run sanity validators, including cross-checks such as differential % × WBC = absolute count.
- **review:** a web page that is the only place data is written by hand. It shows the page crop beside each value.
- **export:** a data pack (JSON plus page images) and the archive CSVs. The dashboard reads only this pack, with no server behind it.

**Stack:** Vite + React + Recharts; FastAPI (5 routes: documents, pages, extractions, patch measurement, explainers); SQLAlchemy + SQLite; `uv`; `openapi.yaml` as the contract; Make, Compose, and one CI workflow (test → eval → build the synthetic dashboard → deploy Pages). Build data-first: gold set and `schemas.py`, then extractor, then API, then UI.

## Data model

Provenance chain: **chart point → Measurement → Extraction → Page → Document → file hash.**

| Entity | Key fields | Rule |
|---|---|---|
| Document | `id` (sha256), `doc_key` (e.g. invoice number or report run time), `filename`, `kind`, `source_chat`, `lab`, `received_date`, `page_count`, `triage_label` | Re-ingesting the same file or the same `doc_key` is a no-op |
| Page | `document_id`, `page_no`, `image_path`, `words` (text + bbox) | Every document has pages, even a single photo |
| Extraction | `label_raw`, `value_raw`, `unit_raw`, `ref_raw`, `flag_raw`, `date_raw`, `basis` (current, previous), `analyzer_star`, `bbox`, `grounded` (auto, manual, none), `extractor`, `model`, `prompt_hash` | Immutable; one row per candidate |
| Measurement | `analyte`, `value`/`unit`, `value_original`/`unit_original`, `ref_low`/`ref_high`, `flag`, `date`, `time`, `date_basis`, `visit_id`, `lab`, `analyzer`, `confidence`, `status`, `reviewed_at`, `note` | `status` ∈ {extracted, corrected, rejected}; charts show non-rejected AND grounded only |
| AnalyzerComment | `date`, `time`, `analyzer`, `comment`, `document_id` | Shown beside the run, never as a diagnosis |
| Visit | `date`, `clinic`, `visit_type`, `document_ids[]` | Groups several documents into one visit; splits one report with several runs into several visits |
| Explainer | `analyte`, `species: dog`, `what_it_measures`, `why_ordered`, `general_causes_high/low[]`, `caveats[]`, `sources[]`, `last_reviewed` | Test fails if `sources` is empty or `species` ≠ dog |

Corrections never overwrite the raw extraction. A canonical unit is added only when `units.py` has a factor for that analyte; otherwise the chart shows the original unit with a note.

**Archive mapping.** `labs.csv` holds Measurements (`record_type = panel`), AnalyzerComments (`analyzer comment`) and chat-only findings (`reported`). `visits.csv` holds Visits. `source` names the document but not yet the page or region; adding `page_no` and `bbox` is the first step in moving the archive onto this model.

## Evaluation

`atlas eval` (`evals/score.py`) reports precision, recall, unit errors, digit errors and wrong-visit rate. Every milestone closes on a number from this or from a timed run. Thresholds are set after the first real eval.

`evals/gold/` has two parts:

- **Real pairs (private, under `ATLAS_DATA_DIR`):** reports that exist both as a text-layer PDF and as a photo (2025-02-10, 2026-02-04, 2026-08-10). The PDF values are the answer key for the vision extractor. Hand transcriptions of these photos matched the PDFs exactly.
- **Synthetic (public):** reports built from real layouts with values and identifiers replaced, for CI.

## Roadmap

- **M0:** `schemas.py`, `atlas eval` scoring, gold set from the real PDF/photo pairs plus synthetic reports. *(The archive's PDF parser and photo transcriptions already provide most of the gold data.)*
- **First vertical slice:** ingest → `rules` adapter on the IDEXX PDFs → ground → review → chart, for creatinine only, with the bbox round-tripping page → chart → page.
- **Then:** all analytes and previous-result values → triage and the `vision` adapter for photos → explainers (20 analytes) → static demo plus a timed fresh-clone run (< 15 min).

## Repo layout

```
backend/app/{main,models,schemas,database,cli}.py
backend/app/ingest/{register,triage}.py
backend/app/extraction/{base,vision,rules,ground,pages}.py + prompts/
backend/app/normalization/{terminology,units,validators}.py
backend/app/services/{review,export}.py
frontend/src/pages/{Dashboard,Review,Sources}.tsx
knowledge/{explainers/,terminology.yaml,sources.yaml}
evals/{gold/,score.py}
data/raw/            (gitignored except README)
data/processed/      archive CSVs (public)
data/synthetic/
scripts/             prototypes (triage_images.py)
docs/{spec,tasks,methodology,data-dictionary,getting-your-records,talking-to-your-vet,how-we-built-it,health-summary,diet-critique}.md
```

## Privacy, content and license

- `ATLAS_DATA_DIR` (default `~/.canine-atlas/<dog>/`) and `data/raw/` are gitignored, along with all images and WhatsApp exports.
- Archive exports remove people's names (owners, vets, sitters, staff), addresses, phone numbers, client and patient IDs, vehicle plates and bank details. Clinic names are kept. A pattern scan runs before every commit.
- Explainers are reviewed writing, not generated text. They cite `knowledge/sources.yaml` (Merck Veterinary Manual, eClinpath) and use "veterinarians consider" phrasing, never "this means".
- Synthetic reports are built from real layouts with values and identifiers replaced. They include a text PDF with a previous-result column, a photo, a scan, a report with an analyzer `*` flag, one with no reference intervals, and one in SI units.
- MIT license for the code and the explainer text; sources are linked, never copied.

## Open questions

Answered by the archive:

- [x] **Document kinds:** lab results are mostly text-layer PDFs (29 of 43 runs); medicine labels, invoices and the rest are mostly photos.
- [x] **Vision provider:** Claude; the owner accepted sending page images.
- [x] **Collection vs report date:** IDEXX reports carry the run time, the print time and the previous run's date. Chats need a `date_basis` because of the time offset.
- [x] **Explainer analytes (20):** HCT, HGB, RBC, RETIC, PLT, WBC, NEU, MONO, ALT, ALKP, UREA, CREA, SDMA, LIPA, GLU, ALB, TP, PHOS, CA, CHOL.
- [x] **Body weight:** on lab report headers (sometimes stale), in chats, on medicine labels and in the diet analysis; not on invoices.

Still open:

- [ ] How much of the photo OCR fails to ground (blur, glare, curled paper)? Measure on the 14 photographed runs.
- [ ] Should the archive CSVs gain `page_no` and `bbox` now, or only once the Atlas regenerates them?
- [ ] Is the triage model (YOLO + OCR keywords) good enough without hand corrections? So far 13 photos needed overriding.
- [ ] Which records are still missing from the clinic (SDMA values for Oct 2024 and Apr 2026, imaging and biopsy reports, post-mortem report), and should `docs/getting-your-records.md` cover requesting them?
