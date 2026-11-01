# Dog Aging Project instruments: end of life, cognition and body condition

The [Dog Aging Project](https://dogagingproject.org) (DAP) is a long-term study of ageing in tens of thousands of US companion dogs. It publishes its owner survey instruments in its public GitHub repository, [`dogagingproject/dataRelease`](https://github.com/dogagingproject/dataRelease/tree/master/Survey_Instruments). This page summarises the three parts relevant to a senior dog's last years: the **End of Life Survey**, the **cognition survey** (DAP's version of the CCDR) and how DAP records **body condition**. Item content is summarised and DAP's variable names are given so the original wording can be found; the forms themselves are not reproduced. The repository has no stated licence, so the PDFs are kept as local copies only (`docs/instruments/forms/dap/`, gitignored).

## End of Life Survey (EOLS)

**Source:** [`Survey_Instruments/EOLS/DAP_EOLS.pdf`](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/EOLS/DAP_EOLS.pdf) (version 1.0, 23 pages). Owner-completed after a dog's death; most questions allow "I'm not sure" or "unknown".

**Validation:** McNulty et al. (2023) developed and validated the EOLS. Test–retest agreement was substantial for cause of death (κ = 0.73), moderate for quality of life in the last two weeks (κ = 0.49), and fair to substantial for reason for euthanasia. Pearson et al. (2024) analysed 2,570 responses and found euthanasia was associated with cause of death but not with age.

| Section | What it asks | Answer format | Variables |
|---|---|---|---|
| 1. New diagnoses | Conditions diagnosed since the last health survey, in 21 categories (cancer, cardiac, liver or pancreas, kidney, orthopaedic, neurological, blood or lymphatic, immune-mediated, dental, and so on), with month, year and a description for each | Checkboxes, then month/year and free text | `eol_new_condition_*` |
| 2. Date of death | Whether the exact date is known, and the date | Yes/no; date | `eol_exact_death_date_known`, `eol_death_date` |
| 3. Old-age characteristics, last 2 weeks | 20 options: poor vision, poor hearing, weight loss, poor mobility from **weakness** or from **pain or stiffness**, other pain, poor cleanliness, disorientation, changed interaction, sleep disturbance, house soiling, anxiety, reduced eating and drinking, inactivity, repetitive pacing, memory loss, not recognising people, sundowning, other, none | Select all | `eol_recent_aging_char_*` |
| 4. Medical signs, last 2 weeks | Lethargy, vomiting, diarrhoea, poor appetite, weight loss, coughing, sneezing, difficulty breathing, bleeding or bruising easily, drinking a lot or very little, urinating a lot, incontinence, chronic wounds, seizures, swollen abdomen, other, none | Select all | `eol_recent_symptom_*` |
| 5. Quality of life | QoL in the last two weeks | 7-point scale, from 1 "always bad days" to 7 "always good days" | `eol_recent_qol` |
| | When QoL first began to decline | No decline; hours to days; weeks; months; one year; two or more years before death | `eol_qol_declined` |
| | Main contributor to the decline | Physical changes of old age; behavioural changes of old age; health problems; other | `eol_qol_declined_reason` |
| 6. Veterinary care, last 2 weeks | Seen or discussed with a vet; hospital stay and length; sedation, anaesthesia or surgery; owner's understanding of prognosis | Yes/no/not sure; prognosis on a 5-point scale from "almost certainly will die within the next month" to "almost certainly will live beyond a month", or not discussed | `eol_recent_vet_*`, `eol_recent_sedation`, `eol_understand_prognosis` |
| 7. Place and witnesses | Where the dog died (home; friend's home; away from home with a carer; **away from home while unsupervised**; vet clinic; boarding or grooming), and who was present | Single choice; select all | `eol_death_location`, `eol_death_witness*` |
| 8. Manner of death | Whether euthanised and by whom; the main reason and any additional reasons (poor QoL, pain or suffering, poor prognosis, unmanageable medical or behaviour problems, risk of harm, housing, cost, other) | Yes/no; single choice; select all | `eol_euthan*`, `eol_euthan_main_reason`, `eol_euthon_add_reason_*` |
| 9. Cause of death | Primary and secondary cause: old age; illness or disease; **trauma or injury**; toxin; related to sedation, anaesthesia or surgery; behaviour problems; **sudden death with no apparent cause**; personal factors; other | Single choice each | `eol_cause_of_death_primary`, `eol_cause_of_death_secondary` |
| 10. Cause details | **Old age:** which characteristic was most significant. **Illness:** cancer (with body system, e.g. spleen, and name if known), infection (type and system) or other illness (system and diagnosis); when the owner first became aware of it; whether it was being treated, including treatment for comfort (palliative). **Trauma:** type, including fall from height and head trauma. **Toxin:** type | Single choice; select all; free text | `eol_old_age_*`, `eol_illness_*`, `eol_trauma`, `eol_toxin` |
| 11. Narrative | Anything else about the circumstances of the death; whether new vet records can be uploaded | Free text | `eol_notes_description`, `eol_add_vemr` |

**Applied to Kuro (from his records).** Most items can be answered from the archive:

| Item | Answer from the records |
|---|---|
| Location | Home property (garden fish pond) |
| Present at death | Yes. He was 5 feet away from his dad when he slipped into the pond "without noise"; no one saw him go in, and the helper found him at about 6.48 pm, almost 2.5 hours later |
| Euthanised | No |
| Primary cause | Unclear. Trauma (drowning) or sudden death, with illness (splenic tumour with partial rupture) as the main contributor; the post mortem could not determine the mechanism |
| Cancer system | Spleen |
| Treatment at death | Yes, comfort (palliative) care |
| First aware of the illness | Two or more years before death (Jun–Jul 2024) |
| Signs in the last 2 weeks | Not recorded systematically. The family later reported "difficulty in breathing"; a "nothing" answer to the clinic's symptoms question is in the chat |
| Old-age characteristics | Poor mobility from weakness, poor vision (cataracts), weight loss (19.4–19.7 kg) |

Quality of life in the last two weeks was never scored. That gap is what this survey is designed to fill.

## Cognition: Canine Social and Learned Behavior survey (CSLB)

**Source:** [`Survey_Instruments/CSLB/DAP_CSLB.pdf`](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/CSLB/DAP_CSLB.pdf) (2020.11.12). The survey is the **CCDR** (Salvin et al., 2011), minimally modified and renamed so it does not suggest dementia to owners. It is repeated every year.

| Part | Items (variable names) | Response scale |
|---|---|---|
| How often, now | Pacing or aimless wandering (`cslb_pace`); staring blankly at walls or floor (`cslb_stare`); getting stuck behind objects (`cslb_stuck`); not recognising familiar people or pets (`cslb_recognize`); walking into walls or doors (`cslb_walk_walls`); avoiding being petted (`cslb_avoid`) | 1 never · 2 once a month · 3 once a week · 4 once a day · 5 more than once a day |
| How often, now | Difficulty finding food dropped on the floor (`cslb_find_food`) | 1 never · 2 1–30% of the time · 3 31–60% · 4 61–99% · 5 always |
| Compared with 6 months ago | Pacing (`cslb_pace_6mo`); staring (`cslb_stare_6mo`); house soiling (`cslb_defecate_6mo`); difficulty finding food (`cslb_food_6mo`); not recognising people or pets (`cslb_recognize_6mo`) | 1 much less · 3 the same · 5 much more |
| Compared with 6 months ago | Time spent active (`cslb_active_6mo`) | Reversed: 1 much more · 3 the same · 5 much less |
| Optional | Any other changes in thinking (`cslb_other_changes`) | Free text |

**Score:** the sum of all 13 items, with the 6-month food item counted twice and the 6-month recognition item counted three times. The range is 16–80, and **≥50 indicates canine cognitive dysfunction**, matching the CCDR.

**Kuro:** never scored. The records note cataracts and poor vision but no recorded pacing, staring, getting stuck or failure to recognise people.

## Age-Related Changes (Annual Follow-Up Survey)

**Source:** [`Survey_Instruments/AFUS/DAP_AFUS_12_AgeRelatedChanges.pdf`](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/AFUS/DAP_AFUS_12_AgeRelatedChanges.pdf). This asks the same list of old-age characteristics as the EOLS, but over the past year (`afus_ac_aging_char_*`). It also asks for yearly quality of life on the same 7-point scale (`afus_ac_recent_qol`), whether QoL declined, and what contributed most. That makes it easy to compare the last year of life with the final two weeks.

## Body condition

DAP's owner surveys **do not ask for a body condition score**. The baseline survey asks for a weight range and exact weight in pounds (`dd_weight_range`, `dd_weight_lbs`; [HLES section 2](https://github.com/dogagingproject/dataRelease/blob/master/Survey_Instruments/HLES/DAP_HLES_02_DogDemographics.pdf)), and the annual follow-up updates the exact weight (`afus_dd_dog_weight_lbs`). Body condition scores in DAP research come from **veterinary records**: one study extracted them for 200 dogs alongside 13,890 questionnaires. Owners are known to misjudge their dog's condition, so for home monitoring use the WSAVA 9-point Body Condition Score and Muscle Condition Score (see [the instruments page](README.md)).

## References

- McNulty KE, Creevy KE, et al. Development and validation of a novel instrument to capture companion dog mortality data: the Dog Aging Project End of Life Survey. *J Am Vet Med Assoc.* 2023. Preprint: [bioRxiv 2023.04.01.535178](https://www.biorxiv.org/content/10.1101/2023.04.01.535178).
- Pearson EB, Hoffman JM, Melvin RL, McNulty KE, Creevy KE, Ruple A. Analysis of 2,570 responses to Dog Aging Project End of Life Survey demonstrates that euthanasia is associated with cause of death but not age. *J Am Vet Med Assoc.* 2024;262(2). doi:10.2460/javma.23.07.0366 ([PMC10996864](https://pmc.ncbi.nlm.nih.gov/articles/PMC10996864)).
- Salvin HE, McGreevy PD, Sachdev PS, Valenzuela MJ. The canine cognitive dysfunction rating scale (CCDR): a data-driven and ecologically relevant assessment tool. *Vet J.* 2011;188:331–336.
- Creevy KE, Akey JM, Kaeberlein M, Promislow DEL; Dog Aging Project Consortium. An open science study of ageing in companion dogs. *Nature.* 2022;602:51–57.
- Dog Aging Project survey instruments, [github.com/dogagingproject/dataRelease](https://github.com/dogagingproject/dataRelease/tree/master/Survey_Instruments) (accessed Oct 2026).
