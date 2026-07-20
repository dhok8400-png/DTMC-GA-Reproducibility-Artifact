# Docker Test Status

Artifact release version: `v0.3.6-mdpi-data-availability`  
Docker/CI verification status: **PASSED**  
Last verified: 2026-07-20

GitHub Actions successfully completed the Phase 3C Artifact Verification workflow on the `main` branch.

The successful verification included:

- Python dependency installation
- Smoke-test execution
- Automated test execution
- Raw-result integrity verification
- Verification of 750 retained experiment runs
- Coverage of 5 benchmark fixtures
- Coverage of 5 algorithms
- Coverage of 30 independent seeds per fixture/algorithm
- Confirmation of zero duplicate `system,algorithm,seed` records
- Verification of required processed outputs
- Verification of all nine generated figures
- Docker image build
- Packaged artifact verification inside Docker

## Repository

https://github.com/dhok8400-png/DTMC-GA-Reproducibility-Artifact

## Zenodo Archival Status

The previous archived release, `v0.3.5-phase3C-zenodo`, is available at:

- DOI: `10.5281/zenodo.21045304`

The current release, `v0.3.6-mdpi-data-availability`, has not yet been published and archived by Zenodo.

Its version-specific Zenodo DOI will be added after the GitHub release is published and successfully archived.

## Scope

The verification applies to the included local executable benchmark suite and the retained 750-run dataset.

It does not represent external large-project runtime validation for Chromium, Firefox, MySQL, OpenCV, Unreal, Godot, or ITK.
