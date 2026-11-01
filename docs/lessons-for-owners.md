# What another senior-dog owner can learn from Kuro

Kuro lived to 16 years 7 months. In his last two and a half years he lived with an inoperable splenic tumour, anemia, pancreatitis, arthritis and gradual loss of mobility, cared for by his family, a household helper, a pet sitter, a pet taxi driver, a groomer and three clinics. This page turns his records into five practical questions. Each case has four parts: **what happened to Kuro**, **what the records support**, **what remains unknown**, and **questions to discuss with your own vet**.

His records show something that is easy to miss: **medical management and daily quality of life are related but distinct.** A dog can keep receiving good veterinary treatment while becoming steadily more dependent on people for moving, toileting, hygiene and safety. Both need planning.

This is one dog's history, not veterinary advice. Use it to prepare better questions, not to diagnose your own dog.

## Care-transition timeline

When each problem moved from *something to watch* to *something that needed daily help*. Sources are the CSVs in [`data/processed/`](../data/processed/) and the [health summary](health-summary.md).

| Area | Monitoring | Regular treatment | Daily assistance |
|---|---|---|---|
| **Blood and tumour** | "Low red blood count" first mentioned (May 2023); HCT 34% (May 2024) | Transfusion and ICU, tumour judged inoperable (Jun–Jul 2024); prednisolone, iron, then darbepoetin (from Oct 2024); roughly monthly blood tests (2025–26) | Medicines given at home every day from Jul 2024 |
| **Mobility** | "Crepitus… indicating arthritis" at a house call (Jul 2024) | Acupuncture from Jul 2024, weekly then twice weekly at times; "arthritis and some nerve pain" with Galliprant (Apr 2025) | Hot packs almost every evening (May 2025 – Apr 2026); carried in lifts (Sep 2025); "unable to stand" at acupuncture (Jun 2026); muscle loss ("sarcopenia", Jul 2026) |
| **Toileting** | Bladder control a concern on long trips (Jul 2024) | Diapers for outings and acupuncture (from Aug 2024) | Belly wraps and stained bedding (Feb–Mar 2026); "found lying in urine", urine-scald risk (Jun–Jul 2026) |
| **Eating** | Weight loss and a senior diet (Jan–Mar 2024) | Low-fat diet after pancreatitis (Jun 2024); strict low fat during a flare (Nov 2025) | Smaller meals three times a day (May 2026), then 10–15% more food and measured water to hold his weight (Jul–Aug 2026) |
| **Hygiene and skin** | Dandruff and itching (2021–23) | Medicated shampoo and ear drops (2023); home grooming every 2–3 weeks (2024–26) | Grooming moved indoors to avoid falls (from Jul 2024); wound care with a cone (Jul 2024, May 2025) |
| **Safety** | — | Careful handling on stairs to protect the spleen (Jul 2024) | Supervision near the garden pond ("make sure… his leg won't drop into water", Jun 2024). He was found in the pond on 18 Oct 2026; the post mortem could not say whether he collapsed first |

## 1. How do I recognize when my dog's normal routine needs to change?

**What happened to Kuro.** In the days before his Jun 2024 emergency he vomited, ate little, limped and had a bloated stomach. His HCT had already been below range a month earlier (34.0% on 27 May), then fell to 24.8% (28 Jun) and 13.2% (30 Jun), when he needed a transfusion.

**What the records support.** The crisis followed a few weeks of small changes in appetite, energy and gait, and a lab value that was already low. Later, routine changes tracked his decline: shorter walks, more rest, the move to nightly hot packs, smaller and more frequent meals.

**What remains unknown.** When the tumour began. The May 2023 mention of a "low red blood count" and a Jan 2024 "high SDMA" have no numbers in the records, so it is not clear what was followed up.

**Questions for your vet.**
- Which changes in appetite, drinking, energy, gait or breathing should make me call you, rather than wait for the next check-up?
- If a lab value is slightly out of range, when should we recheck it?
- Should my senior dog have a baseline abdominal ultrasound?

## 2. Which clinical signs should prompt urgent veterinary attention?

**What happened to Kuro.** The owner's notes after his Jul 2024 hospital stay list **pale gums and laboured breathing** as signs to watch for, and carers were told to watch for **blood in the stool or vomit**. Cerenia and Yunnan Baiyao were kept at home for those events. Carers were told to handle him carefully on stairs so he wouldn't hit his abdomen. In Nov 2024 his HCT dropped to 18.9% while his usual vets were away, and he was seen at another clinic.

**What the records support.** With a splenic mass, the warning signs were those of internal bleeding and anemia: weakness, pale gums, fast breathing, collapse and dark stools. Dark stools in Nov 2024 came days after his worst anemia, although activated charcoal, which also darkens stool, is a confounder.

**What remains unknown.** Whether his death on 18 Oct 2026 had warning signs in the hours before. The post mortem found partial splenic rupture "not… a fresh, acute event" and could not establish the terminal mechanism.

**Questions for your vet.**
- Given my dog's conditions, which signs mean "go to an emergency clinic now"?
- Which emergency clinic should we use when you are closed or away, and can they see my dog's records?
- Should I keep any medicines at home for emergencies, and when should I use them?

## 3. What should I record and ask my vet when a blood-test result changes?

**What happened to Kuro.** He had more than 40 in-house blood panels. His anemia was repeatedly flagged by the analyzer as "likely non-regenerative". Urea rose from Dec 2025 (peaking at 17.2 mmol/L in Aug 2026) while creatinine and SDMA stayed normal. ALT was above range for much of 2025. Results are missing for 8 visits where tests were billed.

**What the records support.** Keeping every printout made trends visible. They showed the anemia was chronic rather than new, and that kidney function markers stayed normal even as urea rose. Billed tests without results were only discovered by cross-checking invoices against reports ([`visits.csv`](../data/processed/visits.csv), `lab_status`).

**What remains unknown.** The values for those 8 visits, and the written reports for the 2024 ultrasound, the needle aspirate and the post mortem.

**Questions for your vet.**
- Can I have the full printout of every test, including the reference ranges?
- Is this change outside my dog's own usual range, not just the lab's range?
- What could explain it (disease, medicine, diet, hydration), and when will we recheck?
- Does a change here mean we should change the diet or a medicine?

## 4. How do I organize daily care when several people share responsibility?

**What happened to Kuro.** His owner was often abroad. Daily care was split among his parents, a live-in helper, a pet sitter, a pet taxi driver, a groomer and the clinics, with one WhatsApp group for each role. The helper photographed stools and every hot-pack session. The owner wrote care notes and medicine schedules, and carers sent updates after each acupuncture visit.

**What the records support.** The photo log shows care actually done, not just recommended: 321 hot-pack sessions and 63 stool photos ([`home_care.csv`](../data/processed/home_care.csv), [`stool_log.csv`](../data/processed/stool_log.csv)). Written handover notes, such as which emergency signs to watch and how to handle him on stairs, went to every carer. A written update after his 10 Jun 2026 acupuncture session told the family he could no longer stand and had been lying in urine.

**What remains unknown.** What was never logged. For example, only 41 acupuncture sessions are documented, but there were probably 100–140. Separate chats also made it hard to see one complete picture at any moment.

**Questions to settle (with your vet and your carers).**
- Who gives each medicine, and how do they confirm it was given?
- What goes in one shared log: food, water, stools, urine, medicines, mobility, mood?
- Which changes does each carer report straight away, and to whom?
- Does every carer have the emergency signs and clinic contacts in writing?

## 5. What should I budget and plan for if my dog loses mobility?

**What happened to Kuro.** His vet invoices and service records document about **RM38,500**, and the full total was probably RM52,000–65,000. Mobility care added recurring costs and labour: acupuncture once or twice a week, a pet taxi to get him there, house calls, diapers and wraps, hot packs, and indoor grooming. The family looked at a rear-support dog wheelchair in May 2025. Daily help with standing, toileting and cleaning fell mainly on the household helper.

**What the records support.** Mobility loss was gradual, starting with arthritis in Jul 2024 and ending with an inability to stand by Jun 2026. Each step needed more people and time, as well as money ([`providers.csv`](../data/processed/providers.csv), [`invoice_items.csv`](../data/processed/invoice_items.csv)).

**What remains unknown.** The full cost: some invoices and most acupuncture sessions are missing. Also unknown is whether earlier home changes would have helped, such as non-slip flooring, ramps or fencing the pond.

**Questions for your vet.**
- What will my dog likely need as mobility declines: pain relief, physiotherapy, a harness, a wheelchair?
- How should I adapt the home: floors, stairs, water, sleeping area?
- How will we judge quality of life as care needs grow, and when should we talk about end-of-life care?
