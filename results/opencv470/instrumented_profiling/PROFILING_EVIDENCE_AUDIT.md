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
- profile_nodes.csv SHA-256: `bbacee65a5edc6ae8ee2f45152291b2355c57ace96d10d876763e11b693aad31`
- dynamic_interaction_edges.csv SHA-256: `792876118c0756c7a26af9da363c30ae5127180ebd63c933b5c36da536af1340`

The audit confirms real instrumented call/timing/interactions evidence while preserving the boundary that byte-level communication volume and parallel overlap were not measured by this single-threaded profiling campaign.
