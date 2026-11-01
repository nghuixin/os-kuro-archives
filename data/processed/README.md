# Processed data

Values extracted from Kuro's records. The raw sources (WhatsApp chats, photos, invoices) stay in `data/raw/` and are not published.

| File | Rows | What it holds | Source |
|---|---|---|---|
| `visits.csv` | one per clinic per day | date, clinic, visit type, short summary, plus a cross-check of what exists for that visit: `lab_runs`, `lab_status` (`results present`, `billed, results missing`, `none`), `weight_kg` (all weights within ±1 day), `prescriptions`, `invoice_ids`, `imaging`. A count of 0 means nothing was found. | chats, invoices, lab reports, labels |
| `invoice_items.csv` | one per invoice line | tests, procedures, medications, supplements, quantity, price (RM) | 24 FurKids invoices (Jul 2024 – Oct 2026, each reconciled to its printed total), 1 Petcare house-call invoice (amounts only) |
| `labs.csv` | one per lab value, comment or reported finding | all lab data; `record_type` says which kind of row it is (see below) | IDEXX report PDFs, photographed printouts, chats |
| `prescriptions.csv` | one per dispensed item | medication, `kind`, `brand` (maker, empty if none recorded; "(probable)" if inferred rather than read on the label), purpose, dose, frequency, duration, instructions, with a confidence rating. `kind` is `medication` (licensed drugs and vet-prescribed therapeutics, incl. prescribed iron and Yunnan Baiyao), `supplement` (vitamins, minerals, probiotics, nutraceuticals, herbal and homeopathic remedies) or `care product` (cleaners, cleansers, conditioners, dental additives) | photographed medicine labels, prescriptions, care notes |
| `weights.csv` | one per weighing | weight in kg | chats |
| `imaging.csv` | one per study | ultrasound, x-ray, surgical photo, with measurements | chats, clinic images |
| `health_events.csv` | one per mention | symptoms, diagnoses, medications, care notes and post-mortem findings, quoted | Pet Taxi chat, FurKids chats |
| `feeding.csv` | one per food, instruction or diet change | what Kuro was fed: home-cooked ingredients, therapeutic foods, toppers, treats, feeding instructions and appetite changes, with amounts where given | photos, invoices, chats |
| `stool_log.csv` | one per stool photo | Purina fecal score (1-7), colour, blood, mucus, foreign material, notes; `method` says whether it was judged from a contact-sheet thumbnail or the full-size photo | Care chat photos (Jul 2024 - May 2025) |
| `home_care.csv` | one per hot-pack session (date + morning/evening) | time of first photo (Malaysia time), body site, number of photos | Care chat photos (May 2025 - Apr 2026) |
| `grooming.csv` | one per booked grooming session | date, service (basic grooming, dental cleaning), status (done, cancelled, not done) and the groomer's notes on his skin, ears and condition | grooming chat (Jan 2024 - Oct 2026) |
| `communicator_notes.csv` | one per impression or observation | health and pain impressions from an animal communicator's six communication reports and 43 remote reiki session notes, plus the owner's observations in the same chat: `session` (communication, reiki, owner observation), `reported_by`, `body_areas`, `impression`. **Non-clinical**: these are the communicator's intuitive impressions, not examinations; for reiki rows, `body_areas` are where healing was sent. Personal and family matters in the reports are left out. | communicator reports and chat (Jul 2024 - Sep 2026) |
| `socialisation.csv` | one per trip or outing | trips Kuro went on so far: start and end date (approximate where inferred), place, who went, activities, the evidence and a confidence rating. Trips his family took without him are not included | chats, the owner's recollection |
| `dna_comparison.csv` | one per compared item | Wisdom Panel (Jan 2023) vs Embark (Feb 2025): `area` (ancestry, health, trait, other), each test's result and `agree` (1 or 0); breed percentages agree when within 5 points; health genes matched by gene. See `docs/dna-comparison.md` | both DNA reports |
| `milestones.csv` | one per milestone | birthdays and how they were celebrated, age milestones, the 2024 prognosis and the dates he outlived it, his passing and farewell; `age` in years | chats |
| `birthday_wishes.csv` | one per form response | wishes and RSVPs for his 15th birthday (Mar 2025): timestamp, greeter (first two letters of each name only), in-person attendance, message | birthday form responses |
| `providers.csv` | one per service provider | clinics, pet carers, transport and other services used while Kuro was alive, with type, service, first and last month, `status` (used, booked only, emergency contact only) and evidence. People's names are omitted. | chats, invoices, labels, care notes |
| `diet.csv` | one per nutrient | home-cooked NRC-balanced senior recipe: macronutrients, amino acids, fatty acids, minerals, vitamins vs NRC allowance | diet analysis PDF, Mar 2024 |

## `labs.csv`

| `record_type` | Rows | Columns used |
|---|---|---|
| `panel` | one per analyte per analyzer run: IDEXX Catalyst chemistry and electrolytes, ProCyte CBC, SNAP 4Dx and cPL | `time`, `lab`, `analyzer`, `analyte`, `value`, `unit`, `ref_low`, `ref_high`, `flag`, `confidence` |
| `analyzer comment` | one per interpretive comment the analyzer printed for a run (match on `date`, `time`, `analyzer`) | `comment` |
| `reported` | numbers or readings mentioned in chat with no printout (e.g. "a bit anemic", blood type DEA 1+) | `value` or `qualitative` |

Filter on `record_type = panel` for charting. `date_basis` is `lab report` for panels and comments, `chat` for reported rows.

## Conventions

- **Dates.** `date_basis` says where a date comes from. Invoice and image-header dates are Malaysia local dates. Chat dates are as exported, which runs about 15 hours behind Malaysia time, so a daytime visit can appear one day earlier than it happened.
- **Quotes** are verbatim from the chats, including typos. They record what was said, not a diagnosis.
- **Lab panels** come from 10 IDEXX report PDFs (parsed from their text layer, May 2024 – Aug 2026; each report also carries the previous result, which becomes its own row with `note = previous-result column`), plus photographed printouts for 2026-09-14, the one run without a PDF. Values typed from photos matched the PDFs wherever both exist. Flags are as printed for current results and computed from the same reference intervals for previous results. Values the analyzer marked `*` are kept with a note to confirm by blood film.
- **Removed:** people's names, addresses, phone numbers, the clinic patient ID, vehicle plates and bank details.

Clinics: **FurKids** (Furkids Wellness Veterinary Centre, regular vet), **Asia Paws** (acupuncture), **Petcare** (house call and clinic, Apr–May 2025).
