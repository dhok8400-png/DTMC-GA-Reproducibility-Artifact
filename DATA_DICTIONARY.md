# Data Dictionary and Minimal-Dataset Guide

This document describes the files and variables needed to interpret and reproduce the central findings reported for the local executable benchmark-suite. A machine-readable variable dictionary is provided in `DATA_DICTIONARY.csv`.

## Scope and interpretation

- The primary evidence consists of five included CSV benchmark fixtures, five algorithms, and 30 retained seeds per fixture/algorithm (750 run-level records).
- All seed-level runs are retained; no best-run filtering is used.
- Runtime values labeled as surrogate/model validation are generated for pipeline-regression checks and are not external wall-clock measurements from Chromium, Firefox, MySQL, or other large projects.
- The artifact contains no personally identifiable, confidential, patient, or proprietary third-party data.
- `memory_mb` is blank because memory usage was not collected for the retained runs. Blank values must not be treated as zero.

## File inventory

| File | Rows | Role |
|---|---:|---|
| `raw_results/experiment_runs.csv` | 750 | Primary retained run-level data supporting aggregate result tables. |
| `raw_results/runtime_validation.csv` | 750 | Predicted-versus-surrogate validation records. |
| `raw_results/dtmc_validation.csv` | 80 | DTMC expected-versus-simulated visit and call-frequency validation. |
| `raw_results/mq_validation.csv` | 750 | MQ and surrogate-speedup validation data. |
| `raw_results/ablation_results.csv` | 1050 | Ablation study records. |
| `raw_results/sensitivity_results.csv` | 600 | Parameter-sensitivity records. |
| `raw_results/per_generation_logs.csv` | 2400 | Generation-level optimization logs. |
| `raw_results/figure_manifest.csv` | 9 | Figure provenance and regeneration mapping. |
| `benchmarks/benchmark_metadata.csv` | 5 | Benchmark fixture metadata. |
| `workloads/workload_metadata.csv` | 5 | Workload metadata. |
| `processed_results/summary_statistics.csv` | 125 | Descriptive summaries regenerated from retained runs. |
| `processed_results/statistical_tests.csv` | 55 | Friedman and Bonferroni-adjusted Wilcoxon results. |
| `processed_results/module_assignments.csv` | 12000 | Class-to-module assignments used for auditing and representative figures. |

## Variable definitions

Complete variable-level definitions, data types, units, and allowed-value notes are stored in:

- `DATA_DICTIONARY.csv`

## Reproduction map

- Raw results: `raw_results/`
- Processed tables and metrics: `processed_results/`
- Statistical analysis: `statistical_analysis/analyze_results.py`
- Figure generation: `scripts/make_figures.py`
- Figure provenance: `raw_results/figure_manifest.csv`
- Full benchmark-suite regeneration: `bash scripts/run_benchmark_suite.sh`
- Integrity and packaged-output verification: `bash scripts/phase3c_ci_verify.sh`
- Docker verification: commands in the repository `README.md`

## Relationship to the manuscript

The manuscript’s Data Availability Statement should describe this dataset as publicly available through the GitHub repository and the Zenodo archive. “Available on request” is not an accurate description of the current public artifact.
