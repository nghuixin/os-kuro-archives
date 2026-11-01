# Dog Aging Project surveys: what they ask and how Kuro was answered

The [Dog Aging Project](https://dogagingproject.org) (DAP) is a long-term study of ageing in tens of thousands of US companion dogs. It publishes its owner survey instruments and codebooks in its public GitHub repository, [`dogagingproject/dataRelease`](https://github.com/dogagingproject/dataRelease).

Kuro was never enrolled in the DAP. After his death his owner answered five DAP survey sections for him, so that his last year can be compared with DAP dogs. The answers are in [`data/dog_aging_project/dap_surveys_kuro.csv`](../../data/dog_aging_project/dap_surveys_kuro.csv), and this page describes the surveys behind them:

| Survey | When DAP asks it | Kuro's answers cover |
|---|---|---|
| [End of Life Survey (EOLS)](#end-of-life-survey-eols) | Once, after a dog dies | His final two weeks and death (18 Oct 2026) |
| [Cognition (CSLB)](#cognition-canine-social-and-learned-behavior-survey-cslb) | Every year | Sep–Oct 2026, compared with Apr 2026 |
| [Annual Follow-Up: Age-Related Changes](#annual-follow-up-age-related-changes) | Every year | His last year (Oct 2025 – Oct 2026) |
| [Annual Follow-Up: Diet](#annual-follow-up-diet) | At baseline and every year | His diet in his final months |
| [Annual Follow-Up: Medications and Preventives](#annual-follow-up-medications-and-preventives) | Every year | His last year |

Item content is summarised and DAP's variable names are given so the original wording can be found; the forms are not reproduced. The repository has no stated licence, so the PDFs and the DAP codebook are kept as local copies only (`docs/dog-aging-project/forms/`, gitignored).

## How Kuro's answers are recorded

[`dap_surveys_kuro.csv`](../../data/dog_aging_project/dap_surveys_kuro.csv) is laid out like a DAP response: **one row per DAP variable**, using DAP's variable names and answer codes as defined in the [DAP 2025 codebook](https://github.com/dogagingproject/dataRelease/tree/master/Codebooks). Tick-box items are `True`/`False`, as in DAP's data. Questions the survey's skip logic would not have shown are left out, as DAP would leave them blank.

| Column | Meaning |
|---|---|
| `variable` | DAP variable name, e.g. `eol_recent_qol` |
| `value` | The answer, as a DAP code (or text for free-text items) |
| `answered_by` | `owner` for every row: each answer was given or confirmed by his owner (Oct–Nov 2026) |
| `evidence` | A check of the answer against what was written at the time (chats, vet records, labs). It starts with a verdict (`supports`, `contradicts`, `mixed`, `not mentioned`, `not checkable`), then gives dated, sourced quotes, and notes where the owner revised an answer after seeing the evidence |

**How it was built.** The owner answered the End of Life and cognition surveys from memory. Every answer was then checked against the records: 101 of the owner's 152 original answers were supported, 2 were contradicted (whether anyone was present at his death) and 20 were mixed; the owner revised four answers after seeing the evidence. For the Age-Related Changes, Diet and Medications sections, answers were first prefilled from the records and then confirmed or corrected by the owner. All codes were validated against the DAP codebook. Two variables are not in DAP's public release: `eol_notes_description` (free text, withheld by DAP) and `dt_overweight_hles` (on the form but not released).

## End of Life Survey (EOLS)

**Source:** [`Survey_Instruments/EOLS/DAP_EOLS.pdf`](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/EOLS/DAP_EOLS.pdf) (version 1.0, 23 pages). Owner-completed after a dog's death; most questions allow "I'm not sure" or "unknown".

**Validation:** McNulty et al. (2023) developed and validated the EOLS. Test–retest agreement was substantial for cause of death (κ = 0.73), moderate for quality of life in the last two weeks (κ = 0.49), and fair to substantial for reason for euthanasia. Pearson et al. (2024) analysed 2,570 responses and found euthanasia was associated with cause of death but not with age.

| Section | What it asks | Answer format | Variables |
|---|---|---|---|
| 1. New diagnoses | Conditions diagnosed since the last health survey, in 21 categories (cancer, cardiac, liver or pancreas, kidney, orthopaedic, neurological, blood or lymphatic, immune-mediated, dental, and so on), with month, year and a description for each | Checkboxes, then month/year and free text | `eol_new_condition_*` |
| 2. Date of death | Whether the exact date is known, and the date | Yes/no; date | `eol_exact_death_date_known`, `eol_death_date` |
| 3. Old-age characteristics, last 2 weeks | 20 options: poor vision, poor hearing, weight loss, poor mobility from **weakness** or from **pain or stiffness**, other pain, poor cleanliness, disorientation, changed interaction, sleep disturbance, house soiling, anxiety, reduced eating and drinking, inactivity, repetitive pacing, memory loss, not recognising people, sundowning, other, none | Select all | `eol_recent_aging_char_*` |
| 4. Medical signs, last 2 weeks | Lethargy, vomiting, diarrhoea, poor appetite, weight loss, coughing, sneezing, difficulty breathing, bleeding or bruising easily, drinking a lot or very little, urinating a lot, incontinence, chronic wounds, seizures, swollen abdomen, other, none | Select all | `eol_recent_symptom_*` |
| 5. Quality of life | QoL in the last two weeks; when it first began to decline; the main contributor | 7-point scale from "always bad days" to "always good days"; timing; single choice | `eol_recent_qol`, `eol_qol_declined`, `eol_qol_declined_reason` |
| 6. Veterinary care, last 2 weeks | Seen or discussed with a vet; hospital stay; sedation, anaesthesia or surgery; owner's understanding of prognosis | Yes/no/not sure; 5-point prognosis scale, or not discussed | `eol_recent_vet_*`, `eol_recent_sedation`, `eol_understand_prognosis` |
| 7. Place and witnesses | Where the dog died, and who was present | Single choice; select all | `eol_death_location`, `eol_death_witness*` |
| 8. Manner of death | Whether euthanised, by whom, and why | Yes/no; single choice; select all | `eol_euthan*` |
| 9. Cause of death | Primary and secondary cause: old age; illness; trauma; toxin; sedation or surgery; behaviour; **sudden death with no apparent cause**; personal factors; other | Single choice each | `eol_cause_of_death_primary`, `eol_cause_of_death_secondary` |
| 10. Cause details | For illness: type, cancer body system and name if known, when the owner first became aware, whether it was being treated (incl. palliative). Similar follow-ups for old age, trauma and toxin | Single choice; select all; free text | `eol_illness_*`, `eol_old_age_*`, `eol_trauma`, `eol_toxin` |
| 11. Narrative | Anything else about the circumstances of the death | Free text | `eol_notes_description` |

**Kuro's answers:**

| Item | Answer |
|---|---|
| New diagnoses in his last year | Trauma (left hind limp, Dec 2025), eye (cataract; cyst above the eye), liver or pancreas (pancreatitis flare, Nov 2025), orthopaedic (sarcopenia, Jul 2026), blood (anaemia again, Mar 2026) |
| Old-age characteristics, last 2 weeks | Poor vision, poor mobility from weakness and from pain, other pain, poor cleanliness |
| Medical signs, last 2 weeks | Difficulty breathing, incontinence |
| Quality of life, last 2 weeks | 6, almost entirely good days; decline began one or more months before death, mainly from health problems |
| Vet care, last 2 weeks | Seen by a vet; no hospital stay or sedation; understood he would likely live beyond a month |
| Place and witnesses | At home; **no one present** (no one saw him go into the pond) |
| Euthanised | No |
| Cause of death | Primary: illness (cancer of the spleen, name not known, known about for two or more years, treated palliatively). Secondary: sudden death with no apparent cause |

The post-mortem findings behind the cause of death are in the [health summary](../case-study/health-summary.md#post-mortem-examination-19-oct-2026).

## Cognition: Canine Social and Learned Behavior survey (CSLB)

**Source:** [`Survey_Instruments/CSLB/DAP_CSLB.pdf`](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/CSLB/DAP_CSLB.pdf) (2020.11.12). The survey is the **CCDR** (Salvin et al., 2011), minimally modified and renamed so it does not suggest dementia to owners. It is repeated every year.

| Part | Items (variable names) | Response scale |
|---|---|---|
| How often, now | Pacing or aimless wandering (`cslb_pace`); staring blankly at walls or floor (`cslb_stare`); getting stuck behind objects (`cslb_stuck`); not recognising familiar people or pets (`cslb_recognize`); walking into walls or doors (`cslb_walk_walls`); avoiding being petted (`cslb_avoid`) | 1 never · 2 once a month · 3 once a week · 4 once a day · 5 more than once a day |
| How often, now | Difficulty finding food dropped on the floor (`cslb_find_food`) | 1 never · 2 1–30% of the time · 3 31–60% · 4 61–99% · 5 always |
| Compared with 6 months ago | Pacing (`cslb_pace_6mo`); staring (`cslb_stare_6mo`); house soiling (`cslb_defecate_6mo`); difficulty finding food (`cslb_food_6mo`); not recognising people or pets (`cslb_recognize_6mo`) | 1 much less · 3 the same · 5 much more |
| Compared with 6 months ago | Time spent active (`cslb_active_6mo`) | Reversed: 1 much more · 3 the same · 5 much less |

**Score:** the sum of all 13 items, with the 6-month food item counted twice and the 6-month recognition item counted three times. The range is 16–80, and **≥50 indicates canine cognitive dysfunction**, matching the CCDR.

**Kuro's score: 36**, below the borderline range (40–49). He never paced, stared, got stuck or failed to recognise people; he sometimes had trouble finding dropped food (likely his cataracts), and house soiling had increased slightly over six months. No vet ever assessed him for cognitive dysfunction.

## Annual Follow-Up: Age-Related Changes

**Source:** [`Survey_Instruments/AFUS/DAP_AFUS_12_AgeRelatedChanges.pdf`](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/AFUS/DAP_AFUS_12_AgeRelatedChanges.pdf). The same list of old-age characteristics as the EOLS, but over the past year, and only for changes the owner attributes to ageing rather than to a specific condition (`afus_ac_aging_char_*`). It also asks for quality of life over the year on the same 7-point scale (`afus_ac_recent_qol`), whether it declined (`afus_ac_qol_declined_yn`) and what contributed most (`afus_ac_qol_declined_reason`). The weight question comes from the Dog Demographics section (`afus_dd_dog_weight_lbs`).

**Kuro's answers:** poor vision, weight loss, poor mobility from weakness and from pain, other pain, poor cleanliness and house soiling; quality of life 5 (more good days than bad), declining over the year, mainly from physical changes of old age; last weight 43.4 lb (19.7 kg, 14 Sep 2026).

## Annual Follow-Up: Diet

**Source:** [`Survey_Instruments/AFUS/DAP_AFUS_06_Diet_Comprehensive.pdf`](https://github.com/dogagingproject/dataRelease/tree/master/Survey_Instruments/AFUS) ("Baseline and Follow-up: Comprehensive Diet", 2023.05.02, 30 pages). It uses the same `dt_` variables as the baseline survey. The DAP public data release includes these variables for the baseline survey only, so Kuro's answers follow the baseline codebook.

| Part | What it asks | Variables |
|---|---|---|
| Feeding pattern | How consistent the diet is; how many people feed the dog; scheduled or free feeding; meals a day and at what times; appetite and how fast meals are finished, and whether either changed in six months | `dt_pattern_*`, `dt_feeding_pattern` |
| Weight | Whether weight stayed the same over the past year and how it changed; whether the dog was ever considered under- or overweight | `dt_weight_change*`, `dt_underweight_hles`, `dt_overweight_hles` |
| Primary diet | Commercial food or home-prepared; for commercial food, brand, product and form (asked for up to two foods); for home-prepared, a description | `dt_primary_diet_type`, `dt_comm1_*`, `dt_comm2_*`, `dt_homeprep_description` |
| Additions | Foods added to the main diet | `dt_add_*`, `dt_addition_*` |
| Supplements | 23 types (joint, skin, vitamins, enzymes, probiotics, fibre, omega-3, liver, immune and others), with how often each is given | `dt_supplements_type_*`, `dt_supplements_*_freq` |
| Treats | 7 types (crunchy, chewy, jerky or rawhide, dental, low-calorie, freeze-dried, other), with how often and how many days a week | `dt_treats_type_*`, `dt_treats_*_freq`, `dt_treats_*_daysweek` |
| Notes | Anything else about the dog's diet | `dt_additional_info_description` |

**Kuro's answers:** a home-cooked diet (lean meat, rice and vegetables, kept low in fat), cooked by his mother and fed by the helper alone, four meals a day at 7 am, 11 am, 3 pm and 7 pm. Voracious appetite; ate very fast. Lost weight over the year; had been both overweight (2021) and thin (2026) at different times. Daily vitamins, enzymes, probiotic and other supplements, and a liver tonic twice a day. Treats: low-fat jerky (Honu Paws) and air-dried trout, three days a week.

## Annual Follow-Up: Medications and Preventives

**Source:** [`Survey_Instruments/AFUS/DAP_AFUS_07_Meds.pdf`](https://github.com/dogagingproject/dataRelease/tree/master/Survey_Instruments/AFUS) ("Follow-up: Medications and Preventives", 2023.05.02, 8 pages). Despite the name, it asks about routine and preventive care rather than prescription drugs.

| Part | What it asks | Variables |
|---|---|---|
| Dental care | How often the teeth are examined and brushed, and dental treats, dental food or breath fresheners given; dental procedures, cleanings and extractions since the last survey | `afus_mp_dental_*` |
| Grooming | Professional grooming and home washing, and how often | `afus_mp_professional_grooming*`, `afus_mp_home_grooming*` |
| Flea and tick | Whether used, how often, form (topical, collar, oral, shampoo and others) and brand | `afus_mp_flea_and_tick_*`, `afus_mp_flea_*_brand` |
| Heartworm | Whether used, how often, form and brand | `afus_mp_heartworm_*` |
| Vaccines | How often each is received: rabies, distemper combo, leptospirosis, kennel cough, canine influenza, Lyme | `afus_mp_vaccine_*` |
| Non-prescription products | 14 types (antibiotic ointment, antihistamine, anti-inflammatory, ear cleaner, eye lubricant, joint supplement, stomach remedy, omega-3, probiotic, vitamin and others) | `afus_mp_recent_non_prescription_meds_*` |

**Kuro's answers:** teeth checked and brushed only occasionally; a professional dental cleaning in 2026 (also one in 2024), no extractions. Groomed professionally about monthly; washed at home a few times a year. One topical flea and heartworm treatment (Advocate) in Sep 2026. Vaccines last given around 2022–2023; which ones is not known. Non-prescription products: ear cleaner, eye lubricant, joint supplement, stomach remedy, omega-3, probiotic, vitamin and others (liver and kidney supplements, Chinese herbal formulas).

## Body condition

DAP's owner surveys **do not ask for a body condition score**. The baseline survey asks for a weight range and exact weight in pounds (`dd_weight_range`, `dd_weight_lbs`; [HLES section 2](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/HLES/DAP_HLES_02_DogDemographics.pdf)), and the annual follow-up updates the exact weight (`afus_dd_dog_weight_lbs`). Body condition scores in DAP research come from **veterinary records**: one study extracted them for 200 dogs alongside 13,890 questionnaires. Owners are known to misjudge their dog's condition, so for home monitoring use the WSAVA 9-point Body Condition Score and Muscle Condition Score. Kuro was never scored; the vet noted "sarcopenia (muscle atrophy)" in Jul 2026.

## References

- McNulty KE, Creevy KE, et al. Development and validation of a novel instrument to capture companion dog mortality data: the Dog Aging Project End of Life Survey. *J Am Vet Med Assoc.* 2023. Preprint: [bioRxiv 2023.04.01.535178](https://www.biorxiv.org/content/10.1101/2023.04.01.535178).
- Pearson EB, Hoffman JM, Melvin RL, McNulty KE, Creevy KE, Ruple A. Analysis of 2,570 responses to Dog Aging Project End of Life Survey demonstrates that euthanasia is associated with cause of death but not age. *J Am Vet Med Assoc.* 2024;262(2). doi:10.2460/javma.23.07.0366 ([PMC10996864](https://pmc.ncbi.nlm.nih.gov/articles/PMC10996864)).
- Salvin HE, McGreevy PD, Sachdev PS, Valenzuela MJ. The canine cognitive dysfunction rating scale (CCDR): a data-driven and ecologically relevant assessment tool. *Vet J.* 2011;188:331–336.
- Creevy KE, Akey JM, Kaeberlein M, Promislow DEL; Dog Aging Project Consortium. An open science study of ageing in companion dogs. *Nature.* 2022;602:51–57.
- Dog Aging Project survey instruments and codebooks, [github.com/dogagingproject/dataRelease](https://github.com/dogagingproject/dataRelease) (accessed Nov 2026).
