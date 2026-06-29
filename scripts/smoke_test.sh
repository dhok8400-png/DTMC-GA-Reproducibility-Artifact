#!/usr/bin/env bash
set -euo pipefail

python scripts/check_artifact.py
python -m pytest -q tests
python statistical_analysis/analyze_results.py --input raw_results/experiment_runs.csv --out processed_results
python statistical_analysis/validate_runtime.py --input raw_results/runtime_validation.csv --out processed_results
python statistical_analysis/validate_dtmc.py --input raw_results/dtmc_validation.csv --out processed_results
python statistical_analysis/validate_mq.py --input raw_results/mq_validation.csv --out processed_results

echo "Phase 3C smoke test completed. Packaged benchmark-suite outputs and analysis scripts were checked; use scripts/run_benchmark_suite.sh for full regeneration."
