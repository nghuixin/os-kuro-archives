# Diet critique: NRC Balanced White + Red Meat, Senior V2 (Mar 2024)

A brief review of the tailored recipe in [`data/processed/diet.csv`](../data/processed/diet.csv), analysed on 15 Mar 2024 for Kuro at 21.5 kg, inactive senior. It almost certainly corresponds to the **tailored raw diet** he started around 25 Mar 2024, whose ingredients the owner listed in the grooming chat: salmon head, chicken meaty bones, cooked spinach, buffalo spleen and liver, chicken liver, red cabbage, cooked carrot, blueberries, psyllium husk, kefir, inulin, pumpkin seeds, curcumin, piperine, flax seed, wheat germ oil, kelp powder and zinc. The recipe is 540 g and 895 kcal a day. Values are converted to per 1,000 kcal so they can be compared with published limits. This is a desk review, not a substitute for a board-certified veterinary nutritionist.

## What it gets right

- **Calories match the requirement:** 895 kcal against 899 kcal.
- **Protein is generous:** about 78 g per 1,000 kcal (31% of calories), well above the AAFCO minimum of about 45 g. That suits a senior dog, and his later records note "sarcopenia (muscle atrophy)".
- **Calcium-to-phosphorus ratio** is 1.22, inside the 1–1.4 target.
- **Omega-3s (EPA + DHA)** are about 1.4 g per 1,000 kcal, a meaningful dose for joints. The EPA:DHA ratio (0.59) is below the analysis tool's own "balanced" range, but that is minor.

## Concerns

| # | Issue | Recipe | Reference |
|---|---|---|---|
| 1 | **Fat is high** | ~48 g / 1,000 kcal (43% of calories) | Common low-fat threshold < 30 g; 20–25 g after a pancreatitis episode; ~38 g often cited even with no history |
| 2 | **Vitamin D is above the AAFCO maximum** | ~1,090 IU / 1,000 kcal; ~5,200 IU/kg dry matter; ~94% of the NRC safe upper limit by body weight | AAFCO max 750 IU / 1,000 kcal; 3,000–3,200 IU/kg DM; NRC SUL 2.6 µg/kg^0.75 (~26 µg/day for him) |
| 3 | **Nutrients only just met** | Choline 100.4%, vitamin K 103% of the NRC allowance | Recipes usually aim well above 100% to cover cooking losses and ingredient variation |
| 4 | **Iron doubled up** | ~5× the NRC allowance (33.8 mg) from food alone | He was also given Maltofer and iron tablets from 2024 for anemia |
| 5 | **Phosphorus fine at the time, but above kidney-diet levels** | ~1.4 g / 1,000 kcal | Kidney diets use 0.4–1.1 g / 1,000 kcal |
| 6 | **Sodium high** | ~3.7× the NRC allowance | Acceptable for a healthy dog; worth limiting with heart or kidney disease |

### Notes on each

1. **Fat.** Three months after this analysis (28 Jun 2024) Kuro had lipase of 5,745 U/L and an abnormal cPL, and the vet put him on a low-fat diet. The evidence that dietary fat causes pancreatitis is not conclusive, so this can't be called the cause. But the recipe would have needed reformulating after Jun 2024. The records only show a switch to commercial low-fat gastrointestinal food, so it's unclear whether that happened.
2. **Vitamin D.** Those limits were set mainly to protect large-breed puppies rather than tested in adult dogs, but there is almost no margin left once supplements are added. Worth correcting.
3. **Choline and vitamin K.** No buffer for losses during cooking.
4. **Iron.** Probably not harmful during anemia, but the vet should have known the diet's iron content when prescribing more.
5. **Phosphorus.** His creatinine and SDMA stayed normal throughout, so restriction wasn't indicated. His urea did rise in 2025–26, so it should be rechecked if the recipe were reused.

## What was actually fed

Photos and chats in [`feeding.csv`](../data/processed/feeding.csv) show what reached the bowl after the analysis:

- **25 Mar – Jun 2024: the tailored raw diet** (ingredients above). It includes **chicken meaty bones** (a calcium source), **wheat germ oil and flax** (oils), kelp and zinc, so it was a complete recipe on paper. It was **raw and high in fat**, and he developed pancreatitis about three months after starting it; on 29 Jun 2024 the owner wrote, "Maybe from his diet change". In Apr–May 2024 the groomer also linked new tail hair loss to the diet change.
- **Jul 2024 (after the pancreatitis episode):** "chicken breast, 0.25 cup of sweet potatoes, 0.25 cup of pumpkin, 2x day", plus Royal Canin and Vet Pro low-fat gastrointestinal food from FurKids, a boiled egg in the evening, and a pork food topper (70% muscle meat with bones and vegetables).
- **Jul 2024 care notes:** the same chicken, sweet potato and pumpkin meals, plus Dr. Harvey's Multivitamin & Mineral Powder (4 scoops, twice a day), turmeric and a herbal powder mixed in.
- **Oct 2024:** a handwritten list, "Kuro Daily Foods Ingredients": beef or chicken breast, sweet potatoes, pumpkin, broccoli, blueberries.
- **2025 care notes:** carrot, cabbage, broccoli, beef liver, beef lung, chicken breast, occasional frozen berries.
- **Treats:** beef, lamb, fish and salmon-and-egg treats and chews, 2023–2025.

Two points follow:

1. **After the raw diet stopped, calcium and oil are unaccounted for.** The raw recipe covered them (bones, wheat germ oil, flax), but the home-cooked lists from Jul 2024 onward include no calcium source, oil or vitamin-mineral mix, which an NRC-balanced meat-and-vegetable recipe depends on. The owner's Jul 2024 care notes show that **Dr. Harvey's Multivitamin & Mineral Powder, 4 scoops twice a day**, was mixed into his food, with turmeric and a herbal powder. That covers the vitamin-mineral gap for 2024, but whether it supplied enough calcium depends on its formulation, which the records don't give. By 2025 it no longer appears on the supplement list. The 2025 ingredient list adds **beef liver and beef lung**, which add vitamin A, B vitamins, iron and copper, but still no calcium source or oil.
2. **The Jul 2024 version suits the vet's low-fat order.** Chicken breast with pumpkin and sweet potato is a lean base, unlike the 43%-fat analysed recipe. But it gives no meat quantity, so its calories and protein can't be checked against his weight loss later on.

## Overall

A well-built maintenance recipe for a healthy senior. But it is a **raw, high-fat** recipe — **too high in fat** for a dog who developed pancreatitis about three months after starting it — **over the AAFCO vitamin D maximum**, and **only just adequate** on choline and vitamin K. The analysis covers the recipe as written, not what was actually cooked and eaten.

## Sources

- [IVIS – Vitamin D and canine health](https://www.ivis.org/library/veterinary-focus/nutrition-matters-veterinary-focus-vol-283-nov-2018/vitamin-d-canine-health)
- [Royal Canin Academy – Vitamin D in canine health](https://academy.royalcanin.com/en/veterinary/vitamin-d-in-canine-health)
- [PMC10445235 – vitamin D in dog foods](https://pmc.ncbi.nlm.nih.gov/articles/PMC10445235)
- [Frontiers in Veterinary Science 2023 – vitamin D upper limit](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2023.1242851/full)
- [PMC4976120 – AAFCO/NRC vitamin D ranges](https://pmc.ncbi.nlm.nih.gov/articles/PMC4976120)
- [Vet Times – Fat-sensitive conditions in dogs](https://www.vettimes.com/clinical/small-animal/fat-sensitive-conditions-in-dogs?hub=true)
- [PMC9151489 – dietary fat and pancreatitis review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9151489/)
- [Science Insights – low-fat thresholds for pancreatitis](https://scienceinsights.org/what-is-the-best-low-fat-dog-food-for-pancreatitis/)
- [Today's Veterinary Practice – ACVN nutrition (renal diet phosphorus)](https://todaysveterinarypractice.com/wp-content/uploads/sites/4/2016/05/2016-0304_ACVN-Nutrition.pdf)
- [IVIS – Royal Canin nutritional information (phosphorus restriction)](https://www.ivis.org/library/encyclopedia-of-canine-clinical-nutrition/royal-canin-nutritional-information-6)
