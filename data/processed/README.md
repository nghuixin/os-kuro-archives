# Processed data

Values extracted from Kuro's records. The raw sources (WhatsApp chats, photos, invoices) stay in `data/raw/` and are not published.

| File | Rows | What it holds | Source |
|---|---|---|---|
| `visits.csv` | one per visit | date, clinic, visit type, short summary | chats, invoices |
| `invoice_items.csv` | one per invoice line | tests, medications, supplements, quantity, price (RM) | 4 Furkids invoices |
| `lab_panels.csv` | one per analyte per test | IDEXX Catalyst chemistry (incl. ALT, ALKP, CREA, UREA), ProCyte CBC and SNAP 4Dx values with reference intervals and high/low flags | photographed clinic printouts |
| `lab_results.csv` | one per finding | earlier numbers and qualitative readings mentioned in chat | chats |
| `weights.csv` | one per weighing | weight in kg | chats |
| `imaging.csv` | one per study | ultrasound, x-ray, surgical photo, with measurements | chats, clinic images |
| `health_events.csv` | one per mention | symptoms, diagnoses, medications, care notes, quoted | chats |

## Conventions

- **Dates.** `date_basis` says where a date comes from. Invoice and image-header dates are Malaysia local dates. Chat dates are as exported, which runs about 15 hours behind Malaysia time, so a daytime visit can appear one day earlier than it happened.
- **Quotes** are verbatim from the chats, including typos. They record what was said, not a diagnosis.
- **Lab panels** were transcribed from photos of the clinic printouts: full panels for 2026-07-01, 2026-08-10 and 2026-09-14 (each report also shows the previous result), a partial panel for 2026-02-04 (`confidence = medium`), and SNAP 4Dx results for 2024-06-28 and 2026-09-14. Flags are computed from the printed reference intervals and match the printouts. No SDMA value appears in any record; earlier panels need to be requested from the clinic.
- **Removed:** people's names, addresses, phone numbers, the clinic patient ID, vehicle plates and bank details.

Clinics: **FurKids** (Furkids Wellness Veterinary Centre, regular vet), **Asia Paws** (acupuncture), **Petcare** (house call and clinic, Apr–May 2025).
