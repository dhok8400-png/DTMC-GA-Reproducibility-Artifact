#!/usr/bin/env bash
set -euo pipefail
python scripts/check_artifact.py
python statistical_analysis/analyze_results.py --input raw_results/experiment_runs.csv --out processed_results
python statistical_analysis/validate_runtime.py --input raw_results/runtime_validation.csv --out processed_results
python statistical_analysis/validate_dtmc.py --input raw_results/dtmc_validation.csv --out processed_results
python statistical_analysis/validate_mq.py --input raw_results/mq_validation.csv --out processed_results
