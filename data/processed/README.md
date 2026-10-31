# Processed data

Values extracted from Kuro's records. The raw sources (WhatsApp chats, photos, invoices) stay in `data/raw/` and are not published.

| File | Rows | What it holds | Source |
|---|---|---|---|
| `visits.csv` | one per visit | date, clinic, visit type, short summary | chats, invoices |
| `invoice_items.csv` | one per invoice line | tests, procedures, medications, supplements, quantity, price (RM) | 24 FurKids invoices (Jul 2024 – Oct 2026, each reconciled to its printed total), 1 Petcare house-call invoice (amounts only) |
| `lab_comments.csv` | one per comment | interpretive comments printed by the IDEXX analyzers | IDEXX reports |
| `prescriptions.csv` | one per dispensed item | medication, purpose, dose, frequency, duration, instructions, with a confidence rating | photographed medicine labels and prescriptions |
| `lab_panels.csv` | one per analyte per test | IDEXX Catalyst chemistry (incl. ALT, ALKP, CREA, UREA), ProCyte CBC and SNAP 4Dx values with reference intervals and high/low flags | photographed clinic printouts |
| `lab_results.csv` | one per finding | earlier numbers and qualitative readings mentioned in chat | chats |
| `weights.csv` | one per weighing | weight in kg | chats |
| `imaging.csv` | one per study | ultrasound, x-ray, surgical photo, with measurements | chats, clinic images |
| `health_events.csv` | one per mention | symptoms, diagnoses, medications, care notes, quoted | chats |

## Conventions

- **Dates.** `date_basis` says where a date comes from. Invoice and image-header dates are Malaysia local dates. Chat dates are as exported, which runs about 15 hours behind Malaysia time, so a daytime visit can appear one day earlier than it happened.
- **Quotes** are verbatim from the chats, including typos. They record what was said, not a diagnosis.
- **Lab panels** come from 10 IDEXX report PDFs (parsed from their text layer, May 2024 – Aug 2026; each report also carries the previous result, which becomes its own row with `note = previous-result column`), plus photographed printouts for 2026-09-14, the one run without a PDF. Values typed from photos matched the PDFs wherever both exist. Flags are as printed for current results and computed from the same reference intervals for previous results. Values the analyzer marked `*` are kept with a note to confirm by blood film.
- **Removed:** people's names, addresses, phone numbers, the clinic patient ID, vehicle plates and bank details.

Clinics: **FurKids** (Furkids Wellness Veterinary Centre, regular vet), **Asia Paws** (acupuncture), **Petcare** (house call and clinic, Apr–May 2025).
