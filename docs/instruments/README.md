# Validated instruments for monitoring a senior dog

Owner-completed and clinician scales for older dogs that have **published validation** (reliability, validity or both in peer-reviewed studies). Each entry says what the evidence shows and where the official form can be obtained. The forms themselves are **not reproduced here**: most are copyrighted, and some may only be downloaded by veterinary professionals.

This is a record-keeping aid, not veterinary advice. Bring scores to your vet rather than acting on them alone.

## Instruments

| Domain | Instrument | What it measures | Scoring | Validation evidence | How to get it | Suggested frequency |
|---|---|---|---|---|---|---|
| Quality of life | **VetMetrica HRQL** (Reid et al., 2013) | 22 items; energetic/enthusiastic, happy/content, active/comfortable, calm/relaxed | Online; benchmarked against healthy dogs | Developed and validated with reliability testing (Reid et al., 2013); shortened to 22 items (Reid et al., 2018) | **Commercial licence** from NewMetrica; also offered in some vet apps | Every 3 months; monthly if ill |
| Quality of life | **CORQ**, Canine Owner-Reported Quality of Life (Giuffrida et al., 2018) | 17 items; vitality, companionship, pain, mobility; past 7 days | 1–7 per item, higher = better | Psychometric testing in dogs with cancer (Giuffrida et al., 2018); Spanish validation (2025); associated with age-related decline and mortality in senior dogs (PLoS ONE, 2024) | From the authors or the original paper | Every 3 months |
| Chronic pain | **CBPI**, Canine Brief Pain Inventory (Brown et al., 2008) | Pain severity (4 items) and interference with daily activity (6 items) | 0–10 scales | Detects response to treatment in osteoarthritis (Brown et al., 2008) | **Copyright University of Pennsylvania**; free after agreeing to the terms on Penn Vet's [registration form](https://app.smartsheet.com/b/form/8a907567c13d42ebbcfa58ff5a07b69e) | Monthly; before and after any pain-treatment change |
| Chronic pain | **LOAD**, Liverpool Osteoarthritis in Dogs (Hercock et al., 2009) | Mobility and exercise in osteoarthritis | 0–52; 0–10 mild, 11–20 moderate, 21–30 severe, 31–52 extreme | Validated against clinical assessment (Hercock et al., 2009) | Owned by the University of Liverpool, distributed by Elanco; [download restricted to animal-health professionals](https://my.elanco.com/en_gb/product-support/pet/the-liverpool-osteoarthritis-in-dogs-load-questionnaire-access), so ask your vet | Monthly |
| Chronic pain | **HCPI**, Helsinki Chronic Pain Index (Hielm-Björkman et al., 2009) | 11 items; mood, vocalisation, willingness to move | 0–4 per item, total 0–44 | Psychometric testing (Hielm-Björkman et al., 2009); Italian validation (2023), Spanish translation (2025) | English HCPI-E2 [freely available for research use](https://dspace.uevora.pt/rdpc/bitstream/10174/19611/1/HCPI_E2.pdf) | Monthly |
| Cognitive dysfunction (diagnosis) | **CCDR**, Canine Cognitive Dysfunction Rating scale (Salvin et al., 2011) | 13 behaviour items | 13–80; ≥50 suggests cognitive dysfunction, 40–49 borderline | Diagnostic accuracy and two-month test–retest reliability (r = 0.73) reported in the original paper | Published in the original paper (*Vet J*, doi:10.1016/j.tvjl.2010.05.014) | Every 6 months from about age 8; every 3 months if concerned |
| Cognitive dysfunction (staging) | **CADES**, Canine Dementia Scale (Madari et al., 2015) | 17 items; spatial orientation, social interaction, sleep–wake, house soiling | 0–5 per item by frequency, total 0–95; bands for normal, mild, moderate, severe | Validated as a screening tool and predictor of progression in 215 dogs (Madari et al., 2015) | Original paper (doi:10.1016/j.applanim.2015.08.034); German form from [TiHo Hannover](https://www.tiho-hannover.de/fileadmin/13_Kleintiere/Down/Neuro/CADES_Questionnaire_deutsch_Hund.pdf) | Every 6 months once diagnosed |
| Body condition | **WSAVA 9-point Body Condition Score** | Fat cover | 1–9; 4–5 ideal | Validated against body fat measured by DEXA (Laflamme, 1997) | [WSAVA chart](https://wsava.org/wp-content/uploads/2020/01/Body-Condition-Score-Dog.pdf) | Every vet visit; monthly at home |
| Muscle condition | **WSAVA Muscle Condition Score** | Muscle over spine, scapulae, skull, hips | Normal / mild / moderate / severe loss | **Partial:** substantial repeatability and moderate reproducibility in dogs, weaker for mild and moderate loss (Freeman et al., 2019); described in 2024 as still lacking full validation for dogs | [WSAVA chart](https://wsava.org/wp-content/uploads/2020/01/Muscle-Condition-Score-Chart-for-Dogs.pdf) | Every vet visit; monthly at home |
| Frailty | **Canine frailty phenotype** (Hua et al., 2016) | Five components, including weight loss, weakness, low activity, exhaustion, slowness | Number of components met; ≥2 = frail | **Early:** in 116 aged guide dogs, ≥2 components predicted death (adjusted hazard ratio 3.9); the authors say the concept needs further development | Original paper (*Am J Vet Res* 2016;77:1357–1365) | Every 6 months |
| Frailty | **Canine Frailty Index** (Banzato et al., 2019) | Accumulated health deficits from clinical records | 0–1 | **Early:** rose with age and predicted 6-month mortality with moderate accuracy; used in a 451-dog multi-centre study (2022) | Open-access paper (*Scientific Reports*, 2019) | Yearly |

The human equivalents, for anyone adapting this: VetMetrica and CORQ play the role of the SF-36 or EQ-5D, the CBPI is adapted from the human Brief Pain Inventory, the CCDR and CADES sit where cognitive screens such as the AD8 sit, and the frailty phenotype is adapted from Fried's criteria.

## Not included, and why

| Tool | Reason |
|---|---|
| **HHHHHMM quality-of-life scale** (Villalobos, 2004) | Widely used in hospice care, but no peer-reviewed validation study was found; its author describes it as "not perfect", and published cut-offs disagree |
| **DISHAA checklist** (Landsberg) | Recommended by 2025 canine cognitive dysfunction guidelines, but no psychometric validation study was found. Use the CCDR or CADES for a validated score |
| **Purina Fecal Scoring Chart** | Widely used in research and clinics (and used for `stool_log.csv` in this archive), but no peer-reviewed reliability or validation study was found. This archive measured its own inter-rater agreement instead (weighted kappa 0.61) |
| **AAHA Senior Care Guidelines** visit schedule | A consensus guideline, not a measurement instrument |
| **Blood-based cancer screens** (Nu.Q, OncoK9) | Laboratory tests rather than monitoring instruments; moderate sensitivity |

## Recording template

[`data/templates/senior_monitoring_template.csv`](../../data/templates/senior_monitoring_template.csv) has one row per assessment date, with a column for each instrument above plus `source` and `confidence`. Kuro's archive predates this template: apart from weights, his records contain none of these scores, so they could not be filled in retrospectively.

## Local copies of the forms

Freely downloadable forms (HCPI-E2, CADES in German, WSAVA BCS and MCS, Purina chart) are saved in `docs/instruments/forms/` on the archive owner's computer. That folder is excluded from Git so copyrighted forms are not republished.

## References

- Reid J, Wiseman-Orr ML, Scott EM, Nolan AM. Development, validation and reliability of a web-based questionnaire to measure health-related quality of life in dogs. *J Small Anim Pract.* 2013;54:227–233. doi:10.1111/jsap.12059
- Reid J, Wiseman-Orr L, Scott M. Shortening of an existing generic online health-related quality of life instrument for dogs. *J Small Anim Pract.* 2018.
- Giuffrida MA, Brown DC, Ellenberg SS, Farrar JT. Development and psychometric testing of the Canine Owner-Reported Quality of Life questionnaire, an instrument designed to measure quality of life in dogs with cancer. *J Am Vet Med Assoc.* 2018;252:1073–1083.
- Brown DC, Boston RC, Coyne JC, Farrar JT. Ability of the Canine Brief Pain Inventory to detect response to treatment in dogs with osteoarthritis. *J Am Vet Med Assoc.* 2008;233:1278–1283.
- Hercock CA, Pinchbeck G, Giejda A, Clegg PD, Innes JF. Validation of a client-based clinical metrology instrument for the evaluation of canine elbow osteoarthritis. *J Small Anim Pract.* 2009;50:266–271.
- Hielm-Björkman AK, Rita H, Tulamo RM. Psychometric testing of the Helsinki chronic pain index by completion of a questionnaire in Finnish by owners of dogs with chronic signs of pain caused by osteoarthritis. *Am J Vet Res.* 2009;70:727–734.
- Salvin HE, McGreevy PD, Sachdev PS, Valenzuela MJ. The canine cognitive dysfunction rating scale (CCDR): a data-driven and ecologically relevant assessment tool. *Vet J.* 2011;188:331–336. doi:10.1016/j.tvjl.2010.05.014
- Madari A, Farbakova J, Katina S, et al. Assessment of severity and progression of canine cognitive dysfunction syndrome using the CAnine DEmentia Scale (CADES). *Appl Anim Behav Sci.* 2015;171:138–145. doi:10.1016/j.applanim.2015.08.034
- Laflamme D. Development and validation of a body condition score system for dogs. *Canine Pract.* 1997;22:10–15.
- Freeman LM, Michel KE, Zanghi BM, Vester Boler BM, Fages J. Evaluation of the use of muscle condition score and ultrasonographic measurements for assessment of muscle mass in dogs. *Am J Vet Res.* 2019;80:595–600.
- Christie et al. Interobserver variability of assessing body condition scores and muscle condition scores in a population of 43 active working explosive detection dogs. *Front Vet Sci.* 2024. doi:10.3389/fvets.2024.1431855
- Hua J, Hoummady S, Muller C, et al. Assessment of frailty in aged dogs. *Am J Vet Res.* 2016;77:1357–1365.
- Banzato T, Franzo G, Di Maggio R, et al. A Frailty Index based on clinical data to quantify mortality risk in dogs. *Sci Rep.* 2019. (open access, PMC6856105)
- WSAVA Global Nutrition Committee. Body Condition Score and Muscle Condition Score charts for dogs.

*Validation details were checked against the papers' abstracts and the publishers' or authors' pages in Oct 2026. Check full texts before relying on specific statistics.*
