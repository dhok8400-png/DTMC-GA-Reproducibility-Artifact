# Reproducibility and Minimal-Dataset Checklist

Last reviewed: 2026-07-20

## Public availability

- [x] Public GitHub repository is available.
- [x] A tagged GitHub release is available (`v0.3.5-phase3C-zenodo`).
- [x] A Zenodo archival DOI is provided (`10.5281/zenodo.21045304`).
- [x] The corrected manuscript Data Availability Statement identifies both the GitHub repository and Zenodo archive.
- [x] The corrected manuscript Code Availability Statement identifies both the GitHub repository and Zenodo archive.

## Minimal dataset

- [x] `raw_results/experiment_runs.csv` contains 750 retained runs: 5 fixtures x 5 algorithms x 30 seeds.
- [x] All seed-level runs are retained; no best-run filtering is used.
- [x] Runtime-surrogate validation records are included.
- [x] DTMC validation records are included.
- [x] MQ validation records are included.
- [x] Ablation records are included.
- [x] Sensitivity records are included.
- [x] Per-generation optimization logs are included where generated.
- [x] Benchmark and workload metadata are included.
- [x] A machine-readable and human-readable data dictionary is included.
- [x] Figure provenance is listed in `raw_results/figure_manifest.csv`.

## Reproducible analysis

- [x] Statistical scripts regenerate descriptive summaries and statistical tests.
- [x] Figure scripts regenerate the released figures.
- [x] Source code and configuration files are included.
- [x] Docker configuration is included.
- [x] GitHub Actions verification, including Docker build/run, has passed.
- [x] README reproduction commands are provided.
- [x] Integrity checks verify row counts, fixture/algorithm/seed coverage, duplicate absence, outputs, and figures.

## Privacy and scope

- [x] The dataset contains no names, email addresses, account identifiers, patient information, or other personally identifiable information.
- [x] The dataset contains no confidential third-party project traces.
- [x] The evidence is explicitly limited to the included local executable fixture suite.
- [x] The artifact does not claim external large-project runtime validation.
- [x] Blank `memory_mb` values are documented as “not collected,” rather than interpreted as zero.

## Before sending the editor response

- [ ] Upload all documentation corrections to the public GitHub repository.
- [ ] Create a new GitHub release for the corrected artifact.
- [ ] Update the Zenodo record with the corrected artifact package.
- [ ] If Zenodo assigns a new version-specific DOI, replace the DOI in `CITATION.cff`, `README.md`, and the manuscript before submission.
- [ ] Confirm that the final public and archived packages match the manuscript statement exactly.
