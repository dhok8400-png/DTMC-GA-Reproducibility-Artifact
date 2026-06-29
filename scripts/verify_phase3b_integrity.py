#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SYSTEMS = [
    'demo_eight_class', 'layered_services_12', 'event_pipeline_16',
    'cyclic_workflow_20', 'plugin_platform_24'
]
EXPECTED_ALGORITHMS = ['DTMC-GA','Bunch','FCA','RandomValidPartition','TraditionalMQ']
EXPECTED_SEEDS = 30
EXPECTED_ROWS = len(EXPECTED_SYSTEMS) * len(EXPECTED_ALGORITHMS) * EXPECTED_SEEDS

REQUIRED_RAW = [
    'experiment_runs.csv', 'runtime_validation.csv', 'dtmc_validation.csv',
    'mq_validation.csv', 'ablation_results.csv', 'sensitivity_results.csv',
    'per_generation_logs.csv'
]
REQUIRED_PROCESSED = [
    'summary_statistics.csv', 'statistical_tests.csv', 'dtmc_validation_metrics.csv',
    'mq_validation_metrics.csv', 'runtime_validation_metrics.json',
    'phase3B_benchmark_suite_manifest.json'
]
REQUIRED_FIGURES = [
    'phase3B_speedup_by_system', 'phase3B_communication_by_system',
    'phase3B_runtime_validation', 'phase3B_mq_validation', 'phase3B_ablation',
    'phase3B_sensitivity_latency', 'phase3B_module_size_representative',
    'phase3B_heatmap_representative'
]

def require(path: Path, errors: list[str], min_bytes: int = 1) -> None:
    if not path.exists():
        errors.append(f'missing: {path.relative_to(ROOT)}')
    elif path.stat().st_size < min_bytes:
        errors.append(f'too small: {path.relative_to(ROOT)} ({path.stat().st_size} bytes)')

def main() -> int:
    errors: list[str] = []
    raw_dir = ROOT / 'raw_results'
    processed_dir = ROOT / 'processed_results'
    figures_dir = ROOT / 'figures'

    for name in REQUIRED_RAW:
        require(raw_dir / name, errors)
    for name in REQUIRED_PROCESSED:
        require(processed_dir / name, errors)
    for stem in REQUIRED_FIGURES:
        require(figures_dir / f'{stem}.png', errors, min_bytes=1000)
        require(figures_dir / f'{stem}.pdf', errors, min_bytes=1000)

    runs_path = raw_dir / 'experiment_runs.csv'
    if runs_path.exists():
        runs = pd.read_csv(runs_path)
        if len(runs) != EXPECTED_ROWS:
            errors.append(f'experiment_runs.csv row count {len(runs)} != {EXPECTED_ROWS}')
        systems = sorted(runs['system'].astype(str).unique())
        if systems != sorted(EXPECTED_SYSTEMS):
            errors.append(f'systems mismatch: {systems}')
        algorithms = sorted(runs['algorithm'].astype(str).unique())
        if algorithms != sorted(EXPECTED_ALGORITHMS):
            errors.append(f'algorithms mismatch: {algorithms}')
        duplicates = int(runs.duplicated(['system','algorithm','seed']).sum())
        if duplicates != 0:
            errors.append(f'duplicate system/algorithm/seed rows: {duplicates}')
        coverage = runs.groupby(['system','algorithm'])['seed'].nunique().reset_index(name='seed_count')
        bad = coverage[coverage['seed_count'] != EXPECTED_SEEDS]
        if not bad.empty:
            errors.append('seed coverage mismatch: ' + bad.to_csv(index=False).strip())
        if 'benchmark_type' in runs.columns:
            bad_type = runs[~runs['benchmark_type'].astype(str).str.contains('phase3B_csv_fixture', na=False)]
            if len(bad_type):
                errors.append(f'unexpected benchmark_type rows: {len(bad_type)}')

    report = {
        'phase': '3C',
        'check': 'phase3B_integrity',
        'expected_rows': EXPECTED_ROWS,
        'status': 'passed' if not errors else 'failed',
        'errors': errors,
    }
    out = processed_dir / 'phase3C_integrity_report.json'
    out.write_text(json.dumps(report, indent=2), encoding='utf-8')
    if errors:
        print('Phase 3C integrity check FAILED')
        for e in errors:
            print(f'- {e}')
        return 1
    print('Phase 3C integrity check passed: 750 rows, full 5x5x30 coverage, no duplicates, required outputs/figures present.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
