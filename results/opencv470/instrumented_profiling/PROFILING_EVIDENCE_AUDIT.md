# OpenCV 4.7.0 Instrumented Profiling — Independent Evidence Audit

**Status: PASS**

- Exact OpenCV commit: `725e440d278aca07d35a5e8963ef990572b07316`
- Untimed profiling warm-ups: 2
- Independent profiling runs: 5
- Parsed trace node rows: 25
- Unique parent/node pairs: 1
- Parsed dynamic edge rows: 25
- Unique parent/child pairs: 1
- Maximum threads observed in trace nodes: 1
- Byte-level communication measured: False
- Parallel overlap measured: False
- Sequential overlap by design: 0
- profile_nodes.csv SHA-256: `2750cbd2366768865df8a3c9eb7e87d13aaa692aa6499de6b0ce706facd9a695`
- dynamic_interaction_edges.csv SHA-256: `b4449a99831c2fa4eaa24677f64546dd7bd41a9d0099d7c9ad2f16ba4f39d639`

The audit confirms real instrumented call/timing/interactions evidence while preserving the boundary that byte-level communication volume and parallel overlap were not measured by this single-threaded profiling campaign.
