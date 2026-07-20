# Reproducibility and Minimal-Dataset Checklist

Last reviewed: 2026-07-20

## Public Availability

- [x] The public GitHub repository is available.
- [x] Documentation corrections have been uploaded to the `main` branch.
- [x] The artifact was prepared for release as `v0.3.6-mdpi-data-availability`.
- [x] The `v0.3.6-mdpi-data-availability` GitHub release has been published.
- [x] Zenodo successfully archived the new GitHub release.
- [x] Zenodo assigned the version-specific DOI `10.5281/zenodo.21457470`.
- [x] The new Zenodo DOI has been added to `CITATION.cff`.
- [x] The new Zenodo DOI has been added to `README.md`.
- [ ] The new Zenodo DOI has been added to the final manuscript.
- [ ] The final Data Availability Statement identifies both the GitHub repository and the new Zenodo archive.
- [ ] The final Code Availability Statement identifies both the GitHub repository and the new Zenodo archive.

## Minimal Dataset

- [x] `raw_results/experiment_runs.csv` contains 750 retained runs: 5 fixtures × 5 algorithms × 30 seeds.
- [x] All seed-level runs are retained; no best-run filtering is used.
- [x] Runtime-surrogate validation records are included.
- [x] DTMC validation records are included.
- [x] MQ validation records are included.
- [x] Ablation records are included.
- [x] Sensitivity records are included.
- [x] Per-generation optimization logs are included where generated.
- [x] Benchmark and workload metadata are included.
- [x] Human-readable and machine-readable data dictionaries are included.
- [x] Variables in `processed_results/module_assignments.csv` are documented.
- [x] Provenance for all nine generated figures is listed in `raw_results/figure_manifest.csv`.

## Reproducible Analysis

- [x] Statistical scripts regenerate descriptive summaries and statistical tests.
- [x] Figure scripts regenerate the released figures.
- [x] Full benchmark-suite regeneration preserves all nine figure-provenance records.
- [x] Phase 3A demo outputs are generated separately in `demo_outputs/`.
- [x] Running the demo script does not overwrite the retained manuscript evidence.
- [x] Source code and configuration files are included.
- [x] Docker configuration is included.
- [x] GitHub Actions verification, including Docker build/run, has passed.
- [x] README reproduction commands are provided.
- [x] Integrity checks verify row counts, fixture/algorithm/seed coverage, duplicate absence, outputs, and figures.

## Privacy and Scope

- [x] The dataset contains no names, email addresses, account identifiers, patient information, or other personally identifiable information.
- [x] The dataset contains no confidential or proprietary third-party project traces.
- [x] The evidence is explicitly limited to the included local executable fixture suite.
- [x] The artifact does not claim external large-project runtime validation.
- [x] Blank `memory_mb` values are documented as “not collected” and are not interpreted as zero.

## Published Records

- [x] GitHub release: `v0.3.6-mdpi-data-availability`.
- [x] Zenodo version-specific DOI: `10.5281/zenodo.21457470`.
- [x] Previous Zenodo version DOI: `10.5281/zenodo.21045304`.
- [x] Concept DOI covering all Zenodo versions: `10.5281/zenodo.21045303`.
- [x] The GitHub repository and Zenodo record are publicly accessible.
- [x] The Zenodo record is published as open-access software.

## Before Sending the Editor Response

- [x] Upload all source-code, metadata, documentation, and minimal-dataset corrections to the public GitHub repository.
- [x] Confirm that GitHub Actions passes after the final documentation and code changes.
- [x] Publish the `v0.3.6-mdpi-data-availability` GitHub release.
- [x] Confirm that Zenodo successfully archives the new release.
- [x] Record the new version-specific Zenodo DOI.
- [x] Add the new DOI to `CITATION.cff` and `README.md`.
- [ ] Add the new DOI to the final manuscript.
- [ ] Update the manuscript Data Availability Statement.
- [ ] Update the manuscript Code Availability Statement.
- [ ] Confirm whether a metadata-only follow-up release is needed so the archived release snapshot itself contains the assigned DOI.
- [ ] Confirm that the final GitHub repository, Zenodo archive, and manuscript statements are consistent.
- [ ] Send the corrected Data Availability response to the MDPI editor.
