# DTMC-GA Modularization Reproducibility Artifact

## Artifact Availability

GitHub repository: https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact

Zenodo DOI: 10.5281/zenodo.21045304
This artifact is a **Phase 3C CI-ready executable benchmark-suite pipeline** for the manuscript
"DTMC-GA-Based Modularization for Automated Parallelization of Sequential Software".

Phase 3C preserves the Phase 3B executable benchmark suite and adds Docker/CI verification readiness: it includes a local executable benchmark suite with five CSV fixtures, retained 30-seed runs per algorithm/fixture, executable Python modules for CSV input, CDG construction, DTMC analysis, conservative call-use displacement, DET-inspired partition evaluation, GA/baseline optimization, validation helpers, statistical analysis, and figure generation.

**Important:** the generated Phase 3B executable benchmark-suite results are local fixture-based outputs from the artifact benchmark suite.
They are not final evidence for the manuscript's large-system performance claims. The artifact is publicly available through the GitHub repository and archived on Zenodo using the DOI listed above. The current evidence is based on the local executable benchmark-suite, not external large-project runtime traces.

## Included implementation modules

- `src/parser/csv_reader.py`: normalized CSV benchmark reader.
- `src/cdg_builder/cdg.py`: weighted CDG preparation.
- `src/dtmc_analyzer/dtmc_matrix.py`: transition matrix, finite-horizon expected visits, simulated visits.
- `src/call_use_displacement/`: safety-rule decision and safe tgap update.
- `src/det_calculator/det_model.py`: compact DET-inspired partition evaluator.
- `src/ga_optimizer/optimizer.py`: executable DTMC-GA and baseline optimizers.
- `src/validator/schema.py`: output schema checks.

## Local executable benchmark suite

The `benchmarks/` folder contains five local CSV fixtures used for Phase 3B generation. The original `demo_eight_class` fixture remains as the smallest smoke-test fixture:

- `classes.csv`
- `edges.csv`
- `safety.csv`

This benchmark is intended to test the pipeline end-to-end. It is not a substitute for real Chromium,
Firefox, MySQL, OpenCV, Unreal, Godot, or ITK experiments.

## Run Phase 3B executable benchmark-suite demo experiments

```bash
bash scripts/run_demo_experiments.sh
```

This writes demo rows to:

- `raw_results/experiment_runs.csv`
- `raw_results/runtime_validation.csv`
- `raw_results/dtmc_validation.csv`
- `raw_results/mq_validation.csv`
- `raw_results/ablation_results.csv`
- `raw_results/sensitivity_results.csv`
- `raw_results/per_generation_logs.csv`

It also writes analysis outputs to `processed_results/` and a demo figure to `figures/`.

## Smoke test

```bash
bash scripts/smoke_test.sh
```

## Docker and CI verification

Phase 3C adds a self-contained Dockerfile and GitHub Actions workflow for reproducibility checks.

Build and run the packaged-output verification:

```bash
docker build -f docker/Dockerfile -t dtmc-ga-artifact:phase3c .
docker run --rm dtmc-ga-artifact:phase3c
```

Run the same verification without Docker:

```bash
bash scripts/phase3c_ci_verify.sh
```

Run full benchmark-suite regeneration when more time is available:

```bash
bash scripts/run_benchmark_suite.sh
# or, after building the image:
docker run --rm dtmc-ga-artifact:phase3c bash scripts/run_benchmark_suite.sh
```

The ChatGPT execution environment used to prepare this package did not provide a Docker daemon; therefore Docker build/run must still be verified locally or in CI before final submission. The included `.github/workflows/artifact-ci.yml` workflow runs both Python integrity checks and Docker image verification.

## Final submission requirements still pending

Before journal submission:

1. Replace the demo benchmark with final real benchmark traces.
2. Run all algorithms for 30 independent seeds per system.
3. Regenerate all statistical outputs and figures from final raw data.
4. Replace provisional manuscript values with final artifact-generated values.
5. Publish the repository, create a release, archive it on Zenodo, and insert the DOI.


## Phase 3B benchmark-suite raw results

Run the full included benchmark-suite pipeline with:

```bash
bash scripts/run_benchmark_suite.sh
```

This generates retained raw results for all local CSV benchmark fixtures in `raw_results/`:

- `experiment_runs.csv` (5 benchmark fixtures × 5 algorithms × 30 seeds = 750 retained rows)
- `per_generation_logs.csv`
- `runtime_validation.csv`
- `dtmc_validation.csv`
- `mq_validation.csv`
- `ablation_results.csv`
- `sensitivity_results.csv`

The Phase 3B benchmark fixtures are real executable artifact inputs, but they are not third-party large-project checkouts. They should be reported as benchmark-suite evidence and not as final Chromium/Firefox/MySQL runtime evidence.

## Phase 3C verification additions

Phase 3C adds:

- `scripts/verify_phase3b_integrity.py` for row-count, coverage, duplicate, output, and figure checks.
- `scripts/phase3c_ci_verify.sh` for lightweight local/CI verification of the packaged outputs.
- `.github/workflows/artifact-ci.yml` for GitHub Actions Python and Docker verification.
- A self-contained `docker/Dockerfile` that copies the artifact into the image and runs the Phase 3C CI verification script by default.
- `DOCKER_REPRODUCTION_LOG.md` documenting the non-Docker checks completed in the current environment and the Docker verification still pending.

Phase 3C does not add manuscript tables or figures; page count is intentionally preserved.
