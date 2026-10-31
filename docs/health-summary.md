# Kuro — health summary, Oct 2024 to Oct 2026

Kuro was a male dog, 15 years old in December 2025, cared for by FurKids (regular vet) and Asia Paws (acupuncture). This summary is assembled from WhatsApp messages, four vet invoices and clinic images. It records what vets and carers said; it is not a diagnosis. Data: [`data/processed/`](../data/processed/).

## Recurring themes

| Theme | Period | What the records show |
|---|---|---|
| Abdominal (spleen) mass and anemia | 2024-11 → 2026-10 | Red cell count 19% in Nov 2024, down from 30% a month earlier; vet suspected an "immune-mediated issue due to the spleen mass". Mass measured 197.5 × 179.7 mm on x-ray (Dec 2025). "Abit anemic" in Mar and May 2026; darbepoetin injections and iron tablets from Apr 2026. Prednisolone throughout. |
| Hind leg, hip and back pain | 2024-10 → 2026-10 | Mentioned at almost every acupuncture session (35+ times). Progressed to weakness, trouble getting up, and "sarcopenia (muscle atrophy)" by Jul 2026. |
| Incontinence | 2024-10 → 2026-07 | Diapers from Nov 2024; peeing on himself and urine burn concerns in Jun–Jul 2026. |
| Liver and kidney values | 2025-07 → 2026-07 | ALT high (Jul 2025); liver "abit high" (Apr 2026); kidney off with dehydration (May 2026); both "abit high but manageable" (Jul 2026). SDMA kidney test ordered in Oct 2024, Apr 2026 and Aug 2026. Ursofalk (Oct 2025) and Samylin. |
| Weight loss | 2024-10 → 2026-09 | 21.3 → 20.5 → 20.6 → 19.9 → 19.5 → 19.4 → 19.7 kg. Smaller, more frequent meals with probiotics from May 2026. |
| Wounds and infections | 2025-04, 2026-09 | Hind leg abrasion (Apr–May 2025, cone and cream); nibbled wound (Sep 2026, Baytril). Infection suspected from bloodwork in Apr 2026 (Baytril). |
| Lumps | 2025-12 → 2026-07 | Bump near the eye, "small cyst" (Dec 2025); fluid in the right cheek (Mar 2026); hind leg and armpit growths, "may be a lipoma", non-inflammatory (Jul 2026). |
| Dental and appetite | 2025-01 → 2025-10 | Plaque, gum discomfort, mouth spray; refused pumpkin and sweet potato (Aug 2025). |
| Slow heart rate | 2025-08 → 2026-06 | T4 thyroid test suggested (Aug 2025); "heart is okay just slow" (Jun 2026). Heart and lungs otherwise reported good. |

## Ongoing medications and supplements (from invoices)

Prednisolone 5 mg, Protexin Pro-Enzorb, Supra Mineral at every invoiced visit; darbepoetin and iron tablets from Apr 2026; Aminavast from Aug 2026; Baytril in Apr and Sep 2026; Advocate in Sep 2026.

From medicine labels (`prescriptions.csv`): Maltofer iron and prednisolone 0.5 tablet from Mar 2025; during the Apr–May 2025 leg wound, Galliprant (anti-inflammatory, 10 days), an antibiotic (5 days), Neuroforte (nerve supplement), plus B12 and antibiotic injections; homeopathic Arnica and Hypericum for pain (May and Sep 2025) and Strophanthus for heart support (Nov 2025) from the acupuncture clinic; prednisolone 0.5 tablet every other day in Feb 2026.

## Lab panels, 2026 (FurKids in-house, IDEXX)

From `data/processed/lab_panels.csv`. H/L = outside the printed reference interval.

| Analyte | Ref | 2026-02-04 | 2026-07-01 | 2026-08-10 | 2026-09-14 |
|---|---|---|---|---|---|
| UREA (mmol/L) | 2.5–9.6 | 11.2 H | 11.5 H | 17.2 H | 13.0 H |
| CREA (µmol/L) | 44–159 | 78 | 97 | 80 | 114 |
| ALT (U/L) | 10–125 | – | 94 | 130 H | 112 |
| ALKP (U/L) | 23–212 | – | 217 H | 211 | 192 |
| HCT (%) | 37.3–61.7 | – | 33.9 L | 32.8 L | 34.9 L |
| HGB (g/dL) | 13.1–20.5 | – | 11.8 L | 12.0 L | 12.5 L |
| RETIC (K/µL) | 10–110 | – | 60.3 | 70.4 | 38.3 |
| WBC (×10⁹/L) | 5.05–16.76 | – | 11.17 | 13.39 | 16.00 |
| MONO (×10⁹/L) | 0.16–1.12 | – | 0.98 | 1.26 H | 1.29 H |

SNAP 4Dx Plus (Anaplasma, Ehrlichia, heartworm, Lyme): negative in Jun 2024 and Sep 2026. The analyzer printed "anemia without reticulocytosis – likely non-regenerative anemia" in Aug and Sep 2026.

## Gaps

- No SDMA value in any record, though it was ordered in Oct 2024, Apr 2026 and Aug 2026. Panels before Jul 2026 (beyond the partial Feb 2026 one) need to be requested from FurKids.
- No invoices before Oct 2025.
- Remaining medical photos are mostly medicine labels and acupuncture appointment screenshots; dosing from the Feb 2026 labels is in `health_events.csv`.
