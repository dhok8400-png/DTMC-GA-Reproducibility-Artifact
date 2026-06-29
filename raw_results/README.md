# Raw Results

This folder contains the retained raw outputs for the Phase 3B local executable benchmark-suite evidence.

Current Phase 3B retained data:

- `experiment_runs.csv`: 750 retained runs = 5 benchmark fixtures x 5 algorithms x 30 seeds.
- `runtime_validation.csv`: predicted-versus-observed surrogate pipeline validation records generated from the executable fixture suite.
- `dtmc_validation.csv`: DTMC validation records for fixture-level transition/visit-count checks.
- `mq_validation.csv`: speedup-based MQ validation records.
- `ablation_results.csv`: retained ablation measurements for the executable suite.
- `sensitivity_results.csv`: retained sensitivity measurements.
- `per_generation_logs.csv`: per-generation optimizer logs where available.
- `figure_manifest.csv`: figure provenance for regenerated Phase 3B figures.

These files are not external Chromium/Firefox/MySQL traces. They are local reproducible benchmark-fixture outputs used to validate the executable pipeline and statistical workflow. External large-project traces, if added later, should be stored in a separate clearly named folder or release and must be distinguished from the Phase 3B fixture-suite evidence.

No best-run filtering is used: all seed-level runs are retained and downstream statistics must be regenerated from these raw files.
