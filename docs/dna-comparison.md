# DNA tests compared: Wisdom Panel (Jan 2023) vs Embark (Feb 2025)

Kuro took two commercial DNA tests. The DNA is the same, so every difference comes from the companies' reference panels, algorithms and wording. The item-by-item scores are in [`data/processed/dna_comparison.csv`](../data/processed/dna_comparison.csv) (1 = agree, 0 = disagree). The raw Embark data is in [`data/raw/embark/`](../data/raw/embark/); the Wisdom Panel report is not published.

## Scorecard

| Area | Binary score | Quantitative measure |
|---|---|---|
| Breed ancestry | **4 / 8** | 71% overlap in breed percentages; 4 of 14 breeds found by both |
| Health variants | **2 / 2** | 128 of 128 genes tested by both give the same result (all clear) |
| Physical traits | **23 / 23** | Same genotype at all 23 genes tested by both; 21 of 23 described the same way |
| Diversity and size | **2 / 2** | — |
| **Total** | **31 / 35 (89%)** | |

**Breed overlap** is the share of ancestry both tests assign to the same breed: the sum, over all breeds, of the smaller of the two percentages. A breed percentage counts as agreeing when the two are within 5 points.

## Breed ancestry

| Breed | Wisdom Panel | Embark |
|---|---|---|
| Golden Retriever | 60% | 52.1% |
| Japanese Spitz | 7% | 33.8% |
| Miniature Pinscher | 8% | 8.4% |
| German Shepherd Dog | 4% | 5.7% |
| Chihuahua | 5% | — |
| Asian breeds (Mongolian Xigou, Qingchuan Hound, Jindo, Chinese Shar-Pei, Thai Ridgeback) | 9% | — |
| Labrador Retriever, Australian Cattle Dog, American Eskimo Dog | 2% each | — |
| Pomeranian | 1% | — |

## Disagreements, ranked by severity

1. **Japanese Spitz, 7% vs 33.8% (high).** A 27-point gap on a major component. The Japanese Spitz was developed in Japan in the 1920s–30s from white German Spitz-type dogs, possibly with Samoyed, so it shares much of its genome with the American Eskimo Dog, Pomeranian and Samoyed (Parker et al. 2017, *Cell Reports*). With a small Japanese Spitz reference set, those segments get assigned to related or Asian breeds, which is what the Wisdom report shows.
2. **Family tree (moderate).** Wisdom gives 6 Golden great-grandparents out of 8; Embark gives 4, plus 2 Japanese Spitz. This follows from point 1. Embark's tree is internally consistent (4 of 8 ≈ its 52%); Wisdom's (6 of 8 = 75%) does not match its own 60%.
3. **Small breeds found only by Wisdom (low to moderate).** Chihuahua 5% and about 9% Asian breeds. Calls under about 5% are the least reliable in any panel, but some local village-dog ancestry is plausible for a dog born in Malaysia, and Embark has little reference data to match it against.
4. **Golden Retriever, 60% vs 52.1% (low).** Within the usual variation between companies.
5. **Shedding wording (trivial).** Same MC5R genotype, read as "occasional shedder" by Wisdom and "heavy/seasonal" by Embark.
6. **Saddle tan wording (none).** Same genotype; irrelevant because his dominant-black gene overrides the pattern.

## Agreements, ranked by strength

1. **No disease variants (very strong).** Wisdom found 0 at risk and 0 carrier out of 210 conditions; Embark found none out of 273. All 128 genes on both panels agree. Single-variant genotyping is far more reliable than breed estimation (Donner et al. 2018 and 2023, *PLoS Genetics*).
2. **Trait genotypes (very strong).** Identical at all 23 shared genes. His dominant-black result fits his name: "Kuro" means black.
3. **Genetic diversity (strong).** Wisdom gives heterozygosity of 48%, above the 33–46% typical for mixed breeds; Embark gives 0% inbreeding and high diversity at both immune-gene (MHC) regions.
4. **Miniature Pinscher about 8% and German Shepherd 4–6% (moderate to strong),** both on the Spitz side of the family.
5. **Size (consistent).** Predictions of 42–68 lb (Wisdom) and 51 lb (Embark) bracket his actual 21–23 kg.

**Caveats:**
- Health genes were matched by gene, not by exact variant. That is safe here because every result is clear.
- Agreement on "all clear" is weaker evidence than it looks. Most dogs are clear for most variants, so two tests agree by default. A chance-corrected statistic such as Cohen's kappa cannot be calculated when every result is the same.

## What it means for his health records

- **Embark tested three relevant things Wisdom did not:**
  - **Type I disc disease (CDDY, FGF4 retrogene on chromosome 12; Brown et al. 2017, *PNAS*):** clear. His back pain is unlikely to come from this inherited disc disease, which fits the vet's diagnosis of arthritis and nerve pain.
  - **Golden Retriever ichthyosis (PNPLA1; Grall et al. 2012, *Nature Genetics*):** clear. This common scaly-skin variant is an unlikely cause of his chronic skin problems.
  - **ALT activity variant:** clear. His ALT values in `labs.csv` can be read against standard ranges.
- **Neither test speaks to his splenic tumour, hip dysplasia or arthritis.** Goldens carry a high cancer burden (about 60% of deaths in breed surveys, with splenic hemangiosarcoma prominent), but that risk, like hip and joint disease, is spread across many genes rather than one testable variant.

*References are cited from general knowledge; check exact figures before quoting them.*
