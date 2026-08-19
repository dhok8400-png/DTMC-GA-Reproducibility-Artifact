# DTMC-GA Modularization Reproducibility Artifact

## Artifact Availability and Verification Status

This repository contains the public Phase 3C/Phase 5A reproducibility artifact for the manuscript:

**“DTMC-GA-Based Modularization for Automated Parallelization of Sequential Software”**

* GitHub repository: https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact
* Zenodo archive: https://doi.org/10.5281/zenodo.21457470
* GitHub release: `v0.3.6-mdpi-data-availability`
* Docker/CI verification status: **PASSED**
* OpenCV 4.7.0 exact-source build validation: **PASSED**
* OpenCV 4.7.0 30-run sequential baseline: **PASSED**

GitHub Actions successfully completed the Phase 3C Artifact Verification workflow, including Python smoke/integrity checks and Docker build/run verification. Revision-time GitHub Actions also verified and built the exact OpenCV 4.7.0 source tree and executed a fixed DNN convolution workload under explicit sequential controls.

The artifact includes source code, benchmark fixtures, retained raw results, processed results, statistical scripts, generated figures, Docker configuration, GitHub Actions workflows, and revision-time OpenCV 4.7.0 execution evidence.

**Evidence boundary:** The central comparative results remain the five-fixture executable benchmark-suite study with 750 retained runs and model-derived performance indicators. In addition, the revision now includes direct real-project OpenCV 4.7.0 source/build/workload execution evidence and a measured sequential runtime reference. This OpenCV baseline is not, by itself, evidence of DTMC-GA optimized measured speedup, automatic production-C++ rewriting, byte-level communication volume, or production transformation safety.

## Executed OpenCV 4.7.0 Validation

The revision-time real-project validation uses the official OpenCV 4.7.0 source tree at commit:

`725e440d278aca07d35a5e8963ef990572b07316`

The fixed DNN convolution workload contains:

* `Conv.conv/0`
* `Conv.conv/2`
* `Conv.conv/28`
* `Conv.conv/42`
* `Conv.conv/69`

The clean Release baseline uses `--perf_threads=1`, `OPENCV_FOR_THREADS_NUM=1`, matching single-thread environment controls, and one-CPU process affinity where supported. After three untimed warm-up process runs, 30 independent timed process runs completed successfully.

Audited sequential baseline summary:

* successful timed runs: **30/30**
* mean: **4.491456572 s**
* median: **4.470818768 s**
* sample SD: **0.118431329 s**
* minimum: **4.430297497 s**
* maximum: **5.101106220 s**
* coefficient of variation: **2.6368%**

The baseline runner provenance records Ubuntu 22.04 on a GitHub-hosted Azure VM with an **AMD EPYC 7763** processor, 4 exposed logical CPUs, GCC/G++ 11.4.0, CMake 3.31.6, Ninja 1.13.2, and Python 3.10.12. The timed process itself is restricted to one CPU for the sequential reference.

The audited evidence is retained under:

`results/opencv470/sequential_baseline/`

A reviewer-response draft for the real-project execution comment is retained at:

`results/opencv470/R3C1_REVIEWER_RESPONSE_DRAFT.md`

Instrumented OpenCV profiling is a separate revision-time campaign. Its results are not treated as complete evidence until the profiling workflow and independent publisher/audit finish successfully.

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
* audited OpenCV baseline evidence in `results/opencv470/sequential_baseline/`
* a human-readable guide in `DATA_DICTIONARY.md`
* a machine-readable variable dictionary in `DATA_DICTIONARY.csv`

The dataset contains no personally identifiable, confidential, patient, account, or proprietary third-party information.

The `memory_mb` field in the retained fixture-suite run table is blank because memory usage was not collected for those retained runs. Blank values must not be interpreted as zero.

### Recommended Data Availability Statement

> The minimal dataset supporting the central findings of this study, including benchmark fixtures, retained raw results, processed outputs, statistical analysis scripts, figure-generation scripts, and revision-time audited OpenCV 4.7.0 baseline evidence, is publicly available in the GitHub reproducibility repository at https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact and the core archived artifact is available on Zenodo at https://doi.org/10.5281/zenodo.21457470.

## Run the Smoke Test

```bash
bash scripts/smoke_test.sh
```

## Run the Phase 3C Verification Script

```bash
bash scripts/phase3c_ci_verify.sh
```

This script checks the packaged artifact outputs, including raw-result integrity, fixture/algorithm/seed coverage, duplicate detection, processed outputs, and generated figures.

## Run the Demo Experiment Pipeline

```bash
bash scripts/run_demo_experiments.sh
```

This runs the small demonstration benchmark in an isolated temporary copy and writes demo-only outputs to `demo_outputs/`.

It does not modify the retained manuscript evidence in:

* `raw_results/`
* `processed_results/`
* `figures/`

The demo outputs are not the retained 750-run manuscript evidence.

## Run the Full Local Benchmark-Suite Pipeline

```bash
bash scripts/run_benchmark_suite.sh
```

This regenerates the retained raw results for all five local benchmark fixtures and preserves provenance records for all nine generated figures.

## Docker Verification

The artifact includes a self-contained Dockerfile.

Build the Docker image:

```bash
docker build -f docker/Dockerfile -t dtmc-ga-artifact:phase3c .
```

Run verification inside Docker:

```bash
docker run --rm dtmc-ga-artifact:phase3c
```

The GitHub Actions workflow successfully completed the Phase 3C Artifact Verification workflow, including Docker build/run verification.

## GitHub Actions CI

The repository contains the core artifact CI workflow and revision-time OpenCV validation workflows under `.github/workflows/`.

They cover:

* Python dependency installation
* smoke and integrity checks
* Phase 3C artifact verification
* Docker image build and packaged-output verification
* exact OpenCV 4.7.0 source identity checking
* clean and profiling-capable OpenCV DNN builds
* fixed-workload sequential runtime measurement
* revision-time instrumented profiling and independent evidence publishing

## Reproducibility Scope

This artifact supports the reproducible evidence reported in the manuscript for the local executable benchmark suite and the revision-time OpenCV 4.7.0 execution checkpoint.

### Included evidence

* source code
* benchmark fixtures
* retained raw results
* processed results
* statistical scripts
* generated figures
* figure-provenance documentation
* human-readable and machine-readable data dictionaries
* Docker configuration
* GitHub Actions CI workflows
* exact OpenCV 4.7.0 source/build provenance
* 30-run measured OpenCV sequential baseline and raw logs
* Zenodo archival record: `10.5281/zenodo.21457470`

### Not yet included as final evidence

* measured DTMC-GA optimized/parallel OpenCV runtime
* modeled-versus-measured OpenCV speedup error
* byte-level communication-volume measurements for OpenCV
* measured parallel overlap for OpenCV
* production OpenCV source-rewrite safety/equivalence evidence
* external Chromium runtime traces
* external Firefox runtime traces
* external MySQL runtime traces
* external Unreal runtime traces
* external Godot runtime traces
* external ITK runtime traces
* other full large-project optimized-runtime measurements

These stronger claims remain outside the current evidence until their dedicated execution and audit steps complete.

## Citation

Please cite the associated manuscript and the archived reproducibility artifact.

### Zenodo Archive

DOI: https://doi.org/10.5281/zenodo.21457470

### GitHub Repository

https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact
