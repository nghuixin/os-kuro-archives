# Kuro's protocol, six months at a time

A Blueprint-style log of everything Kuro's care consisted of, in six-month blocks: diet, supplements, medications, therapies, movement, hygiene and monitoring, from the earliest records (2020) to his death (Oct 2026). It is built from [`prescriptions.csv`](../../data/processed/clinical/prescriptions.csv), [`feeding.csv`](../../data/processed/daily_care/feeding.csv), [`visits.csv`](../../data/processed/clinical/visits.csv), [`weights.csv`](../../data/processed/clinical/weights.csv), [`home_care.csv`](../../data/processed/daily_care/home_care.csv), [`grooming.csv`](../../data/processed/daily_care/grooming.csv) and [`health_events.csv`](../../data/processed/clinical/health_events.csv).

**This records what was done, not what anyone should do.** Many items were the owner's own choices, and several were never shown to help (see [diet-review.md](../analyses/diet-review.md)). Discuss any protocol with your own vet. The records also undercount some things: only about 41 of an estimated 100–140 acupuncture sessions are documented, and whether supplements were given every day was rarely recorded.

## The arc

| Phase | Period | Character |
|---|---|---|
| Healthy senior, weight focus | 2020 – 2022 | Overweight, then weight loss; a leg lump removed (2022); supplements chosen by the owner |
| Skin and senses | 2023 | Skin infection, ears and eyes; first FurKids visit |
| Optimisation attempt | H1 2024 | Nutritionist diet, then a tailored raw diet |
| Crisis and stabilisation | H2 2024 | Splenic bleed, transfusion, pancreatitis; palliative care begins |
| Managed multimorbidity | 2025 | Monthly labs, acupuncture, pain control, nightly heat packs |
| Frailty and assisted living | 2026 | Hind-limb weakness, sarcopenia, assisted toileting, more meals |

## Quality of life across the blocks

His quality of life was scored retrospectively for each block from 2024 on, using the **HHHHHMM Quality of Life Scale** (Villalobos), a palliative-care scale with seven items scored 0–10. Scores were prefilled from the records and confirmed by his owner; the evidence for each is in [`hhhhhmm_kuro.csv`](../../data/quality_of_life/hhhhhmm_kuro.csv).

| Item | 2024 H1 | 2024 H2 | 2025 H1 | 2025 H2 | 2026 H1 | 2026 H2 |
|---|---|---|---|---|---|---|
| Hurt | 8 | 6 | 5 | 6 | 6 | 6 |
| Hunger | 9 | 7 | 7 | 8 | 7 | 7 |
| Hydration | 9 | 6 | 7 | 7 | 5 | 5 |
| Hygiene | 8 | 6 | 6 | 7 | 4 | 3 |
| Happiness | 9 | 8 | 8 | 8 | 7 | 7 |
| Mobility | 8 | 7 | 6 | 7 | 4 | 3 |
| More good days than bad | 9 | 7 | 7 | 8 | 6 | 5 |
| **Total (of 70; >35 acceptable)** | **60** | **47** | **46** | **51** | **39** | **36** |

His quality of life stayed above the acceptable line to the end, but only just in his last months. The decline came mainly from **mobility and hygiene**, the parts of his life that depended on people lifting and cleaning him, while **hunger and happiness held up**: he stayed food-driven and engaged. 2025 H1 scores below 2025 H2 because of the Feb–May pain flare. The 2024 H2 hydration score reflects intense thirst, probably from prednisolone, when he drank his own urine at night.

---

Every block below uses the same ten fields, in the same order. "None recorded" means the records hold nothing for that field in that period, not that nothing was done.

### 2020 H1 – 2021 H2 · age 10–11 · "lose the weight"

- **Weight:** 25 kg (2020), up to 31 kg (Jan 2021). The vet's ideal was 26 kg (Nov 2021).
- **Diet:** commercial dog food plus treats. The owner ordered weight loss in 2021: "intermittent fasting 5 days", no morning treats, less kibble and more egg or meat.
- **Supplements:** spirulina, glucosamine, fish treats.
- **Medications:** eye drops at home (from 2021).
- **Procedures and events:** none recorded.
- **Therapies:** none recorded.
- **Mobility:** none recorded.
- **Hygiene and grooming:** occasional grooming.
- **Home and comfort:** none recorded.
- **Monitoring:** about one vet visit a year ("All normal", vaccinated, Nov 2021).

### 2022 H1 · age 12 · "raw food and a lump"

- **Weight:** 28 kg (Jun).
- **Diet:** raw (rabbit meat, beef lung), then a "special dog food" switched in half and half.
- **Supplements:** none recorded.
- **Medications:** antibiotics for a leg lump (May).
- **Procedures and events:** the leg lump removed in a same-day "surgery due to excess fat in the leg" (Jun).
- **Therapies:** massage asked for when his legs looked stiff (May).
- **Mobility:** legs "stiff" (May); wary of crossing the garden pond "because he slipped before" (Jun).
- **Hygiene and grooming:** daily tooth brushing asked for; kangaroo teeth-cleaner chews.
- **Home and comfort:** living outdoors; an elevated mesh bed ("anti skin disease"); water bowl kept free of mould; a larger cage asked for, as he retreated to it when it rained.
- **Monitoring:** vet visits for the lump (May) and surgery (Jun); a blood test at a Gasing vet hospital was never reported back.

### 2022 H2 · age 12 · "cooked meals and supplements"

- **Weight:** "very thin" by Oct 2022 (no number).
- **Diet:** PetChef cooked-meal subscription (250–300 g packs), fewer treats ("not good for kidney").
- **Supplements:** fish oil, probiotics (from Singapore), "the black color supplement".
- **Medications:** none recorded.
- **Procedures and events:** none recorded.
- **Therapies:** none recorded.
- **Mobility:** none recorded.
- **Hygiene and grooming:** mouth-cleanser spray instead of brushing; ear cleaning ("He stressed"); groomer.
- **Home and comfort:** cooling gel mat.
- **Monitoring:** none recorded.

### 2023 H1 · age 13 · "skin"

- **Weight:** none recorded.
- **Diet:** PetChef; dry food with hot water when fresh food ran short.
- **Supplements:** Resvantage Canine (resveratrol), glucosamine daily, "green capsule".
- **Medications:** skin tablets on alternate days (Jan), Surolan ear drops; then eye drops only.
- **Procedures and events:** none recorded.
- **Therapies:** none recorded.
- **Mobility:** none recorded.
- **Hygiene and grooming:** ear cleaner, eye cleanser, Aloveen; a new groomer; a bath every 5 days at most.
- **Home and comfort:** none recorded.
- **Monitoring:** a consultation at an earlier clinic (Taman Megah) for the skin infection (Jan).

### 2023 H2 · age 13 · "allergy management"

- **Weight:** none recorded.
- **Diet:** PetChef, eggs, chicken liver, eggshells, beef treats.
- **Supplements:** Maximus Ophtal (eyes), RESET healthy-ageing capsules, VetClassics mushroom blend (reishi, shiitake, maitake, turkey tail).
- **Medications:** cetirizine, Lanomax eye drops, MiconaHex+Triz medicated shampoo.
- **Procedures and events:** none recorded.
- **Therapies:** neck massage, which "kuro very enjoy" (Oct).
- **Mobility:** "Must bring Kuro on more walks"; no jumping.
- **Hygiene and grooming:** eye balsam, MAOWASH oral-care water additive, cinnamon mouth freshener.
- **Home and comfort:** none recorded.
- **Monitoring:** first FurKids consultations (Sep 2023): "his blood tests are all ok".

### 2024 H1 · age 14 · "the optimisation attempt"

- **Weight:** 21.5 kg (Mar), 23.0 kg (Jun).
- **Diet:** a nutritionist's senior-diet proposal (Jan); an NRC-balanced recipe analysed by Khan & Kara Enterprise (The RAW Proof) (Mar: 895 kcal/day, 43% of calories from fat); a **tailored raw diet** from the same business from about 25 Mar (salmon head, meaty bones, spleen and liver, vegetables, oils, kelp, zinc). Then low-fat gastrointestinal food after pancreatitis (Jun).
- **Supplements:** Maximus Ophtal, Supra Mineral daily, Cosequin, chlorophyll, dental liquid.
- **Medications:** none recorded.
- **Procedures and events:** splenic bleed at the end of June, HCT 13%.
- **Therapies:** "physio" paid for at FurKids (before May).
- **Mobility:** "very hard to get up" on the slippery wooden floor (Apr); "walk very funny like a bear" (Jun); dog shoes for slippery floors (Jun).
- **Hygiene and grooming:** teeth cleaned by the groomer (Jan); grooming every 2–3 weeks.
- **Home and comfort:** the wooden floor judged "bad for Kuro legs" (Apr); mats or shoes suggested.
- **Monitoring:** 3 blood-panel days; anaemia already present (HCT 34%, May).

### 2024 H2 · age 14 · "crisis, then palliative care"

- **Weight:** 21.3–21.7 kg.
- **Diet:** low fat. Royal Canin and Vet Pro gastrointestinal food, then chicken breast, sweet potato and pumpkin twice a day, a boiled egg in the evening, and a pork topper.
- **Supplements:** Protexin Pro-Enzorb, Maximus Hep, Samylin, Adored Beast Liver Tonic and Fido's Flora, Lypex (pancreas), Neuroforte, YuMove, Glycoflex, B12, Dr. Harvey's multivitamin, turmeric, herbal powders, activated charcoal.
- **Medications:** prednisolone (started and tapered); Baytril, Clavamox, Metrogyl; Cerenia and Yunnan Baiyao kept for emergencies; Maltofer iron (from Oct); **darbepoetin injections (from Oct)**; Lanomax eye drops; wound ointment.
- **Procedures and events:** ICU, blood typing and transfusion (Jun–Jul); x-rays and ultrasound; fine-needle aspirate. The mass was judged inoperable, so palliative care. Severe anaemia again in Nov (HCT 18.9%).
- **Therapies:** **acupuncture at Asia Paws from Jul** (weekly from Aug); house-call vet visits.
- **Mobility:** walks up to 30 minutes; careful on stairs to protect the spleen; dog shoes, also worn at acupuncture.
- **Hygiene and grooming:** grooming moved indoors to avoid falls; diapers from Aug.
- **Home and comfort:** a mat over the slippery outdoor area ("Mat very good", Aug); his pen enlarged; sleeping in air-conditioning (Aug); moved temporarily to the old house during building works (Dec).
- **Monitoring:** 9 vet consultations including an outside clinic; 4 blood-panel days with results (more were billed).

### 2025 H1 · age 15 · "managed multimorbidity"

- **Weight:** 20.0–22.0 kg.
- **Diet:** home-cooked carrot, cabbage, broccoli, beef liver, beef lung and chicken breast; lamb and fish treats.
- **Supplements:** Protexin, Maximus Hep, Samylin, Supra Mineral, Adored Beast range, YuMOVE Senior, Neuroforte, Gut Soothe, Vital Defense, turkey tail mushroom, Xiao Chai Hu Tang (Chinese herbal), homeopathic Arnica and Hypericum, Schuessler cell salts, magnesium oil.
- **Medications:** prednisolone 5 mg; Maltofer iron (daily, then every other day); darbepoetin; Clavamox; **Galliprant** and **gabapentin** for arthritis and nerve pain (Apr); chlorhexidine wash and mupirocin for a leg wound.
- **Procedures and events:** a pain flare with limping and an ulcerated hind-leg wound (Apr–May); house-call vet (Apr).
- **Therapies:** **acupuncture** (twice weekly at times); **hot/cold packs on the hips, about twice daily from May**.
- **Mobility:** "struggling to get up" (May); a rear-support wheelchair was considered.
- **Hygiene and grooming:** brushing asked for repeatedly; plaque on the back teeth; grooming every 2–3 weeks.
- **Home and comfort:** his cage, which he broke out of in Apr.
- **Monitoring:** 9 FurKids consultations; 6 blood-panel days; x-rays (May); house calls.

### 2025 H2 · age 15 · "steady, with a flare"

- **Weight:** 21.3–21.9 kg.
- **Diet:** strict low fat for a month (Nov); beef lung, carrot, long beans, mushrooms, goji berry and fish, with no liver. He stopped eating pumpkin and sweet potato (Aug).
- **Supplements:** Protexin, Samylin, Gut Soothe, slippery elm, Roots Soil & Sea, Xiao Chai Hu Tang, homeopathic Arnica and Strophanthus.
- **Medications:** prednisolone 5 mg, iron, gabapentin, **Ursofalk** (liver, Oct), omeprazole; a painkiller and gastroprotectant for a pancreatitis flare (Nov, lipase 4,451).
- **Procedures and events:** a near-miss at the garden pond, stepping through the softening mat laid over it (31 Oct); pancreatitis flare (Nov); a slip at the clinic and a mild left hind sprain (Dec).
- **Therapies:** **hot packs almost every evening** (165 sessions this half-year); acupuncture weekly ("once a week is enough"); massage of the left hind leg.
- **Mobility:** "right side hip pain" and walking "abit weird" (Sep); "running around like a horse" (Nov), "so nimble n can jump" (Dec).
- **Hygiene and grooming:** mouth spray; TropiClean oral care; grooming every 2–3 weeks (dental work at grooming declined).
- **Home and comfort:** no air-conditioning for him, because of his arthritis (Jul).
- **Monitoring:** 7 FurKids consultations; roughly monthly blood tests; x-ray on 29 Dec (abdominal mass 197.5 × 179.7 mm).

### 2026 H1 · age 16 · "frailty begins"

- **Weight:** 22.2 kg, falling to 19.9 kg.
- **Diet:** smaller, more frequent meals: 200 g three times a day with probiotics, then **four meals a day** (May); water every 2 hours on a feeding chart.
- **Supplements:** Protexin Pro-Enzorb, Samylin, Supra Mineral, Antinol (joint, from Apr), liver supplement, Chinese herbal medicine from Asia Paws (Jun).
- **Medications:** prednisolone 5 mg (½ tablet every other day); iron; darbepoetin; antibiotics for a suspected infection (Apr); eye drops.
- **Procedures and events:** dental cleaning at Asia Paws (Jan, owner's recollection); a new household helper (16 Apr); unable to stand and found lying in urine (10 Jun).
- **Therapies:** hot packs nightly until Apr; acupuncture **twice weekly** (May–Jun).
- **Mobility:** "couldn't get up" after pooping (Apr); after 10 Jun, walked on a lead in the backyard three times a day.
- **Hygiene and grooming:** diapers and belly wraps (Feb–Mar); absorbent pads; after 10 Jun, **help to urinate at least four times a day**; home grooming roughly monthly (none in Apr).
- **Home and comfort:** water kept within reach (Jun).
- **Monitoring:** 4 FurKids consultations; monthly blood tests (several results never received).

### 2026 H2 · age 16 · "comfort and support" (to 18 Oct)

- **Weight:** 19.4–19.7 kg.
- **Diet:** meals **increased by 10–15%** to hold 19.5–20 kg; about **1 litre of water a day** for high urea; apple in the water bowl to encourage drinking.
- **Supplements:** Si Miao San and Xiao Chai Hu Tang (Chinese herbal, Oct); kidney supplement (Aug); liver tonic.
- **Medications:** prednisolone; **iron daily** (vet, Jul); darbepoetin; antibiotics for a wound (Sep); Advocate for parasites.
- **Procedures and events:** a nibbled leg wound (Sep); died 18 Oct 2026.
- **Therapies:** acupuncture; home massage advised (Oct); a red-light therapy mat recommended (16 Oct).
- **Mobility:** progressive hind-limb weakness; anti-slip paw grips; getting up on his own "a bit better" (9 Oct).
- **Hygiene and grooming:** toilet help at "4 fixed / absolutely regular times daily"; daily wipes and blow-drying after baths; groomed at home in Jul and on 13 Oct.
- **Home and comfort:** water within reach; the anti-slip mats had worn out by his final months (owner's recollection).
- **Monitoring:** FurKids check-ups in Jul, Aug and Sep (blood work "stable"); acupuncture vet's assessment on 2 Oct ("clear" apart from progressive hind-limb weakness).

---

## Patterns another owner might notice

1. **The protocol grew with each crisis.** About 5 regular items in 2023 became 20 or more after Jul 2024. The sheer number of supplements made it hard to know what was given each day, or what helped.
2. **Monitoring became the backbone.** From 2025, monthly blood panels (anaemia, liver, kidney, pancreas) guided the drug changes. Results for 8 billed tests never reached the owner, so ask for every printout.
3. **Therapies shifted from cure to comfort.** Acupuncture, heat packs and massage were added as mobility declined, and the documented ones were done consistently: 321 heat-pack sessions.
4. **Daily living care was the hardest part.** Toileting help, hygiene and tooth brushing depended on several people. These were the gaps most often raised in the family chat.
5. **Nothing measured how he felt.** Weights and labs were frequent, but pain, mobility, quality of life and muscle condition were never scored.
