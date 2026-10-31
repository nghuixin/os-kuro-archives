# os-kuro-archives

A health archive for **Kuro**, a golden-retriever mix (10 Mar 2010 – 18 Oct 2026), built from his vet records, lab reports, invoices, medicine labels, care notes and WhatsApp messages with his vets and carers, Jan 2023 – Oct 2026.

It is also the reference dataset for the **Canine Health Atlas**, a planned tool that turns a dog's vet records into a source-linked dataset and dashboard (see [`docs/spec.md`](docs/spec.md)).

## What's here

| Path | Contents |
|---|---|
| [`docs/health-summary.md`](docs/health-summary.md) | Timeline, lab trends, recurring conditions, medications, diet and gaps |
| [`docs/diet-critique.md`](docs/diet-critique.md) | Review of his home-cooked diet against published nutrient limits |
| [`docs/spec.md`](docs/spec.md) | Spec for the Canine Health Atlas |
| [`data/processed/`](data/processed/) | The extracted data as CSVs: lab values, visits, prescriptions (medications and supplements, with brands), feeding, weights, imaging, invoices, health events. [Column guide](data/processed/README.md). |
| [`data/raw/embark/`](data/raw/embark/) | Embark DNA results and raw genotypes, with an [analysis plan](data/raw/embark/analysis-plan.md) |

## Using the data

The CSVs are plain files, sorted by date. `visits.csv` is the backbone: one row per clinic per day, with columns showing which lab results, weights, prescriptions, invoices and imaging exist for that visit. To chart lab values, use `labs.csv` filtered to `record_type = panel`.

## Notes

- **Not veterinary advice.** The summaries quote what vets and reports said; the review documents (`diet-critique.md`) are labelled as reviews.
- **Privacy.** Raw records (chat exports, photos, PDFs, Notion notes) are not published. The CSVs exclude people's names, addresses, phone numbers, client and patient IDs, vehicle plates and bank details.
- **Dates.** Chat timestamps run about 15 hours behind Malaysia time, so some dates are a day early; each CSV records its `date_basis`.
