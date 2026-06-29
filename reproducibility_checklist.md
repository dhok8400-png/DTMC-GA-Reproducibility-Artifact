# Reproducibility Checklist

## Required before final journal submission

- [ ] Public GitHub/GitLab repository created.
- [ ] Release tag created, e.g., `v1.0-submission`.
- [ ] Zenodo DOI created and inserted into the manuscript.
- [ ] `raw_results/experiment_runs.csv` contains all 30 runs per stochastic method.
- [ ] No best-run filtering is used.
- [ ] Hardware, OS, compiler, build flags, and profiler are documented.
- [ ] Benchmark metadata table is complete.
- [ ] Workload metadata table is complete.
- [ ] Runtime validation compares predicted and measured speedup.
- [ ] DTMC validation compares static/dynamic call frequencies and visit counts.
- [ ] MQ validation compares MQ with measured speedup and traditional metrics.
- [ ] Ablation results include all planned method variants.
- [ ] Sensitivity results include latency, bandwidth, module count, GA parameters, and workload profiles.
- [ ] Statistical scripts regenerate all result tables.
- [ ] Figure scripts regenerate all figures.
- [ ] Docker image builds successfully.
- [ ] README reproduction instructions tested on a clean machine.
- [ ] Manuscript captions no longer mark final values as provisional.


## Phase 3B benchmark-suite reproducibility checklist

- [x] README paths synchronized with actual `raw_results/` layout.
- [x] Invalid placeholder repository/DOI fields removed from CITATION.cff; public repository URL and Zenodo DOI remain pending until archival.
- [x] Schema-only analysis scripts produce explicit not-run reports instead of failing.
- [x] `scripts/smoke_test.sh` added for local/CI smoke checks.
- [x] Dockerfile retained with explicit local/CI verification commands.
- [ ] Docker build/run verified on a machine with Docker available.
- [ ] Final raw results added and all provisional manuscript values regenerated.


## Phase 3B checks

- [x] Local benchmark-suite fixtures are included under `benchmarks/`.
- [x] `scripts/run_benchmark_suite.sh` regenerates raw results for all included fixtures.
- [x] Raw results retain all 30 seeds for every stochastic algorithm; no best-run filtering is used.
- [x] Statistical summaries and tests are regenerated from raw CSV files.
- [x] Full-quality PNG/PDF figures are regenerated from raw results.
- [ ] Docker build/run must be verified on a local machine or CI runner before final submission.
- [ ] Final large third-party project results must replace fixture-only evidence before making industrial benchmark claims.
- [ ] GitHub URL and Zenodo DOI must be inserted before submission.


## Phase 3B-hotfix checks

- [x] README wording updated from demo-only/eight-class language to local executable benchmark-suite language.
- [x] `scripts/smoke_test.sh` completion message updated to Phase 3B.
- [x] `CITATION.cff` version updated to `0.3.1-phase3B-hotfix`.
- [x] Invalid placeholder repository/DOI fields removed from `CITATION.cff`; final public URL and Zenodo DOI remain pending.
- [x] No new manuscript tables or figures were added during this hotfix, keeping the PDF page count suitable for journal submission.


## Phase 3B-hotfix3 consistency checks

- [x] `CITATION.cff` version and message updated to `0.3.3-phase3B-hotfix3`.
- [x] `DOCKER_TEST_STATUS.md` heading and note updated to Phase 3B-hotfix3.
- [x] No manuscript tables or figures were added in this consistency hotfix; page count is preserved.
- [x] Raw results remain unchanged: 750 retained rows = 5 fixtures x 5 algorithms x 30 seeds.
- [ ] Docker build/run remains pending until tested on a Docker-enabled local machine or CI runner.

## Phase 3C Docker/CI readiness checks

- [x] Self-contained Dockerfile added; the artifact is copied into the image at build time.
- [x] Docker default command runs `scripts/phase3c_ci_verify.sh`.
- [x] `.dockerignore` added to keep image build context clean.
- [x] GitHub Actions workflow added at `.github/workflows/artifact-ci.yml`.
- [x] `scripts/verify_phase3b_integrity.py` added for row-count, fixture/algorithm/seed coverage, duplicate, output, and figure checks.
- [x] `scripts/phase3c_ci_verify.sh` added for lightweight local/CI verification.
- [x] Non-Docker equivalent checks passed in the current environment.
- [x] `DOCKER_REPRODUCTION_LOG.md` added.
- [ ] Docker build/run remains pending until tested on a Docker-enabled local machine or CI runner.
- [ ] GitHub Actions workflow must pass after the repository is published.
- [ ] Zenodo DOI must be inserted after repository archival.

Historical note: earlier Phase 3B-hotfix checklist entries refer to intermediate artifact versions such as `0.3.1-phase3B-hotfix`. The current Phase 3C artifact version is recorded in `CITATION.cff` as `0.3.4-phase3C-ci-ready`.
