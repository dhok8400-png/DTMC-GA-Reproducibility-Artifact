#!/usr/bin/env bash
set -euo pipefail
rm -f processed_results/*_not_run.md processed_results/analysis_manifest.json processed_results/summary_statistics.csv processed_results/statistical_tests.csv processed_results/runtime_validation_metrics.json processed_results/dtmc_validation_metrics.csv processed_results/mq_validation_metrics.csv figures/speedup_by_algorithm.png
python scripts/run_demo_pipeline.py --benchmark benchmarks/demo_eight_class --out raw_results --seeds configs/seeds_30.txt
python scripts/check_artifact.py
python statistical_analysis/analyze_results.py --input raw_results/experiment_runs.csv --out processed_results
python statistical_analysis/validate_runtime.py --input raw_results/runtime_validation.csv --out processed_results
python statistical_analysis/validate_dtmc.py --input raw_results/dtmc_validation.csv --out processed_results
python statistical_analysis/validate_mq.py --input raw_results/mq_validation.csv --out processed_results
python scripts/make_figures.py --runs raw_results/experiment_runs.csv --out figures
echo "Phase 3A demo experiments completed. Outputs are demo-only and not final manuscript evidence."
