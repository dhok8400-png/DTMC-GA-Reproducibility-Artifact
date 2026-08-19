# Reviewer 3, Comment 1 — Evidence-backed response draft

## Status

**Experimental evidence: COMPLETE / manuscript integration pending.**

This response is based only on the executed OpenCV 4.7.0 validation and the independently audited 30-run sequential baseline. It does not claim optimized measured speedup, byte-level communication volume, or production source transformation; those belong to the remaining R1 C2, R1 C4, and R3 C3 work.

## Proposed response to Reviewer 3, Comment 1

**Response:** We thank the reviewer for requesting validation on a real-world software system. We have now extended the evaluation to the official OpenCV 4.7.0 source tree, using the exact commit `725e440d278aca07d35a5e8963ef990572b07316`. The revision-time validation targets the OpenCV DNN convolution performance suite and uses a fixed workload drawn from `modules/dnn/perf/perf_convolution.cpp` (`Conv.conv/0`, `Conv.conv/2`, `Conv.conv/28`, `Conv.conv/42`, and `Conv.conv/69`). The exact source identity was verified before compilation, and the DNN performance target was built successfully from source.

To establish a measured real-project sequential reference, we used a clean Release build with explicit sequential controls (`--perf_threads=1`, `OPENCV_FOR_THREADS_NUM=1`, and one-CPU process affinity where supported). After three untimed warm-up process runs, we executed 30 independent timed process runs of the same fixed workload. All 30 runs completed successfully with exit code 0. The independently recomputed mean sequential runtime was **4.491456572 s** (median **4.470818768 s**, sample SD **0.118431329 s**, range **4.430297497–5.101106220 s**, CV **2.6368%**). The raw 30-run CSV, per-run logs, workload manifest, exact source hashes, machine/toolchain provenance, and the independent audit are included in the reproducibility artifact.

This experiment changes the evidence boundary of the manuscript: OpenCV 4.7.0 is no longer only a planned external target; the paper now has direct real-project source/build/workload/runtime evidence. We retain a narrow interpretation and do not infer measured optimized speedup or production source-rewrite safety from this baseline alone; those quantities are evaluated separately in the remaining validation steps.

## Proposed manuscript insertion

> **Real-project OpenCV validation.** To complement the controlled fixture suite, we evaluated the revision-time pipeline on the official OpenCV 4.7.0 source tree at commit `725e440d278aca07d35a5e8963ef990572b07316`. A fixed DNN convolution workload was selected from the official performance suite (`Conv.conv/0`, `Conv.conv/2`, `Conv.conv/28`, `Conv.conv/42`, and `Conv.conv/69`). The clean Release configuration was executed under explicit sequential controls (`--perf_threads=1`, `OPENCV_FOR_THREADS_NUM=1`, and one-CPU process affinity). Following three untimed warm-up runs, 30 independent process-level measurements produced a mean sequential runtime of **4.4915 s** (median **4.4708 s**, SD **0.1184 s**, CV **2.64%**; min–max **4.4303–5.1011 s**). All timed runs completed successfully. Exact source hashes, build provenance, the frozen workload manifest, the 30-run CSV, and raw logs are preserved in the public reproducibility artifact. This measurement establishes a real-project sequential reference and is not, by itself, presented as evidence of optimized measured speedup or automatic production-C++ rewriting.

## Evidence record

- Exact OpenCV commit: `725e440d278aca07d35a5e8963ef990572b07316`
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

## Remaining boundary

R3 C1 is evidence-complete once this text is integrated into the manuscript/reviewer-response package. R1 C2 still requires optimized measured runtime and modeled-vs-measured comparison; R1 C4 still requires the real profiling-derived timing/call/interactions evidence; R3 C3 still requires real-project transformation-safety evidence.
