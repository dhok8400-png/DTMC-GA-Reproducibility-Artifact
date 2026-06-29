#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python scripts/run_benchmark_suite.py
python statistical_analysis/analyze_results.py --input raw_results/experiment_runs.csv --out processed_results
python statistical_analysis/validate_runtime.py --input raw_results/runtime_validation.csv --out processed_results
python statistical_analysis/validate_dtmc.py --input raw_results/dtmc_validation.csv --out processed_results
python statistical_analysis/validate_mq.py --input raw_results/mq_validation.csv --out processed_results
python scripts/make_figures.py --runs raw_results/experiment_runs.csv --out figures
python scripts/check_artifact.py
