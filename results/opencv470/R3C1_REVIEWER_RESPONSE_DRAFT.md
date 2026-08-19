# Reviewer 3, Comment 1 — Evidence-backed response

## Status

**COMPLETE in the revision checking manuscript: executed evidence + manuscript integration.**

This response is based only on the executed OpenCV 4.7.0 source/build/workload validation and the independently audited 30-run sequential baseline. It does not claim optimized measured speedup, byte-level communication volume, parallel overlap, or production source transformation; those belong to the remaining R1 C2, R1 C4, and R3 C3 work.

## Proposed final response to Reviewer 3, Comment 1

**Response:** We thank the reviewer for requesting validation on a real-world software system. We have extended the revision-time evaluation to the official OpenCV 4.7.0 source tree at exact commit `725e440d278aca07d35a5e8963ef990572b07316`. The real-project checkpoint targets the OpenCV DNN convolution performance suite and uses a fixed workload from `modules/dnn/perf/perf_convolution.cpp`: `Conv.conv/0`, `Conv.conv/2`, `Conv.conv/28`, `Conv.conv/42`, and `Conv.conv/69`. The exact source identity was verified before compilation, and the DNN performance target was built successfully from source.

To establish a measured real-project sequential reference, we used a clean Release build with explicit sequential controls (`--perf_threads=1`, `OPENCV_FOR_THREADS_NUM=1`, one-thread controls for the numerical backends, and one-CPU process affinity where supported). After three untimed warm-up process runs, we executed 30 independent timed process runs of the same fixed workload. All 30 timed runs completed successfully with exit code 0. The independently recomputed mean sequential runtime was **4.491456572 s** (median **4.470818768 s**, sample SD **0.118431329 s**, range **4.430297497–5.101106220 s**, CV **2.6368%**).

The baseline runner provenance records Ubuntu 22.04 on a GitHub-hosted Azure VM exposing four logical CPUs from an **AMD EPYC 7763** processor, with GCC/G++ 11.4.0, CMake 3.31.6, Ninja 1.13.2, and Python 3.10.12; the timed benchmark process itself was restricted to one CPU. The raw 30-run CSV, per-run logs, workload manifest, exact source hashes, build provenance, and independent audit are retained under `results/opencv470/sequential_baseline/` in the public reproducibility repository.

The manuscript has been synchronized accordingly: the Introduction evidence boundary, Experimental Design claim-validation table, a new Results subsection titled **“OpenCV 4.7.0 Real-Project Sequential Runtime Checkpoint,”** the Discussion/future-work boundary, Conclusion, Data Availability, and Code Availability now report this executed evidence. The interpretation remains deliberately bounded. This checkpoint establishes direct OpenCV source/build/workload execution and a measured sequential reference; it is not used to infer measured DTMC-GA optimized speedup or automatic production-C++ rewriting. Those stronger claims require the matched profiling, optimized-execution, and transformation-safety steps that remain separately tracked.

## Evidence record

- Exact OpenCV commit: `725e440d278aca07d35a5e8963ef990572b07316`
- Fixed DNN workload: `Conv.conv/0`, `Conv.conv/2`, `Conv.conv/28`, `Conv.conv/42`, `Conv.conv/69`
- Warm-ups: 3
- Timed runs: 30
- Successful timed runs: 30/30
- Mean: 4.491456572 s
- Median: 4.470818768 s
- Sample SD: 0.118431329 s
- Minimum: 4.430297497 s
- Maximum: 5.101106220 s
- CV: 2.6368%
- Baseline CSV SHA-256: `321deb95d357e275a02aad689ff708d040f7980a51b1072bbe2bd1c66e73a4f4`
- Baseline CPU provenance: AMD EPYC 7763; four exposed logical CPUs; measured process restricted to one CPU

## Remaining boundary

- **R3 C1: Completed** in the revision checking manuscript.
- **R1 C2: Partial** — requires empirical profiling input, selected optimized execution, matched 30-run optimized runtime, measured speedup, and modeled-versus-measured prediction error.
- **R1 C4: Partial** — requires completion and audit of real profiling-derived timing/call/interaction evidence, with no unmeasured communication/overlap quantities inferred.
- **R3 C3: Partial** — requires real-project production-C++ transformation-safety evidence.
