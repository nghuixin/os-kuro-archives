# Canine Health Atlas — Spec

A local-first tool that turns a folder of one dog's veterinary records into a reviewed, source-linked dataset and a dashboard that charts each measurement, explains what it measures, and opens the page it came from.

**Feature test:** does it help an owner understand a number and bring it to their vet, *without* telling them what the number means for their dog? If not, cut it.

## Principles

1. Explain the measurement; never diagnose, interpret or alert.
2. Every chart point links to the exact page, and the region on that page, it came from.
3. Never plot a value that isn't grounded on a page. Unreviewed values look visibly different.
4. Reference intervals are per lab and per measurement, never one band across a chart.
5. Real records never enter Git or leave the machine (except page images sent to a vision API, opt-in).

## Scope

**MVP:** photographed lab reports (the bulk of Kuro's records); scans and text-layer PDFs; body weight; a reviewed measurement table; per-analyte charts; explainers for common chemistry and CBC analytes; page-level source viewing.

**Out:** medications, narrative findings, imaging, text messages, multi-dog, cloud hosting, accounts, interpretation or alerting. First post-MVP addition: a hand-entered events timeline.

## Audiences

| | Owner (personal) | Next dog owner (case study) |
|---|---|---|
| Data | Kuro's records in `ATLAS_DATA_DIR` (outside Git) | `data/synthetic/`: one fictional dog, 6 visits, 2 labs, mostly phone photos plus 1 scan and 1 text PDF |
| Runs | Full stack locally, own API key | Same stack, or the static demo on GitHub Pages |
| Success | Every lab value charted, source page one click away | Fresh clone → synthetic dashboard in < 15 min |

## Architecture

One `atlas` CLI, one small API, one static dashboard.

```
ingest → pages → extract → ground → normalize → review → export → static dashboard
```

- **pages:** every input becomes page PNGs plus a word list with bounding boxes. Photos are first fixed for EXIF rotation, deskewed and perspective-corrected (Pillow/OpenCV), then OCR'd with Tesseract. PDFs use `pdftoppm` and `pdfplumber`.
- **extract:** an `Extractor` protocol with two adapters, chosen by `ATLAS_EXTRACTOR=vision|rules`.
  - `vision` (primary, since the records are mostly photos): a vision model returns JSON matching a Pydantic schema. The prompt and schema are versioned in `extraction/prompts/`.
  - `rules`: `pdfplumber` plus regex for known text-PDF layouts. This is the CI path and needs no API key.
- **ground:** fuzzy-match each value to the page's OCR words and attach its bbox. Values with no match are stored as `unverified` and never plotted, until a reviewer draws the box by hand on the review page (`grounded = manual`).
- **normalize:** map labels through `knowledge/terminology.yaml` (explicit, never fuzzy; unknown labels are listed). Convert units only where a factor is defined. Run sanity validators.
- **review:** a web page that is the only place data is written by hand. It shows the page crop beside each value.
- **export:** a data pack (JSON plus page images). The dashboard reads only this pack, with no server behind it.

**Stack:** Vite + React + Recharts; FastAPI (5 routes: documents, pages, extractions, patch measurement, explainers); SQLAlchemy + SQLite; `uv`; `openapi.yaml` as the contract; Make, Compose, and one CI workflow (test → eval → build the synthetic dashboard → deploy Pages). Build data-first: gold set and `schemas.py`, then extractor, then API, then UI.

## Data model

Provenance chain: **chart point → Measurement → Extraction → Page → Document → file hash.**

| Entity | Key fields | Rule |
|---|---|---|
| Document | `id` (sha256), `filename`, `kind`, `lab`, `received_date`, `page_count` | Re-ingesting the same file is a no-op |
| Page | `document_id`, `page_no`, `image_path`, `words` (text + bbox) | Every document has pages, even a single photo |
| Extraction | `label_raw`, `value_raw`, `unit_raw`, `ref_raw`, `flag_raw`, `date_raw`, `bbox`, `grounded` (auto, manual, none), `extractor`, `model`, `prompt_hash` | Immutable; one row per candidate |
| Measurement | `analyte`, `value`/`unit`, `value_original`/`unit_original`, `ref_low`/`ref_high`, `flag`, `collection_date`, `visit_id`, `lab`, `method`, `status`, `reviewed_at`, `note` | `status` ∈ {extracted, corrected, rejected}; charts show non-rejected AND grounded only |
| Visit | `date`, `clinic`, `document_ids[]` | Groups several PDFs into one visit; splits one PDF with several dates into several visits |
| Explainer | `analyte`, `species: dog`, `what_it_measures`, `why_ordered`, `general_causes_high/low[]`, `caveats[]`, `sources[]`, `last_reviewed` | Test fails if `sources` is empty or `species` ≠ dog |

Corrections never overwrite the raw extraction. A canonical unit is added only when `units.py` has a factor for that analyte; otherwise the chart shows the original unit with a note.

## Evaluation

`evals/gold/` holds synthetic reports with hand-labelled `expected.jsonl`. `atlas eval` (`evals/score.py`) reports precision, recall, unit errors, digit errors and wrong-visit rate. Every milestone closes on a number from this or from a timed run. Thresholds are set after the first real eval.

## Roadmap

- **M0:** gold set, `schemas.py`, `atlas eval` scoring.
- **First vertical slice:** photo preprocessing + OCR + vision adapter on one lab layout → ground → review → chart, for creatinine only, with the bbox round-tripping page → chart → page. The rules adapter runs on the synthetic text PDF for CI.
- **Then:** all analytes → remaining layouts and scans → explainers (15–20 analytes) → static demo plus a timed fresh-clone run (< 15 min).

## Repo layout

```
backend/app/{main,models,schemas,database,cli}.py
backend/app/extraction/{base,vision,rules,ground,pages}.py + prompts/
backend/app/normalization/{terminology,units,validators}.py
backend/app/services/{review,export}.py
frontend/src/pages/{Dashboard,Review,Sources}.tsx
knowledge/{explainers/,terminology.yaml,sources.yaml}
evals/{gold/,score.py}
data/synthetic/
docs/{spec,tasks,methodology,data-dictionary,getting-your-records,talking-to-your-vet,how-we-built-it}.md
```

## Privacy, content and license

- `ATLAS_DATA_DIR` (default `~/.canine-atlas/<dog>/`) is gitignored. The export strips clinic names, vet names and account numbers.
- Explainers are reviewed writing, not generated text. They cite `knowledge/sources.yaml` (Merck Veterinary Manual, eClinpath) and use "veterinarians consider" phrasing, never "this means".
- Synthetic reports are built from real layouts with values and identifiers replaced. They include a scan, a photo, a report with two collection dates, one with no reference intervals, and one in SI units.
- MIT license for the code and the explainer text; sources are linked, never copied.

## Open questions (before M0)

- [x] Document kinds: mostly phone photos. Still to do: count photos per lab layout.
- [ ] Which vision model provider, and is sending page images to it acceptable? (Blocking: with mostly photos, the no-API-key path covers very little real data.)
- [ ] How much of the OCR fails to ground (blur, glare, curled paper)? Measure on 10 real photos before M1.
- [ ] Do reports carry both a collection date and a report date?
- [ ] Which 15–20 analytes appear often enough to deserve explainers?
- [ ] Where is body weight recorded: lab reports, invoices or visit notes?
