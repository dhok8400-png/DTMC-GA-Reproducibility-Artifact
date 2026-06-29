#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats


def mape(y_true, y_pred):
    y_true = np.asarray(y_true, dtype=float); y_pred = np.asarray(y_pred, dtype=float)
    mask = y_true != 0
    return float(np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100)


def main():
    ap = argparse.ArgumentParser(description='Validate predicted speedup against measured speedup.')
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', required=True)
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df=pd.read_csv(args.input)
    if df.empty:
        (out/'runtime_validation_not_run.md').write_text('Input has headers only. Populate runtime_validation.csv first.\n', encoding='utf-8')
        print('Input has headers only. Populate runtime_validation.csv first.')
        return
    req={'predicted_speedup','measured_speedup'}
    if req-set(df.columns): raise ValueError(f'Missing columns: {sorted(req-set(df.columns))}')
    x=pd.to_numeric(df['predicted_speedup'], errors='coerce')
    y=pd.to_numeric(df['measured_speedup'], errors='coerce')
    valid=pd.DataFrame({'predicted':x,'measured':y}).dropna()
    report={
        'n': int(len(valid)),
        'MAE': float(np.mean(np.abs(valid.measured-valid.predicted))),
        'RMSE': float(np.sqrt(np.mean((valid.measured-valid.predicted)**2))),
        'MAPE_percent': mape(valid.measured, valid.predicted),
        'pearson_r': float(stats.pearsonr(valid.predicted, valid.measured).statistic) if len(valid)>=2 else None,
        'spearman_rho': float(stats.spearmanr(valid.predicted, valid.measured).statistic) if len(valid)>=2 else None,
    }
    pd.Series(report).to_json(out/'runtime_validation_metrics.json', indent=2)

if __name__ == '__main__': main()
