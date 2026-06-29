#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md','LICENSE','CITATION.cff','reproducibility_checklist.md',
    'docker/Dockerfile','configs/experiment_config.yaml','configs/seeds_30.txt',
    'raw_results/experiment_runs.csv','statistical_analysis/analyze_results.py'
]
SCHEMA_FILES = {
    'raw_results/experiment_runs.csv': {'system','algorithm','seed','speedup','communication_overhead','load_balance','mq'},
    'raw_results/runtime_validation.csv': {'system','algorithm','seed','predicted_speedup','measured_speedup'},
    'raw_results/dtmc_validation.csv': {'system','class_id','dtmc_expected_visits','observed_visits'},
    'raw_results/mq_validation.csv': {'system','algorithm','seed','mq_speedup_based','measured_speedup'},
}


def headers(path: Path) -> set[str]:
    with path.open(newline='', encoding='utf-8') as f:
        return set(next(csv.reader(f)))


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT/p).exists()]
    if missing:
        raise SystemExit('Missing required artifact files: ' + ', '.join(missing))
    for rel, required in SCHEMA_FILES.items():
        path = ROOT/rel
        h = headers(path)
        miss = required - h
        if miss:
            raise SystemExit(f'{rel} missing required columns: {sorted(miss)}')
    print('Artifact structure and schemas OK. Note: schema check does not validate that final experimental data are populated.')

if __name__ == '__main__':
    main()
