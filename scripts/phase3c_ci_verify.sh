#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python scripts/check_artifact.py
python -m pytest -q tests
python scripts/verify_phase3b_integrity.py
python statistical_analysis/analyze_results.py --input raw_results/experiment_runs.csv --out processed_results
python statistical_analysis/validate_runtime.py --input raw_results/runtime_validation.csv --out processed_results
python statistical_analysis/validate_dtmc.py --input raw_results/dtmc_validation.csv --out processed_results
python statistical_analysis/validate_mq.py --input raw_results/mq_validation.csv --out processed_results
python scripts/verify_phase3b_integrity.py

echo "Phase 3C CI verification completed. This verifies the packaged Phase 3B benchmark-suite outputs without regenerating the full suite. Use scripts/run_benchmark_suite.sh for full regeneration."
