# Raw Results

This folder contains the retained raw outputs used to support the local executable benchmark-suite findings reported in the manuscript.

The files were generated during the Phase 3B experimental work and are retained in the public Phase 3C/Phase 5A reproducibility artifact.

## Retained Dataset Files

- `experiment_runs.csv`: 750 retained runs = 5 benchmark fixtures × 5 algorithms × 30 independent seeds.
- `runtime_validation.csv`: predicted-versus-observed surrogate pipeline validation records generated from the executable fixture suite.
- `dtmc_validation.csv`: DTMC validation records for fixture-level transition and visit-count checks.
- `mq_validation.csv`: speedup-based MQ validation records.
- `ablation_results.csv`: retained ablation measurements for the executable fixture suite.
- `sensitivity_results.csv`: retained sensitivity measurements.
- `per_generation_logs.csv`: per-generation optimizer logs where available.
- `figure_manifest.csv`: provenance information linking generated figures to their source data and generation scripts.

## Dataset Interpretation

No best-run filtering is used. All seed-level runs are retained, and downstream descriptive statistics, statistical tests, tables, and figures should be regenerated from these raw files.

The `memory_mb` field is blank because memory usage was not collected for the retained runs. Blank values must not be interpreted as zero.

Definitions, formats, units, and interpretation guidance for dataset variables are provided in:

- `../DATA_DICTIONARY.md`
- `../DATA_DICTIONARY.csv`

Processed summaries and statistical outputs are available in:

- `../processed_results/`

Generated figures are available in:

- `../figures/`

## Privacy and Scope

The dataset contains no personally identifiable information, confidential records, patient information, account identifiers, or proprietary third-party project traces.

These files are not external Chromium, Firefox, MySQL, OpenCV, Unreal, Godot, or ITK runtime traces. They are locally generated, reproducible benchmark-fixture outputs used to validate the executable pipeline and statistical workflow.

External large-project traces, if added in future work, must be stored in a separate clearly named folder or release and must be explicitly distinguished from the current fixture-suite evidence.
