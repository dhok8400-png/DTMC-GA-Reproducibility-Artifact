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
- profile_nodes.csv SHA-256: `1ad487bb97d3481573f9062f5af51c875e37d494cb9209a13937669b32a6d46c`
- dynamic_interaction_edges.csv SHA-256: `647978e776d2045e0dac7e41ff6c65fed9fe787f9611e0b7969ddd95b150e2ca`

The audit confirms real instrumented call/timing/interactions evidence while preserving the boundary that byte-level communication volume and parallel overlap were not measured by this single-threaded profiling campaign.
