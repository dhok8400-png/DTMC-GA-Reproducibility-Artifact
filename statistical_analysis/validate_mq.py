#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats


def regression_metrics(y, x):
    x=np.asarray(x,dtype=float); y=np.asarray(y,dtype=float)
    if len(x)<2: return {'pearson_r':None,'spearman_rho':None,'r2':None}
    r=stats.pearsonr(x,y).statistic
    rho=stats.spearmanr(x,y).statistic
    return {'pearson_r':float(r),'spearman_rho':float(rho),'r2':float(r*r)}


def main():
    ap=argparse.ArgumentParser(description='Validate MQ and structural metrics against measured speedup.')
    ap.add_argument('--input', required=True); ap.add_argument('--out', required=True)
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df=pd.read_csv(args.input)
    if df.empty:
        (out/'mq_validation_not_run.md').write_text('Input has headers only. Populate mq_validation.csv first.\n', encoding='utf-8')
        print('Input has headers only. Populate mq_validation.csv first.')
        return
    if 'measured_speedup' not in df.columns: raise ValueError('Missing measured_speedup')
    y=pd.to_numeric(df['measured_speedup'], errors='coerce')
    rows=[]
    for col in ['mq_speedup_based','mq_traditional','coupling','cohesion','graph_modularity']:
        if col in df.columns:
            x=pd.to_numeric(df[col], errors='coerce')
            tmp=pd.DataFrame({'x':x,'y':y}).dropna()
            m=regression_metrics(tmp.y,tmp.x)
            m.update({'metric':col,'n':len(tmp)})
            rows.append(m)
    pd.DataFrame(rows).to_csv(out/'mq_validation_metrics.csv', index=False)

if __name__=='__main__': main()
