# DTMC-GA Modularization Reproducibility Artifact

## Artifact Availability and Verification Status

This repository contains the public Phase 3C/Phase 5A reproducibility artifact for the manuscript:

**“DTMC-GA-Based Modularization for Automated Parallelization of Sequential Software”**

* GitHub repository: https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact
* Zenodo DOI: 10.5281/zenodo.21045304
* GitHub release: `v0.3.5-phase3C-zenodo`
* Docker/CI verification status: **PASSED**

GitHub Actions successfully completed the Phase 3C Artifact Verification workflow, including Python smoke/integrity checks and Docker build/run verification.

The released artifact includes source code, benchmark fixtures, retained raw results, statistical scripts, generated figures, Docker configuration, and the GitHub Actions CI workflow.

**Important:** the quantitative evidence in this artifact is based on the local executable benchmark-suite with five fixtures and 750 retained runs. It is not presented as external large-project runtime evidence for Chromium, Firefox, MySQL, OpenCV, Unreal, Godot, or ITK. Those external large-project traces are left for future validation.

## Included Implementation Modules

* `src/parser/csv_reader.py`: normalized CSV benchmark reader.
* `src/cdg_builder/cdg.py`: weighted class-dependence graph preparation.
* `src/dtmc_analyzer/dtmc_matrix.py`: transition matrix, finite-horizon expected visits, and simulated visits.
* `src/call_use_displacement/`: safety-rule decision logic and safe call-use gap update.
* `src/det_calculator/det_model.py`: compact DET-inspired partition evaluator.
* `src/ga_optimizer/optimizer.py`: executable DTMC-GA and baseline optimizers.
* `src/validator/schema.py`: output schema checks.

## Local Executable Benchmark Suite

The `benchmarks/` folder contains five local CSV benchmark fixtures used for Phase 3B/Phase 3C generation. The original `demo_eight_class` fixture remains the smallest smoke-test fixture.

Each fixture contains CSV files such as:

* `classes.csv`
* `edges.csv`
* `safety.csv`

These benchmark fixtures are intended to test the full pipeline end-to-end. They are executable local benchmark-suite inputs, not third-party large-project checkouts.

## Raw Results

The retained raw results are stored in `raw_results/`.

The main experiment file is:

* `raw_results/experiment_runs.csv`

It contains:

* 5 benchmark fixtures
* 5 algorithms
* 30 independent seeds per fixture/algorithm
* 750 retained rows
* No best-run filtering

Additional validation and analysis files include:

* `raw_results/runtime_validation.csv`
* `raw_results/dtmc_validation.csv`
* `raw_results/mq_validation.csv`
* `raw_results/ablation_results.csv`
* `raw_results/sensitivity_results.csv`
* `raw_results/per_generation_logs.csv`

Processed outputs are stored in `processed_results/`.

Generated figures are stored in `figures/`.
## Minimal Dataset and Metadata

The repository contains the essential data needed to support and verify the central fixture-suite findings:

* retained run-level data and validation records in `raw_results/`
* processed summaries and statistical tests in `processed_results/`
* benchmark and workload metadata in `benchmarks/benchmark_metadata.csv` and `workloads/workload_metadata.csv`
* figure provenance in `raw_results/figure_manifest.csv`
* a human-readable guide in `DATA_DICTIONARY.md`
* a machine-readable variable dictionary in `DATA_DICTIONARY.csv`

The dataset contains no personally identifiable or confidential information. The `memory_mb` field is blank because memory usage was not collected for the retained runs; blank values must not be interpreted as zero.

Recommended Data Availability Statement:

> The minimal dataset supporting the central findings of this study, including benchmark fixtures, retained raw results, processed outputs, statistical analysis scripts, and figure-generation scripts, is publicly available in the GitHub reproducibility repository and archived on Zenodo.


## Run the Smoke Test

```bash
bash scripts/smoke_test.sh
```

## Run the Phase 3C Verification Script

```bash
bash scripts/phase3c_ci_verify.sh
```

This script checks the packaged artifact outputs, including raw result integrity, fixture/algorithm/seed coverage, duplicate detection, processed outputs, and generated figures.

## Run the Demo Experiment Pipeline

```bash
bash scripts/run_demo_experiments.sh
```

This regenerates the small demo benchmark outputs and writes results to `raw_results/`, `processed_results/`, and `figures/`.

## Run the Full Local Benchmark-Suite Pipeline

```bash
bash scripts/run_benchmark_suite.sh
```

This regenerates retained raw results for all five local benchmark fixtures.

## Docker Verification

The artifact includes a self-contained Dockerfile.

Build the Docker image:

```bash
docker build -f docker/Dockerfile -t dtmc-ga-artifact:phase3c .
```

Run the verification inside Docker:

```bash
docker run --rm dtmc-ga-artifact:phase3c
```

The GitHub Actions workflow already completed the Phase 3C Artifact Verification workflow successfully, including Docker build/run verification.

## GitHub Actions CI

The CI workflow is located at:

```text
.github/workflows/artifact-ci.yml
```

It performs:

* Python dependency installation
* smoke/integrity checks
* Phase 3C artifact verification
* Docker image build
* Docker-based packaged-output verification

## Reproducibility Scope

This artifact supports the reproducible evidence reported in the manuscript for the local executable benchmark-suite.

Included evidence:

* source code
* benchmark fixtures
* raw results
* processed results
* statistical scripts
* generated figures
* Docker configuration
* GitHub Actions CI workflow
* Zenodo archival DOI

Not included as final evidence:

* external Chromium runtime traces
* external Firefox runtime traces
* external MySQL runtime traces
* other full large-project runtime measurements

Those large-system studies are treated as future external validation.

## Citation

Please cite the associated manuscript and the archived reproducibility artifact.

Artifact DOI:

```text
10.5281/zenodo.21045304
```

GitHub repository:

```text
https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact
```
