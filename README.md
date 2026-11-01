# os-kuro-archives

A longitudinal case study of **ageing, multiple illnesses and caregiving** in one dog: **Kuro**, a Golden Retriever mix (Embark: 52% Golden Retriever, 34% Japanese Spitz), born 10 Mar 2010 in Malaysia, died 18 Oct 2026, aged 16.

In his last two and a half years Kuro lived with an inoperable splenic tumour, anemia, pancreatitis, arthritis and gradual loss of mobility. The archive follows both his medical care and his daily care. They are related but distinct: a dog can keep receiving veterinary treatment while becoming more and more dependent on people for moving, toileting, hygiene and safety. It is not primarily a cancer case report.

It covers 2021 – Oct 2026. Sources are his vet invoices, in-house lab reports, X-rays, medicine labels, care notes and photos, and the WhatsApp chats with his family, vets, pet sitter, pet taxi and household helper.

## Start here

**If you care for an older dog**, read [What another senior-dog owner can learn from Kuro](docs/lessons-for-owners.md). It has a care-transition timeline, showing when each problem moved from "watch it" to "needs daily help", and five short cases:

1. How do I recognize when my dog's normal routine needs to change?
2. Which clinical signs should prompt urgent veterinary attention?
3. What should I record and ask my vet when a blood-test result changes?
4. How do I organize daily care when several people share responsibility?
5. What should I budget and plan for if my dog loses mobility?

Each case sets out what happened to Kuro, what the records support, what remains unknown and questions to discuss with your own vet.

**If you want the full story or the data:**

- [`docs/health-summary.md`](docs/health-summary.md): his story in one page: timeline, lab trends, recurring conditions, home care, medications, diet and the gaps in the records.
- [`data/processed/`](data/processed/): everything as CSVs, with a [column guide](data/processed/README.md).

**Canine Health Atlas.** This archive is also the reference dataset for the Canine Health Atlas, a planned tool that would turn any dog's vet records into a source-linked dataset and dashboard. The Atlas is specified in [`docs/spec.md`](docs/spec.md) but not yet built; what exists today is this hand-built archive.

## What's here

| Path | Contents |
|---|---|
| [`docs/lessons-for-owners.md`](docs/lessons-for-owners.md) | For owners: care-transition timeline and five case-based questions |
| [`docs/instruments/`](docs/instruments/README.md) | Validated scales for monitoring a senior dog (quality of life, pain, cognition, body and muscle condition, frailty), with evidence, where to get each form, and a [recording template](data/templates/senior_monitoring_template.csv) |
| [`docs/health-summary.md`](docs/health-summary.md) | Timeline 2021–2026, lab trend table, recurring themes, home care and stools, diet and feeding, medications, gaps |
| [`docs/diet-critique.md`](docs/diet-critique.md) | Review of his home-cooked diet against published nutrient limits |
| [`docs/dna-comparison.md`](docs/dna-comparison.md) | Wisdom Panel vs Embark: where the two DNA tests agree and disagree, scored item by item |
| [`docs/spec.md`](docs/spec.md) | Spec for the Canine Health Atlas, updated with what building this archive taught us |
| [`data/processed/`](data/processed/) | The extracted data (table below) |
| [`data/raw/embark/`](data/raw/embark/) | Embark DNA results and raw genotypes, with an [analysis plan](data/raw/embark/analysis-plan.md) |
| [`scripts/triage_images.py`](scripts/triage_images.py) | Offline photo sorter (medical / dog / plates / unsure) used on the WhatsApp exports |

### The data

| File | Rows | What it holds |
|---|---|---|
| `visits.csv` | 89 | One row per clinic per day, with what exists for each visit (labs, weight, prescriptions, invoices, imaging) |
| `labs.csv` | 850 | IDEXX blood panels (chemistry, CBC, SDMA, electrolytes, 4Dx), analyzer comments and lab findings mentioned in chat |
| `prescriptions.csv` | 118 | Medications, supplements and care products, with kind, brand, dose and duration |
| `invoice_items.csv` | 228 | Every line of 27 vet invoices (RM) |
| `health_events.csv` | 462 | Symptoms, diagnoses, vet assessments, care notes and post-mortem findings, quoted from the sources |
| `weights.csv` | 24 | Weights from 2020 to 2026 |
| `imaging.csv` | 13 | X-rays, ultrasounds, biopsy and post-mortem photo |
| `feeding.csv` | 33 | What he ate: home-cooked meals, therapeutic diets, toppers, treats, feeding instructions |
| `diet.csv` | 53 | Nutrient analysis of his Mar 2024 home-cooked recipe |
| `home_care.csv` | 321 | Hot/cold pack sessions on his hips and hindquarters (May 2025 – Apr 2026) |
| `stool_log.csv` | 63 | Stool photos scored on the Purina Fecal Scoring Chart by two independent raters, with shape, colour, blood and mucus (Jul 2024 – May 2025) |
| `grooming.csv` | 54 | Home grooming sessions with the groomer's notes on his skin and ears (Jan 2024 – Oct 2026) |
| `communicator_notes.csv` | 61 | Non-clinical health and pain impressions from an animal communicator's reports and reiki notes, with the owner's observations (Jul 2024 – Sep 2026) |
| `socialisation.csv` | 3 | Trips Kuro went on: Dusun eco resort (Jul 2024), Penang (Dec 2024 and Sep 2025) |
| `dna_comparison.csv` | 35 | Wisdom Panel vs Embark, one row per compared item, scored 1 (agree) or 0 (disagree) |
| `providers.csv` | 22 | Clinics, carers, transport and other services used for his care |
| `milestones.csv` | 21 | Birthdays, celebrations and life milestones |
| `birthday_wishes.csv` | 11 | Messages for his 15th birthday |

## Using the data

The CSVs are plain files, sorted by date. `visits.csv` is the backbone: one row per clinic per day, with columns showing what exists for that visit. To chart lab values, use `labs.csv` filtered to `record_type = panel`.

## Notes

- **Not veterinary advice.** The summaries quote what vets and reports said; review documents (`diet-critique.md`) are labelled as reviews.
- **Privacy.** Raw records (chat exports, photos, PDFs, Notion notes) are gitignored and not published, except the Embark DNA data. The CSVs exclude people's names (birthday greeters are shortened to two letters), addresses, phone numbers, client and patient IDs, vehicle plates and bank details.
- **Dates.** The WhatsApp exports were made on a phone set to US Pacific time; chat timestamps have been converted to Malaysia time where it matters (15–16 hours ahead, depending on daylight saving). Each CSV records its `date_basis`, and chat-based dates may be a day off.
- **How it was built.** Text-layer PDFs were parsed directly; photos were read by hand or with AI assistance and cross-checked against the PDFs where both exist; `confidence` columns flag uncertain readings.
