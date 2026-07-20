#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEMO_OUTPUT_DIR="${DEMO_OUTPUT_DIR:-${ROOT_DIR}/demo_outputs}"

TEMP_DIR="$(mktemp -d)"
WORK_REPO="${TEMP_DIR}/repo"

cleanup() {
    rm -rf "${TEMP_DIR}"
}

trap cleanup EXIT

# Prevent accidental deletion of an unsafe directory.
if [[ -z "${DEMO_OUTPUT_DIR}" || "${DEMO_OUTPUT_DIR}" == "/" || "${DEMO_OUTPUT_DIR}" == "${ROOT_DIR}" ]]; then
    echo "ERROR: Unsafe DEMO_OUTPUT_DIR: ${DEMO_OUTPUT_DIR}"
    exit 1
fi

echo "Running the Phase 3A demo in an isolated temporary copy."
echo "The retained manuscript evidence in raw_results/, processed_results/, and figures/ will not be modified."

mkdir -p "${WORK_REPO}"

# Copy the repository into a temporary working directory.
# Existing demo outputs and temporary Python files are excluded.
tar -C "${ROOT_DIR}" \
    --exclude='.git' \
    --exclude='demo_outputs' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    -cf - . | tar -C "${WORK_REPO}" -xf -

cd "${WORK_REPO}"

# Start with clean output folders inside the isolated temporary copy.
rm -rf raw_results processed_results figures
mkdir -p raw_results processed_results figures

# Generate the Phase 3A demo dataset.
python scripts/run_demo_pipeline.py \
    --benchmark benchmarks/demo_eight_class \
    --out raw_results \
    --seeds configs/seeds_30.txt

# Validate the isolated demo artifact.
python scripts/check_artifact.py

# Generate demo-only statistical outputs.
python statistical_analysis/analyze_results.py \
    --input raw_results/experiment_runs.csv \
    --out processed_results

python statistical_analysis/validate_runtime.py \
    --input raw_results/runtime_validation.csv \
    --out processed_results

python statistical_analysis/validate_dtmc.py \
    --input raw_results/dtmc_validation.csv \
    --out processed_results

python statistical_analysis/validate_mq.py \
    --input raw_results/mq_validation.csv \
    --out processed_results

# Generate demo-only figures.
python scripts/make_figures.py \
    --runs raw_results/experiment_runs.csv \
    --out figures

# Copy only the completed demo outputs back to a separate folder.
rm -rf "${DEMO_OUTPUT_DIR}"
mkdir -p "${DEMO_OUTPUT_DIR}"

cp -a raw_results "${DEMO_OUTPUT_DIR}/raw_results"
cp -a processed_results "${DEMO_OUTPUT_DIR}/processed_results"
cp -a figures "${DEMO_OUTPUT_DIR}/figures"

cat > "${DEMO_OUTPUT_DIR}/README.md" <<'README'
# Phase 3A Demo Outputs

These outputs were generated from the small `demo_eight_class` fixture in an isolated temporary copy of the repository.

They are demo-only and are not the retained 750-run manuscript evidence.

The authoritative manuscript evidence remains in the repository-level:

- `raw_results/`
- `processed_results/`
- `figures/`

Running the demo script does not modify those authoritative directories.
README

echo "Phase 3A demo experiments completed safely."
echo "Demo-only outputs: ${DEMO_OUTPUT_DIR}"
echo "The retained manuscript evidence was not modified."
