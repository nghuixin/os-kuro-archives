# Dog Aging Project surveys, scored retrospectively for Kuro

Kuro's records scored against three Dog Aging Project (DAP) owner surveys, as if they had been completed for him. The surveys and their items are described in [`docs/instruments/dog-aging-project.md`](../../docs/instruments/dog-aging-project.md).

**Rule: nothing is inferred.** An item is answered only when a dated record directly supports the answer. If there is no record, the item is `missing`. Absence of a record is never taken to mean "no".

| File | Survey | Time window | Items | Answered | Missing | Other |
|---|---|---|---|---|---|---|
| `eols_kuro.csv` | End of Life Survey | final two weeks (4–18 Oct 2026); death details | 59 | 14 | 40 | 2 conflicting, 3 not applicable |
| `cslb_kuro.csv` | Canine Social and Learned Behavior (DAP's CCDR) | current and vs 6 months ago | 14 | 0 | 14 | — |
| `afus_age_related_changes_kuro.csv` | Annual Follow-Up: Age-Related Changes, plus weight and body condition | final year (18 Oct 2025 – 18 Oct 2026) | 25 | 9 | 16 | — |

## Columns

`survey`, `section`, `variable` (DAP's variable name), `question_summary`, `response_code` and `response_label` (DAP's coding), `status`, `evidence_date`, `evidence` (quoted or summarised from the records), `source` (the processed file or chat the evidence comes from).

`status` is one of:

- **answered:** a dated record directly supports the answer.
- **missing:** no record, or the item needs a judgement the owner never recorded, such as quality of life or the choice of cause-of-death category.
- **conflicting:** records point both ways. The evidence column shows both.
- **not applicable:** the survey's skip logic excludes it, e.g. euthanasia questions for a dog who was not euthanised.

## What could be answered

- **End of Life Survey:**
  - Date of death and place of death (home); not euthanised.
  - Present: yes. He was about 5 feet from his dad when he slipped into the pond "without noise". No one saw him go in, and the helper found him at about 6.48 pm, almost 2.5 hours later.
  - Seen by a vet in the final two weeks (Asia Paws, 8 Oct).
  - Final-two-week signs: poor vision, hind-limb weakness, back pain, looking dirty.
- **Age-Related Changes (final year):**
  - Poor vision, weight loss, poor mobility from weakness and from pain, other pain, poor cleanliness, house soiling.
  - Last recorded weight: 19.7 kg (43.4 lb).
  - Several of these may come from his diagnosed conditions rather than old age; the evidence column flags this.

## What is missing

- **Quality of life:** no 7-point quality-of-life score, for the final two weeks or the final year, and no record of when it began to decline.
- **Cause of death:** the owner's choice of category. On record are "Drowned in the fish pond" and the vet's "sudden death... with significant underlying splenic disease", with the mechanism undetermined. Everything that depends on the category is also missing.
- **Cognition:** all 13 CSLB items, so no cognition score can be calculated.
- **Body condition:** no body condition or muscle condition score. The vet noted "sarcopenia (muscle atrophy)" in Jul 2026.
- **Final-two-week medical signs:** most are unrecorded. Difficulty breathing and "no symptoms" are marked conflicting.

These gaps are themselves a finding: the records describe his medical care in detail, but not the quality-of-life and cognitive measures that ageing studies collect.
