# os-kuro-archives

A longitudinal case study of **ageing, multiple illnesses and caregiving** in one dog: **Kuro**, a Golden Retriever mix (Embark: 52% Golden Retriever, 34% Japanese Spitz), born 10 Mar 2010 in Malaysia, died 18 Oct 2026, aged 16 years 7 months 8 days.

In his last two and a half years Kuro lived with an inoperable splenic tumour, anemia, pancreatitis, arthritis and gradual loss of mobility. The archive follows both his medical care and his daily care. They are related but distinct: a dog can keep receiving veterinary treatment while becoming more and more dependent on people for moving, toileting, hygiene and safety. It is not primarily a cancer case report.

It covers 2021 – Oct 2026. Sources are his vet invoices, in-house lab reports, X-rays, medicine labels, care notes and photos, and the WhatsApp chats with his family, vets, pet sitter, pet taxi and household helper.

## Start here

**If you care for an older dog**, read [What another senior-dog owner can learn from Kuro](docs/owners/lessons-for-owners.md). It has a care-transition timeline, showing when each problem moved from "watch it" to "needs daily help", and five short cases:

1. How do I recognize when my dog's normal routine needs to change?
2. Which clinical signs should prompt urgent veterinary attention?
3. What should I record and ask my vet when a blood-test result changes?
4. How do I organize daily care when several people share responsibility?
5. What should I budget and plan for if my dog loses mobility?

Each case sets out what happened to Kuro, what the records support, what remains unknown and questions to discuss with your own vet.

**If you want the full story or the data:**

- [Health summary](docs/case-study/health-summary.md): his story, the post-mortem findings, lab trends, recurring conditions, daily care, medications, diet and the gaps in the records.
- [`data/processed/`](data/processed/): everything as CSVs.

## What's here

**Documents (`docs/`)**

| Folder | Document | Contents |
|---|---|---|
| [`case-study/`](docs/case-study/) | [Health summary](docs/case-study/health-summary.md) | His story 2021–2026 as a narrative, the post-mortem findings with the vet's answers to follow-up questions, then the lab trend table, recurring themes (incl. trouble standing up), daily care and stools, medications, diet and gaps |
| | [Care protocol](docs/case-study/care-protocol.md) | His full care protocol (diet, supplements, medications, therapies, movement, hygiene, monitoring) in six-month blocks, 2020–2026 |
| [`analyses/`](docs/analyses/) | [Diet review](docs/analyses/diet-review.md) | His Mar 2024 home-formulated diet checked against published nutrient limits |
| | [DNA comparison](docs/analyses/dna-comparison.md) | Wisdom Panel (Jan 2023) vs Embark (Feb 2025): where the two DNA tests agree and disagree, scored item by item |
| [`owners/`](docs/owners/) | [Lessons for owners](docs/owners/lessons-for-owners.md) | Care-transition timeline and five case-based questions for other senior-dog owners |
| [`dog-aging-project/`](docs/dog-aging-project/) | [DAP surveys](docs/dog-aging-project/dap-surveys.md) | The eight Dog Aging Project survey sections answered for Kuro (End of Life, cognition, and the annual Age-Related Changes, Diet, Medications/Preventives, Physical Activity, Environment and Eating behaviour sections): what each asks, and his answers. Pairs with `data/dog_aging_project/` |

**Data and code**

| Path | Contents |
|---|---|
| [`data/processed/`](data/processed/) | Data recorded during his life (vet records, labs, chats, care notes, photos), cleaned into CSVs (table below) |
| [`data/dog_aging_project/dap_surveys_kuro.csv`](data/dog_aging_project/dap_surveys_kuro.csv) | Kuro's answers to eight Dog Aging Project survey sections, one row per DAP variable with DAP codes, all given or confirmed by his owner, each checked against his records in an `evidence` column. See [DAP surveys](docs/dog-aging-project/dap-surveys.md) |
| [`data/quality_of_life/hhhhhmm_kuro.csv`](data/quality_of_life/hhhhhmm_kuro.csv) | His quality of life scored on the HHHHHMM scale for each six-month block from 2024 to his death, with evidence; see [Reading the quality-of-life scores](#reading-the-quality-of-life-scores) |
| [`data/raw/imaging/`](data/raw/imaging/) | His X-rays (Jun–Jul 2024, Dec 2025) and abdominal ultrasound stills (Jul 2024), with the clinic's patient ID redacted |
| [`data/raw/genetics/embark/`](data/raw/genetics/embark/) | Embark DNA test (4 Feb 2025): the report (`embark_dna_report_2025-02-04.pdf`), the results export (`embark_results_2025-02-04.csv`) and raw genotypes in PLINK format (`embark_raw_genotypes/`). The Wisdom Panel report (29 Jan 2023) is kept private |
| [`scripts/triage_images.py`](scripts/triage_images.py) | Offline photo sorter (medical / dog / plates / unsure) used on the WhatsApp exports |

### The data

`data/` is split by when the data was recorded:

- **`raw/`**: the original records (WhatsApp exports with the PDFs and photos sent in them, Notion care notes, DNA reports, imaging). Private, except imaging and Embark.
- **`processed/`**: tables built from records made at the time, grouped by topic (`clinical/`, `daily_care/`, `life/`, `genetics/`, `communicator/`).
- **`dog_aging_project/`**: Dog Aging Project survey answers given after his death, described in [DAP surveys](docs/dog-aging-project/dap-surveys.md).
- **`quality_of_life/`**: quality-of-life scores made after his death, block by block, from his records and confirmed by his owner.

The processed tables, with their subfolder under `data/processed/`:

| File | Rows | What it holds |
|---|---|---|
| `clinical/visits.csv` | 89 | One row per clinic per day, with what exists for each visit (labs, weight, prescriptions, invoices, imaging) |
| `clinical/labs.csv` | 850 | IDEXX blood panels (chemistry, CBC, SDMA, electrolytes, 4Dx), analyzer comments and lab findings mentioned in chat |
| `clinical/prescriptions.csv` | 118 | Medications, supplements and care products, with kind, brand, dose and duration |
| `clinical/invoice_items.csv` | 228 | Every line of 27 vet invoices (RM) |
| `clinical/health_events.csv` | 461 | Symptoms, diagnoses, vet assessments, care notes and post-mortem findings, quoted from the sources |
| `clinical/weights.csv` | 24 | Weights from 2020 to 2026 |
| `clinical/imaging.csv` | 13 | X-rays, ultrasounds, biopsy and post-mortem photo |
| `clinical/providers.csv` | 22 | Clinics, carers, transport and other services used for his care |
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

## Reading the quality-of-life scores

[`hhhhhmm_kuro.csv`](data/quality_of_life/hhhhhmm_kuro.csv) scores Kuro on the **HHHHHMM Quality of Life Scale** (Villalobos), a scale vets use in palliative and hospice care. It has seven items, each scored **0 to 10, where 10 is best**:

| Item | Question |
|---|---|
| **Hurt** | Is pain well controlled, including his ability to breathe comfortably? |
| **Hunger** | Is he eating enough, with or without help? |
| **Hydration** | Is he drinking enough, or does he need encouragement or fluids? |
| **Hygiene** | Can he be kept clean, especially after toileting, and free of sores? |
| **Happiness** | Does he show interest and joy and respond to the family? |
| **Mobility** | Can he get up and walk without help? |
| **More good days than bad** | Do good days outnumber bad ones? |

**How to read a score.** In this archive the item scores follow fixed anchors: **10** no problem for a senior dog · **7–9** a mild or well-managed problem · **4–6** a moderate problem needing regular help or treatment · **1–3** severe or poorly controlled · **0** unmanageable. The seven items add up to a **total out of 70**; on this scale a **total above 35 is considered acceptable quality of life**, and a falling total, or bad days starting to outnumber good ones, is the point to talk with a vet about comfort and end-of-life care.

**How these were scored.** Each row is one item in one six-month block (`block`, `period`), matching the blocks in the [care protocol](docs/case-study/care-protocol.md#quality-of-life-across-the-blocks). The score describes his **typical** state across the block, not his best or worst day. Scores were first proposed from the records, then confirmed or changed by his owner (`answered_by`). `confidence` says how well the records support each score (high, medium, low), and `evidence` gives the dated records behind it.

**Limits.** The scale was designed to be scored in the moment, by the people caring for the dog; here it was scored after his death, which invites hindsight. Records are thinner where daily care wasn't written down (before Jun 2024, and after the household helper changed in Apr 2026). Treat differences of one or two points as noise and look at the direction of change.

**Kuro's results.** Totals of 60 (2024 H1), 47, 46, 51, 39 and 36 (2026 H2): acceptable throughout, but only just in his last months. Mobility and hygiene fell most; hunger and happiness held up.

## Using the data

The CSVs are plain files, sorted by date. `visits.csv` is the backbone: one row per clinic per day, with columns showing what exists for that visit. To chart lab values, use `labs.csv` filtered to `record_type = panel`.

## Notes

- **Not veterinary advice.** The summaries quote what vets and reports said; review documents (`diet-review.md`) are labelled as reviews.
- **Privacy.** Raw records (chat exports, photos, PDFs, Notion notes) are gitignored and not published, except the Embark DNA data and the diagnostic images in `data/raw/imaging/` (patient ID redacted). The CSVs exclude people's names (birthday greeters are shortened to two letters), addresses, phone numbers, client and patient IDs, vehicle plates and bank details.
- **Dates.** The WhatsApp exports were made on a phone set to US Pacific time; chat timestamps have been converted to Malaysia time where it matters (15–16 hours ahead, depending on daylight saving). Each CSV records its `date_basis`, and chat-based dates may be a day off.
- **How it was built.** Text-layer PDFs were parsed directly; photos were read by hand or with AI assistance and cross-checked against the PDFs where both exist; `confidence` columns flag uncertain readings.
