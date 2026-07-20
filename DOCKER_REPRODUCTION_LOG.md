> **Current status:** Docker was not available in the original local verification environment described below. Docker build/run verification was subsequently completed successfully through GitHub Actions. See `DOCKER_TEST_STATUS.md` for the current release status.

# Docker Reproduction Log - Phase 3C

Original local verification date: 2026-06-29  
Artifact release version: `v0.3.6-mdpi-data-availability`  
Documentation last updated: 2026-07-20

## Local Non-Docker Verification

The following checks were performed in the original local execution environment because Docker was not installed:

```bash
bash scripts/smoke_test.sh
python -m pytest -q tests
python scripts/verify_phase3b_integrity.py
bash scripts/phase3c_ci_verify.sh
```

### Observed Outcomes

- Smoke test: passed
- Pytest: 3 tests passed
- Integrity check: passed
- `raw_results/experiment_runs.csv`: 750 retained rows
- Fixture coverage: 5 benchmark fixtures
- Algorithm coverage: 5 algorithms
- Seed coverage: 30 seeds per fixture/algorithm
- Duplicate `system,algorithm,seed` records: 0
- Required processed outputs: present
- Required Phase 3B PNG and PDF figures: present
- Complete figure-provenance manifest: 9 figures

## Docker Verification Result

Docker was not available in the original local execution environment; therefore, Docker build/run verification was not performed locally at that time.

Docker verification was subsequently completed successfully through the GitHub Actions Phase 3C Artifact Verification workflow. The workflow successfully:

- installed the required Python dependencies;
- executed the smoke and integrity checks;
- verified the retained raw and processed outputs;
- built the Docker image;
- ran the packaged artifact verification inside Docker;
- confirmed the presence of the required generated figures.

The Docker configuration and GitHub Actions workflow are available at:

- `docker/Dockerfile`
- `.github/workflows/artifact-ci.yml`

For the current Docker and CI verification status, see:

- `DOCKER_TEST_STATUS.md`

The verification evidence applies to the included local executable benchmark suite and does not represent external large-project runtime validation.
