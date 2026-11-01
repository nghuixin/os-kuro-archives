# Do the animal communicator's health impressions match Kuro's records?

From Jul 2024 to Sep 2026 an animal communicator gave Kuro six communication sessions and 43 remote reiki sessions ([`communicator_notes.csv`](../data/processed/communicator_notes.csv)). This page checks her 56 health impressions against what his vets, carers and lab tests documented. The item-level results are in [`communicator_concordance.csv`](../data/processed/communicator_concordance.csv).

This is a check of agreement with the written record, not a test of whether animal communication works. Matches can come from what she was told, from guesses that fit any old dog, or from chance, and the method below tries to separate those.

## Method

**Deductive qualitative content analysis** with a fixed coding rubric, applied independently by two coders (AI models), with disagreements settled by a third review.

- **Truth source:** vet assessments, symptoms and care notes (`health_events.csv`), visits, lab results and the [health summary](health-summary.md). Anything reported by the communicator was excluded as evidence.
- **Unit:** each of the 56 impressions. Reiki rows were scored as a whole: the stated impression first, otherwise whether the list of body areas included his active problems at the time.

| Code | Values |
|---|---|
| **Match** | **3** specific match: same concrete problem documented within ±60 days · **2** partial: right region or system, but vague, outside the window (same year), or only part matches · **1** weak: plausible for an old dog, nothing documented near the time · **0** none or contradicted |
| **Specificity** | **G** generic: true of most elderly dogs (joints, hips, heart, kidney, eyes, teeth) · **S** specific: a concrete claim (e.g. lower-abdominal pain, throat phlegm, left rib cage) |
| **Prior knowledge** | **K** she had been told about the issue before the session · **P** related context only · **U** no sign she was told |

Area lists that named an active problem among many areas were capped at 2.

**What she was told, and when.** The owner asked for the reiki to focus on his spine and hips (30 Dec 2024). She was also told about the abdominal tumour and his rising white cell count (10 Jan 2025), his coughing (15 Jan 2025), and his limping and the vet's diagnosis of nerve pain and arthritis (28–30 Apr 2025). She met him in person in Nov 2025.

## Reliability

| Code | Agreement between coders | Cohen's kappa |
|---|---|---|
| Match (0–3) | 48 / 56 exact, 56 / 56 within one point | 0.82 weighted (quadratic), 0.78 (linear) |
| Specificity | 54 / 56 | 0.93 |
| Prior knowledge | 37 / 56 | 0.50 |

Match and specificity were coded reliably. Prior knowledge was only moderately reliable, because the coders read the chat context differently. It was settled item by item against the dated disclosures above.

## Results

**Overall:** match 3 (×13), 2 (×36), 1 (×7), 0 (×0); mean 2.11 out of 3. Nothing was contradicted outright, but most matches were partial.

| Group | Items | Mean match | Score 3 |
|---|---|---|---|
| Generic claims | 27 | 2.00 | 2 |
| Specific claims | 29 | 2.21 | 11 |
| She had been told (K) | 25 | 2.16 | 5 |
| Related context (P) | 17 | 2.29 | 7 |
| Not told (U) | 14 | 1.79 | 1 |
| **Specific and not told** | **11** | **1.82** | **1** |

**The strongest matches.** Each of these was specific, but she had at least partial context for all except the thyroid:

- **Jul 2024:** lower-abdominal pain "up to 8/10", days after the splenic bleed, transfusion and pancreatitis.
- **Jul 2024:** bladder control on long trips, before he started drinking urine and wearing diapers (Jul–Aug 2024).
- **Jan 2025:** discomfort "in his side and abdomen" when walking, the week the vet said the tumour had grown 2 cm.
- **Jan–Mar 2025:** congested breathing and throat phlegm, while he was coughing (she had been told about the coughing).
- **Aug 2025:** ear scratching, a week before an ear treatment and two months before head-shaking was reported.
- **Aug 2025:** the thyroid listed as a healing area, ten days after the vet suggested a thyroid (T4) test for a slow heart rate. Nothing shows she had been told. It is the only full match among specific claims made without any context.
- **Oct 2025:** an "asthma"-like panting sound, the day before the owner said he panted more at night.
- **Jul 2026:** "left side of body, rib cage area", in a dog with a large splenic mass, confirmed at post mortem.

**The weakest.** Throat phlegm in Jul 2024 (no cough recorded until Jan 2025), stiff shoulders and bleeding gums in Jan 2025 (not documented; the owner had not seen bleeding), and bad breath in Aug 2026 (no record near the date).

## Interpretation

- **Concordance is high but shallow.** Most items (36 of 56) matched only partially. Generic claims about joints, hips, heart, kidney and teeth will fit almost any 14–16-year-old dog. Long reiki area lists (often six to eight areas) nearly always include one active problem.
- **Prior disclosure explains much of the agreement.** Where she had been told or given context, the mean match was 2.16–2.29. Where she had not, it was 1.79. For specific claims made without being told, it was 1.82, with one full match (the thyroid) out of 11.
- **A few hits are notable,** such as the thyroid timing and the left rib cage, but one or two matches among dozens of claims are within what chance and the base rate of illness in an old dog would produce. The data cannot distinguish insight from chance.
- **Practical value.** Her sessions often prompted the owner to watch something, like breathing or ear scratching. As a prompt to observe and then ask the vet, that is harmless. As a substitute for examination, the record does not support relying on it.

## Limitations

- The truth source is incomplete. Unrecorded problems make some claims look unsupported; recorded problems she was told about make others look like matches.
- The coders were AI models working from the same records, and the third review was by the archive's author.
- No control set was scored, such as the same rubric applied to random body areas, so the chance level is estimated, not measured.
- The ±60-day window and the cap for area lists are judgement calls.
