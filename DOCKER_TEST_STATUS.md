# Docker/CI Test Status - Phase 3C

Phase 3C prepares the artifact for Docker and CI verification. The Dockerfile is now self-contained: it copies the artifact into the image and runs `scripts/phase3c_ci_verify.sh` by default.

## Status in this ChatGPT execution environment

Docker is **not available** in this execution environment (`docker: command not found`), so a real Docker build/run could not be executed here.

Non-Docker equivalent checks were executed successfully in the current container:

- `bash scripts/smoke_test.sh`: passed
- `python -m pytest -q tests`: 3 passed
- `python scripts/verify_phase3b_integrity.py`: passed
- `bash scripts/phase3c_ci_verify.sh`: passed

These checks verify the packaged Phase 3B benchmark-suite outputs without rebuilding the Docker image.

## Required local Docker verification

Run these commands from the artifact root on a Docker-enabled machine:

```bash
docker build -f docker/Dockerfile -t dtmc-ga-artifact:phase3c .
docker run --rm dtmc-ga-artifact:phase3c
```

Expected result:

```text
Phase 3C integrity check passed: 750 rows, full 5x5x30 coverage, no duplicates, required outputs/figures present.
Phase 3C CI verification completed.
```

## Optional full regeneration inside Docker

Full regeneration may take longer than the lightweight CI check:

```bash
docker run --rm dtmc-ga-artifact:phase3c bash scripts/run_benchmark_suite.sh
```

Expected retained raw results after full regeneration:

- `raw_results/experiment_runs.csv`: 750 rows
- coverage: 5 fixtures x 5 algorithms x 30 seeds
- duplicate `system,algorithm,seed` rows: 0
- processed statistics regenerated in `processed_results/`
- figures regenerated in `figures/`

## GitHub Actions

A workflow is included at `.github/workflows/artifact-ci.yml` with two jobs:

1. Python smoke and integrity checks.
2. Docker build and packaged-output verification.

Docker verification remains **pending** until this workflow passes in a public/private repository or the local Docker commands above are run successfully.
