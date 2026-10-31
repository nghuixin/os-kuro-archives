# Processed data

Values extracted from Kuro's records. The raw sources (WhatsApp chats, photos, invoices) stay in `data/raw/` and are not published.

| File | Rows | What it holds | Source |
|---|---|---|---|
| `visits.csv` | one per visit | date, clinic, visit type, short summary | chats, invoices |
| `invoice_items.csv` | one per invoice line | tests, procedures, medications, supplements, quantity, price (RM) | 24 FurKids invoices (Jul 2024 – Oct 2026, each reconciled to its printed total), 1 Petcare house-call invoice (amounts only) |
| `labs.csv` | one per lab value, comment or reported finding | all lab data; `record_type` says which kind of row it is (see below) | IDEXX report PDFs, photographed printouts, chats |
| `prescriptions.csv` | one per dispensed item | medication, purpose, dose, frequency, duration, instructions, with a confidence rating | photographed medicine labels and prescriptions |
| `weights.csv` | one per weighing | weight in kg | chats |
| `imaging.csv` | one per study | ultrasound, x-ray, surgical photo, with measurements | chats, clinic images |
| `health_events.csv` | one per mention | symptoms, diagnoses, medications, care notes and post-mortem findings, quoted | Pet Taxi chat, FurKids chats |
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
