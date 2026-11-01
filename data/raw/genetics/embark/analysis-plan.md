# Embark data — analysis plan

Ways to analyse Kuro's Embark DNA results, either to learn bioinformatics or to check Embark's report against the raw genotypes. Levels run from basic to advanced.

## What's in the export

| File | Contents |
|---|---|
| `embark-raw-data-kuro102/*.tped`, `*.tfam` | Raw genotypes in PLINK transposed format: **82,434 SNPs** on chromosomes 1–42 from an Illumina canine array (`BICF2…` marker IDs). 20 no-calls (99.98% call rate); 29,908 heterozygous (36%). |
| `Embark-full-results-data-*.csv` | 326 rows. **Breed mix:** Golden Retriever 52.1%, Japanese Spitz 33.8%, Miniature Pinscher 8.4%, German Shepherd 5.7%. **Lineage:** mtDNA haplogroup A1a, Y haplogroup A1a. **Genetic stats:** inbreeding 0.0042, predicted adult weight 51.47 lb. **Health:** 276 markers, all "clear" except *Immune Response 1/2 = 2*. **Traits:** 34 coat and body traits. |

## Level 1: data handling and quality checks

*Skills: PLINK basics, genotype file formats.*

1. **Convert and inspect.** `plink --tfile … --make-bed` for a binary fileset; `--recode vcf` for a VCF that `bcftools` can read. Compute call rate (`--missing`) and heterozygosity per chromosome.
2. **Map chromosome codes.** Work out what 39–42 represent (likely X, Y, PAR or mitochondrial, as is common in Embark-style exports).
3. **Identify the reference genome.** Look up a few known SNP positions (dbSNP or EVA) to tell whether positions use CanFam3.1 or a newer build. Everything later depends on matching builds; use liftOver if they differ.
4. **Confirm sex.** A male should show almost no heterozygosity on the non-pseudoautosomal X. A quick check of Embark's "Male".

## Level 2: confirm report items from the raw genotypes

*Skills: variant lookup, reading the literature, coordinate systems.*

5. **Coat traits.** Find the published causal variants in **OMIA** (Online Mendelian Inheritance in Animals): MC1R (E locus), CBD103 (K), ASIP (A), TYRP1 (B), MLPH (D), MITF (S), RSPO2 (furnishings), FGF5 (coat length), MC5R (shedding). Find the matching array SNPs or nearby markers in the `.tped` and check they agree with Embark's calls (e.g. `LhLh`, `KBKy`, `Aya`). Some variants will be on Embark's custom probes and missing from the raw export; identifying which is part of the exercise.
6. **Clinically relevant markers.** Re-confirm from the raw file where the probe is present:
   - **ABCB1 (MDR1):** clear — relevant for drug sensitivity.
   - **ALT activity (GPT) variant:** clear — his raised ALT was not caused by this known variant.
   - **Bleeding-disorder panel:** all clear (von Willebrand types I–III, hemophilia A and B, thrombopathia) — tested inherited clotting disorders don't explain his abdominal bleeding.
7. **Inbreeding.** Call runs of homozygosity (`plink --homozyg`, which works on a single dog), compute F_ROH and compare with Embark's 0.0042. Expect a difference because the methods differ; explaining it is the learning.
8. **Predicted vs actual weight.** Embark predicted 51.47 lb (23.3 kg); his recorded peak was 23.0 kg (Jun 2024). Compare with `data/processed/weights.csv`.

## Level 3: replicate the breed ancestry

*Skills: merging with a reference panel, PCA, ADMIXTURE — the classic population-genetics workflow.*

9. **Reference panel.** Get public dog genotypes on the same Illumina CanineHD array, e.g. Parker et al. 2017 (*Cell Reports*, ~160 breeds), Hayward et al. 2016 (*Nature Communications*) or Dreger et al. 2016. Match SNPs, fix strand and allele flips, prune for linkage (`--indep-pairwise`).
10. **PCA** (`plink --pca` or EIGENSOFT). See where Kuro falls between Golden Retriever, spitz-type, pinscher and German Shepherd clusters.
11. **Supervised ADMIXTURE** with those four breeds plus a few decoy breeds; compare the estimates with 52.1 / 33.8 / 8.4 / 5.7%. Japanese Spitz may be missing from public panels: substituting Samoyed or another spitz breed and watching the estimates shift shows how much reference choice drives ancestry results.

## Level 4: advanced

12. **Local ancestry ("chromosome painting")** with RFMix or similar, to reproduce Embark's chromosome-by-chromosome breed map.
13. **Haplogroups.** Place his mitochondrial and Y-chromosome calls on published dog phylogenies to check A1a / A1a.
14. **Connect to his medical history, as hypotheses only.**
    - Golden Retrievers have a very high rate of splenic hemangiosarcoma: relevant context, since he was half Golden and his splenic tumour type was never confirmed.
    - *Immune Response 1/2* relate to the dog leukocyte antigen (DLA) region. Look up what Embark says they mean, alongside the suspected immune-mediated anemia. One dog can't test an association.

## Making it reproducible

- Put the workflow in `scripts/embark/` or a small Snakemake pipeline, with tool versions pinned via conda.
- On Windows, PLINK, ADMIXTURE and bcftools are easiest through **WSL** or conda.
- Write outputs (QC table, trait concordance, ROH, ancestry comparison) as CSVs in `data/processed/`, with a methods note in `docs/`.
- The filenames, the `.tfam` line and the CSV contain the **Embark swab code**. Decide whether to keep or remove it before publishing the raw files.
