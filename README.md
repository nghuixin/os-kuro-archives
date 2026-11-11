# os-kuro-archives

A longitudinal case study of **ageing, multiple illnesses and caregiving** in one dog: **Kuro**, a Golden Retriever mix (Embark: 52% Golden Retriever, 34% Japanese Spitz), born 10 Mar 2010 in Malaysia, died 18 Oct 2026, aged 16 years 7 months 8 days.

In his last two and a half years Kuro lived with an inoperable splenic tumour (never typed, and never shown to be malignant), anemia, pancreatitis, arthritis and gradual loss of mobility. The archive follows both his medical care and his daily care. They are related but distinct: a dog can keep receiving veterinary treatment while becoming more and more dependent on people for moving, toileting, hygiene and safety. It is not primarily a tumour case report.

It covers 2021 – Oct 2026. Sources are his vet invoices, in-house lab reports, X-rays, medicine labels, care notes and photos, and the WhatsApp chats with his family, vets, pet sitter, pet taxi and household helper.

## Start here

**If you care for an older dog**, read [What another senior-dog owner can learn from Kuro](docs/owners/lessons-for-owners.md). It has a care-transition timeline, showing when each problem moved from "watch it" to "needs daily help", and five short cases:

1. How do I recognize when my dog's normal routine needs to change?
2. Which clinical signs should prompt urgent veterinary attention?
3. What should I record and ask my vet when a blood-test result changes?
4. How do I organize daily care when several people share responsibility?
5. What should I budget and plan for if my dog loses mobility?

Each case sets out what happened to Kuro, what the records support, what remains unknown and questions to discuss with your own vet.

**If you are facing end-of-life decisions**, read [End-of-life thresholds](docs/case-study/end-of-life-thresholds.md), which applies two end-of-life checklists to Kuro block by block.

**If you want the full story or the data:**

- [Health summary](docs/case-study/health-summary.md): his story, the post-mortem findings, lab trends, recurring conditions, daily care, medications, diet and the gaps in the records.
- [`data/processed/`](data/processed/): everything as CSVs.

## Repository layout

```
os-kuro-archives/
├── docs/
│   ├── case-study/          health summary, care protocol, end-of-life thresholds
│   ├── owners/              lessons for owners, vet's palliative-care guide (PDF)
│   ├── analyses/            diet review, DNA test comparison
│   └── dog-aging-project/   Dog Aging Project survey answers, explained
├── data/
│   ├── processed/           CSVs built from records made during his life
│   │   ├── clinical/        visits, labs, prescriptions, invoices, health events, weights, imaging, providers
│   │   ├── daily_care/      feeding, diet, home care, stool log, grooming
│   │   ├── life/            trips, milestones, birthday wishes
│   │   ├── genetics/        Wisdom Panel vs Embark comparison
│   │   └── communicator/    animal communicator notes
│   ├── dog_aging_project/   DAP survey answers (scored after his death)
│   ├── quality_of_life/     HHHHHMM quality-of-life and CBPI pain scores (scored after his death)
│   └── raw/                 original records; only imaging/ and genetics/ are published
│       ├── imaging/         X-rays and ultrasound stills
│       └── genetics/        embark/, wisdom_panel/
└── scripts/
    └── triage_images.py     offline photo sorter for the WhatsApp exports
```

## Documents (`docs/`)

| Folder | Document | Contents |
|---|---|---|
| [`case-study/`](docs/case-study/) | [Health summary](docs/case-study/health-summary.md) | His story 2021–2026 as a narrative, the post-mortem findings with the vet's answers to follow-up questions, then the lab trend table, recurring themes (incl. trouble standing up), daily care and stools, medications, diet and gaps |
| | [Care protocol](docs/case-study/care-protocol.md) | His full care protocol (diet, supplements, medications, therapies, movement, hygiene, monitoring) in six-month blocks, 2020–2026, with quality of life across the blocks |
| | [End-of-life thresholds](docs/case-study/end-of-life-thresholds.md) | Kuro as a case study for end-of-life decision points: the HHHHHMM scale and his vet's palliative-care guide compared, applied block by block, with the emergency signs that occurred and lessons for owners |
| [`owners/`](docs/owners/) | [Lessons for owners](docs/owners/lessons-for-owners.md) | Care-transition timeline and five case-based questions for other senior-dog owners |
| | [Palliative care guide (PDF)](docs/owners/FWVC_PalliativeEnd-of-Life-Care-Support-Guide_2025.pdf) | Furkids Wellness Veterinary Centre's palliative and end-of-life care guide (2025): quality-of-life checklist, when to talk to the vet, emergency signs, home-setup tips |
| [`analyses/`](docs/analyses/) | [Diet review](docs/analyses/diet-review.md) | His Mar 2024 home-formulated diet checked against published nutrient limits |
| | [Supplement review](docs/analyses/supplement-review.md) | Every supplement he took, grouped by ingredient, graded by the strength of evidence in dogs: clinically validated, research stage, tested and not supported, or no credible evidence |
| | [DNA comparison](docs/analyses/dna-comparison.md) | Wisdom Panel (Jan 2023) vs Embark (Feb 2025): where the two DNA tests agree and disagree, scored item by item |
| [`dog-aging-project/`](docs/dog-aging-project/) | [DAP surveys](docs/dog-aging-project/dap-surveys.md) | The eight Dog Aging Project survey sections answered for Kuro (End of Life, cognition, and the annual Age-Related Changes, Diet, Medications/Preventives, Physical Activity, Environment and Eating behaviour sections): what each asks, and his answers. Pairs with `data/dog_aging_project/` |
| | [Kuro vs DAP findings](docs/dog-aging-project/kuro-vs-dap-findings.md) | Where Kuro sits against published Dog Aging Project studies of similar dogs: lifespan by size and breed type, multimorbidity, disease history, cognition, and end-of-life patterns |

## Data (`data/`)

`data/` is split by when the data was recorded:

| Folder | What it holds |
|---|---|
| [`processed/`](data/processed/) | Tables built from records made at the time, grouped by topic (table below) |
| [`dog_aging_project/`](data/dog_aging_project/) | [`dap_surveys_kuro.csv`](data/dog_aging_project/dap_surveys_kuro.csv) (468 rows): Kuro's answers to eight Dog Aging Project survey sections, one row per DAP variable with DAP codes, all given or confirmed by his owner after his death, each checked against his records in an `evidence` column. See [DAP surveys](docs/dog-aging-project/dap-surveys.md) |
| [`quality_of_life/`](data/quality_of_life/) | [`hhhhhmm_kuro.csv`](data/quality_of_life/hhhhhmm_kuro.csv) (42 rows): his quality of life scored on the HHHHHMM scale for each six-month block from 2024 to his death, made after his death from his records and confirmed by his owner. See [Reading the quality-of-life scores](#reading-the-quality-of-life-scores). [`cbpi_kuro.csv`](data/quality_of_life/cbpi_kuro.csv) (66 rows): Canine Brief Pain Inventory for the same blocks, item numbers and scores only, confirmed by his owner. See [Reading the pain scores](#reading-the-pain-scores) |
| [`raw/`](data/raw/) | The original records (WhatsApp exports with the PDFs and photos sent in them, Notion care notes, DNA reports, imaging). Private and gitignored, except the two folders below |
| [`raw/imaging/`](data/raw/imaging/) | 11 images: X-rays (30 Jun 2024, 11 Jul 2024, 29 Dec 2025) and abdominal ultrasound stills (1 Jul 2024), with the clinic's patient ID redacted |
| [`raw/genetics/embark/`](data/raw/genetics/embark/) | Embark DNA test (4 Feb 2025): the report (`embark_dna_report_2025-02-04.pdf`), the results export (`embark_results_2025-02-04.csv`) and raw genotypes in PLINK format (`embark_raw_genotypes/`) |
| [`raw/genetics/wisdom_panel/`](data/raw/genetics/wisdom_panel/) | Wisdom Panel DNA test (29 Jan 2023): the full report (`wisdom_panel_dna_report_2023-01-29.pdf`) with breed ancestry, 210 health conditions tested (all clear) and traits. Compared with Embark in the [DNA comparison](docs/analyses/dna-comparison.md) |

### Processed tables

Paths are relative to `data/processed/`.

| File | Rows | What it holds |
|---|---|---|
| `clinical/visits.csv` | 142 | One row per clinic per day, with what exists for each visit (labs, weight, prescriptions, invoices, imaging) |
| `clinical/labs.csv` | 850 | IDEXX blood panels (chemistry, CBC, SDMA, electrolytes, 4Dx), analyzer comments and lab findings mentioned in chat |
| `clinical/prescriptions.csv` | 118 | Medications, supplements and care products, with kind, brand, dose and duration |
| `clinical/invoice_items.csv` | 228 | Every line of 29 vet invoices (RM) |
| `clinical/health_events.csv` | 469 | Symptoms, diagnoses, vet assessments, care notes and post-mortem findings, quoted from the sources |
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

### Using the data

The CSVs are plain files, sorted by date. `clinical/visits.csv` is the backbone: one row per clinic per day, with columns showing what exists for that visit. To chart lab values, use `clinical/labs.csv` filtered to `record_type = panel`.

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

## Reading the pain scores

[`cbpi_kuro.csv`](data/quality_of_life/cbpi_kuro.csv) scores Kuro on the **Canine Brief Pain Inventory** (CBPI; Brown et al., University of Pennsylvania), an owner-completed pain questionnaire validated in dogs with osteoarthritis. It asks about the past 7 days, on a scale from **0 (no pain / no interference) to 10 (extreme)**:

- **Pain severity:** worst, least and average pain, and pain right now (items 1–4, averaged).
- **Pain interference:** how much pain got in the way of general activity, enjoyment of life, rising, walking, running and climbing (items 5–10, averaged).
- **Overall quality of life:** item 11, from poor to excellent.

The instrument is copyrighted, so the file stores **item numbers and scores only**, not the questions.

**How these were scored.** As for HHHHHMM: one typical week per six-month block, proposed from the chats and vet records, then confirmed by his owner. Each row has `confidence` and dated `evidence`. "Pain right now" can't be observed after the fact, so it was set to the average pain.

**Limits.** The CBPI attributes all interference to pain; it can't separate weakness. In 2026, when his hind-limb weakness (sarcopenia) worsened, the interference scores overstate pain's role. Several pain observations come from acupuncture pulse readings, which aren't a validated measure. Running and climbing were rarely recorded, so those scores are low-confidence.

**Kuro's results.**

| Block | 2024 H1 | 2024 H2 | 2025 H1 | 2025 H2 | 2026 H1 | 2026 H2 |
|---|---|---|---|---|---|---|
| Pain severity | 1.3 | 3.0 | **4.3** | 3.0 | 3.8 | 3.5 |
| Pain interference | 1.3 | 3.2 | 4.7 | 2.8 | 5.3 | **6.2** |
| Overall | very good | good | good | good | fair | fair |

- **Pain peaked in 2025 H1** (he snapped when in pain, and Galliprant and gabapentin were started), then held at a moderate level on gabapentin, acupuncture and heat packs.
- **Interference kept rising while pain didn't.** His decline in 2026 was driven by lost function more than by worsening pain, consistent with the End of Life Survey answer of poor mobility from both weakness and pain.

## Scripts (`scripts/`)

[`triage_images.py`](scripts/triage_images.py) labels each photo from the WhatsApp exports as medical, dog, exclude (licence plates), other or unsure, fully offline (YOLO for dogs and vehicles, RapidOCR for text). It writes an index and a review gallery into `data/raw/` and moves nothing. It needs the private raw exports and the YOLO weights at `scripts/models/yolov8n.pt` (not committed), and runs with [uv](https://docs.astral.sh/uv/):

```
uv run scripts/triage_images.py [--limit N]
```

## Notes

- **Not veterinary advice.** The summaries quote what vets and reports said; review documents (`diet-review.md`) are labelled as reviews.
- **Privacy.** Raw records (chat exports, photos, PDFs, Notion notes) are gitignored and not published, except the Embark and Wisdom Panel DNA reports and the diagnostic images in `data/raw/imaging/` (patient ID redacted). The CSVs exclude people's names (birthday greeters are shortened to two letters), addresses, phone numbers, client and patient IDs, vehicle plates and bank details.
- **Dates.** The WhatsApp exports were made on a phone set to US Pacific time; chat timestamps have been converted to Malaysia time where it matters (15–16 hours ahead, depending on daylight saving). Each CSV records its `date_basis`, and chat-based dates may be a day off.
- **How it was built.** Text-layer PDFs were parsed directly; photos were read by hand or with AI assistance and cross-checked against the PDFs where both exist; `confidence` columns flag uncertain readings.
