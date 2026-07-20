> **Current status:** The local environment described below did not have Docker. Docker build/run verification was subsequently completed successfully through GitHub Actions. See `DOCKER_TEST_STATUS.md` for the current release status.

# Docker Reproduction Log - Phase 3C

Original local verification date: 2026-06-29  
Artifact release version: `v0.3.6-mdpi-data-availability`  
Documentation last updated: 2026-07-20


## Local non-Docker verification performed here

The following checks were run in the available execution environment because Docker was not installed:

```bash
bash scripts/smoke_test.sh
python -m pytest -q tests
python scripts/verify_phase3b_integrity.py
bash scripts/phase3c_ci_verify.sh
```

Observed outcomes:

- smoke test: passed
- pytest: 3 passed
- integrity check: passed
- `experiment_runs.csv`: 750 rows
- fixture coverage: 5 fixtures
- algorithm coverage: 5 algorithms
- seed coverage: 30 seeds per fixture/algorithm
- duplicate `system,algorithm,seed` rows: 0
- required processed outputs present
- required Phase 3B PNG/PDF figures present

## Docker result

Docker was not available in this environment, so Docker build/run was not executed here. The Dockerfile and GitHub Actions workflow are included so that Docker verification can be performed locally or in CI before final journal submission.
