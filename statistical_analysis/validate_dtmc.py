#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats


def main():
    ap=argparse.ArgumentParser(description='Validate DTMC estimates against dynamic traces.')
    ap.add_argument('--input', required=True); ap.add_argument('--out', required=True)
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df=pd.read_csv(args.input)
    if df.empty:
        (out/'dtmc_validation_not_run.md').write_text('Input has headers only. Populate dtmc_validation.csv first.\n', encoding='utf-8')
        print('Input has headers only. Populate dtmc_validation.csv first.')
        return
    req={'dtmc_expected_visits','observed_visits','static_call_frequency','dynamic_call_frequency'}
    missing=req-set(df.columns)
    if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
    rows=[]
    for system,g in df.groupby('system') if 'system' in df.columns else [('all',df)]:
        ev=pd.to_numeric(g['dtmc_expected_visits'], errors='coerce')
        ov=pd.to_numeric(g['observed_visits'], errors='coerce')
        sc=pd.to_numeric(g['static_call_frequency'], errors='coerce')
        dc=pd.to_numeric(g['dynamic_call_frequency'], errors='coerce')
        tmp=pd.DataFrame({'ev':ev,'ov':ov,'sc':sc,'dc':dc}).dropna()
        if len(tmp) == 0: continue
        mape=float(np.mean(np.abs((tmp.ov-tmp.ev)/tmp.ov.replace(0,np.nan))) * 100)
        rows.append({
            'system':system,
            'n':len(tmp),
            'visit_MAE':float(np.mean(np.abs(tmp.ov-tmp.ev))),
            'visit_MAPE_percent':mape,
            'visit_pearson_r':float(stats.pearsonr(tmp.ev,tmp.ov).statistic) if len(tmp)>=2 else None,
            'visit_spearman_rho':float(stats.spearmanr(tmp.ev,tmp.ov).statistic) if len(tmp)>=2 else None,
            'callfreq_pearson_r':float(stats.pearsonr(tmp.sc,tmp.dc).statistic) if len(tmp)>=2 else None,
            'callfreq_spearman_rho':float(stats.spearmanr(tmp.sc,tmp.dc).statistic) if len(tmp)>=2 else None,
        })
    pd.DataFrame(rows).to_csv(out/'dtmc_validation_metrics.csv', index=False)

if __name__=='__main__': main()
