# Figures

This folder contains generated Phase 3B figures in both high-resolution PNG and vector PDF formats where applicable.

Generated Phase 3B figure set:

- `phase3B_speedup_by_system.*`
- `phase3B_communication_by_system.*`
- `phase3B_runtime_validation.*`
- `phase3B_mq_validation.*`
- `phase3B_ablation.*`
- `phase3B_sensitivity_latency.*`
- `phase3B_module_size_representative.*`
- `phase3B_heatmap_representative.*`

The figures are regenerated from the Phase 3B local executable benchmark-suite outputs and are intended for manuscript reporting of the fixture-suite evidence only. They should not be described as external large-project runtime evidence unless external traces are added and the figures are regenerated from those traces.

To regenerate the figures after updating raw data, run:

```bash
python scripts/make_figures.py
```

or use the repository-level smoke/full-analysis scripts described in `README.md`.
