#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import pandas as pd

REQUIRED_RUN_COLUMNS = {'system','algorithm','seed','run_id','modules','speedup','communication_overhead','load_balance','mq','status'}


def validate_experiment_runs(path: str | Path) -> None:
    df = pd.read_csv(path)
    missing = REQUIRED_RUN_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f'experiment_runs.csv missing columns: {sorted(missing)}')
    if not df.empty and (df['status'].astype(str) == '').any():
        raise ValueError('status column contains empty values')
