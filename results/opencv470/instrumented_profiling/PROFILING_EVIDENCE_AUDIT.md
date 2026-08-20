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
- profile_nodes.csv SHA-256: `4cba4401b6fdb43460e8059dcb91d75925a2527d4165629275a687db66de95ae`
- dynamic_interaction_edges.csv SHA-256: `e36c5e4c12ab6c60d20036f6ef168ac57451d16eba198be2be671dd9025cbd73`

The audit confirms real instrumented call/timing/interactions evidence while preserving the boundary that byte-level communication volume and parallel overlap were not measured by this single-threaded profiling campaign.
