# os-kuro-archives

A longitudinal case study of **ageing, multiple illnesses and caregiving** in one dog: **Kuro**, a Golden Retriever mix (Embark: 52% Golden Retriever, 34% Japanese Spitz), born 10 Mar 2010 in Malaysia, died 18 Oct 2026, aged 16 years 7 months 8 days.

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
- [`data/processed/`](data/processed/): everything as CSVs.

**Canine Health Atlas.** This archive is also the reference dataset for the Canine Health Atlas, a planned tool that would turn any dog's vet records into a source-linked dataset and dashboard. The Atlas is specified in [`docs/spec.md`](docs/spec.md) but not yet built; what exists today is this hand-built archive.

## What's here

| Path | Contents |
|---|---|
| [`docs/lessons-for-owners.md`](docs/lessons-for-owners.md) | For owners: care-transition timeline and five case-based questions |
| [`docs/kuro-protocol.md`](docs/kuro-protocol.md) | His full care protocol (diet, supplements, medications, therapies, movement, hygiene, monitoring) in six-month blocks, 2020–2026 |
| [`docs/instruments/`](docs/instruments/) | Validated scales for monitoring a senior dog (quality of life, pain, cognition, body and muscle condition, frailty), with evidence, where to get each form, and a [recording template](data/reference/senior_monitoring_template.csv); plus the [Dog Aging Project's](docs/instruments/dog-aging-project.md) End of Life Survey and cognition survey, with Kuro's end-of-life answers from his records |
| [`docs/health-summary.md`](docs/health-summary.md) | His story 2021–2026 as a narrative, the post-mortem findings with the vet's answers to follow-up questions, then the lab trend table, recurring themes (incl. trouble standing up), daily care and stools, medications, diet and gaps |
| [`docs/diet-critique.md`](docs/diet-critique.md) | Review of his home-cooked diet against published nutrient limits |
| [`docs/dna-comparison.md`](docs/dna-comparison.md) | Wisdom Panel vs Embark: where the two DNA tests agree and disagree, scored item by item |
| [`docs/spec.md`](docs/spec.md) | Spec for the Canine Health Atlas, updated with what building this archive taught us |
| [`data/processed/`](data/processed/) | Data recorded during his life (vet records, labs, chats, care notes, photos), cleaned into CSVs (table below) |
| [`data/retrospective/dap_surveys_kuro.csv`](data/retrospective/dap_surveys_kuro.csv) | Kuro scored retrospectively on the Dog Aging Project's End of Life, cognition (CSLB) and Age-Related Changes surveys, plus the AFUS Diet and Medications/Preventives sections, laid out like a DAP response: one row per DAP variable, with DAP's variable names and answer codes as in the DAP codebook (tick-box items are `True`/`False`; see the [DAP survey notes](docs/instruments/dog-aging-project.md)). Every answer was given or confirmed by his owner after his death (Oct–Nov 2026; `answered_by` = `owner`); some were first prefilled from his records and then accepted, as noted in `evidence`. `evidence` checks each answer against what was written at the time (chats, vet records, labs): it starts with a verdict (`supports`, `contradicts`, `mixed`, `not mentioned` or `not checkable`) followed by dated, sourced quotes, and notes where the owner revised an answer after seeing the evidence |
| [`data/raw/imaging/`](data/raw/imaging/) | His X-rays (Jun–Jul 2024, Dec 2025) and abdominal ultrasound stills (Jul 2024), with the clinic's patient ID redacted |
| [`data/raw/genetics/embark/`](data/raw/genetics/embark/) | Embark DNA results and raw genotypes, with an [analysis plan](data/raw/genetics/embark/analysis-plan.md) |
| [`scripts/triage_images.py`](scripts/triage_images.py) | Offline photo sorter (medical / dog / plates / unsure) used on the WhatsApp exports |

### The data

`data/` is split by when the data was recorded:

- **`raw/`**: the original records (WhatsApp exports with the PDFs and photos sent in them, Notion care notes, DNA reports, imaging). Private, except imaging and Embark.
- **`processed/`**: tables built from records made at the time, grouped by topic (`clinical/`, `daily_care/`, `life/`, `genetics/`, `communicator/`).
- **`retrospective/`**: survey answers made after his death, from his records and from his owner.
- **`reference/`**: the blank monitoring template.

The processed tables, with their subfolder under `data/processed/`:

| File | Rows | What it holds |
|---|---|---|
| `clinical/visits.csv` | 89 | One row per clinic per day, with what exists for each visit (labs, weight, prescriptions, invoices, imaging) |
| `clinical/labs.csv` | 850 | IDEXX blood panels (chemistry, CBC, SDMA, electrolytes, 4Dx), analyzer comments and lab findings mentioned in chat |
| `clinical/prescriptions.csv` | 118 | Medications, supplements and care products, with kind, brand, dose and duration |
| `clinical/invoice_items.csv` | 228 | Every line of 27 vet invoices (RM) |
| `clinical/health_events.csv` | 462 | Symptoms, diagnoses, vet assessments, care notes and post-mortem findings, quoted from the sources |
| `clinical/weights.csv` | 24 | Weights from 2020 to 2026 |
| `clinical/imaging.csv` | 13 | X-rays, ultrasounds, biopsy and post-mortem photo |
| `clinical/providers.csv` | 21 | Clinics, carers, transport and other services used for his care |
| `daily_care/feeding.csv` | 33 | What he ate: home-cooked meals, therapeutic diets, toppers, treats, feeding instructions |
| `daily_care/diet.csv` | 53 | Nutrient analysis of his Mar 2024 home-cooked recipe |
| `daily_care/home_care.csv` | 321 | Hot/cold pack sessions on his hips and hindquarters (May 2025 – Apr 2026) |
| `daily_care/stool_log.csv` | 63 | Stool photos scored on the Purina Fecal Scoring Chart by two independent raters, with shape, colour, blood and mucus (Jul 2024 – May 2025) |
| `daily_care/grooming.csv` | 54 | Home grooming sessions with the groomer's notes on his skin and ears (Jan 2024 – Oct 2026) |
| `life/socialisation.csv` | 3 | Trips Kuro went on: Dusun eco resort (Jul 2024), Penang (Dec 2024 and Sep 2025) |
| `life/milestones.csv` | 21 | Birthdays, celebrations and life milestones |
| `life/birthday_wishes.csv` | 11 | Messages for his 15th birthday |
| `genetics/dna_comparison.csv` | 35 | Wisdom Panel vs Embark, one row per compared item, scored 1 (agree) or 0 (disagree) |
| `communicator/communicator_notes.csv` | 61 | Non-clinical health and pain impressions from an animal communicator's reports and reiki notes, with the owner's observations (Jul 2024 – Sep 2026) |

## Using the data

The CSVs are plain files, sorted by date. `visits.csv` is the backbone: one row per clinic per day, with columns showing what exists for that visit. To chart lab values, use `labs.csv` filtered to `record_type = panel`.

## Notes

- **Not veterinary advice.** The summaries quote what vets and reports said; review documents (`diet-critique.md`) are labelled as reviews.
- **Privacy.** Raw records (chat exports, photos, PDFs, Notion notes) are gitignored and not published, except the Embark DNA data and the diagnostic images in `data/raw/imaging/` (patient ID redacted). The CSVs exclude people's names (birthday greeters are shortened to two letters), addresses, phone numbers, client and patient IDs, vehicle plates and bank details.
- **Dates.** The WhatsApp exports were made on a phone set to US Pacific time; chat timestamps have been converted to Malaysia time where it matters (15–16 hours ahead, depending on daylight saving). Each CSV records its `date_basis`, and chat-based dates may be a day off.
- **How it was built.** Text-layer PDFs were parsed directly; photos were read by hand or with AI assistance and cross-checked against the PDFs where both exist; `confidence` columns flag uncertain readings.
