#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy import stats

METRICS = ['speedup', 'communication_overhead', 'load_balance', 'mq', 'algorithm_runtime_s', 'memory_mb']


def ci95(x: pd.Series) -> float:
    x = pd.to_numeric(x, errors='coerce').dropna()
    if len(x) < 2:
        return float('nan')
    return float(stats.t.ppf(0.975, len(x)-1) * x.std(ddof=1) / np.sqrt(len(x)))


def rank_biserial_from_wilcoxon(x, y) -> float:
    d = np.asarray(x, dtype=float) - np.asarray(y, dtype=float)
    d = d[d != 0]
    if len(d) == 0:
        return 0.0
    ranks = stats.rankdata(np.abs(d))
    r_plus = ranks[d > 0].sum()
    r_minus = ranks[d < 0].sum()
    return float((r_plus - r_minus) / (r_plus + r_minus))


def write_flat_summary(df: pd.DataFrame, out_file: Path) -> None:
    rows = []
    for (system, algorithm), g in df.groupby(['system', 'algorithm']):
        for metric in METRICS:
            if metric not in g.columns:
                continue
            values = pd.to_numeric(g[metric], errors='coerce').dropna()
            if values.empty:
                continue
            rows.append({
                'system': system,
                'algorithm': algorithm,
                'metric': metric,
                'count': int(values.count()),
                'mean': float(values.mean()),
                'median': float(values.median()),
                'sd': float(values.std(ddof=1)) if len(values) > 1 else float('nan'),
                'ci95': ci95(values),
                'min': float(values.min()),
                'max': float(values.max()),
            })
    pd.DataFrame(rows).to_csv(out_file, index=False)


def main() -> None:
    ap = argparse.ArgumentParser(description='Summarize experiment runs and compute non-parametric tests.')
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)
    if df.empty:
        (out/'analysis_not_run.md').write_text('Input has headers only. Populate raw_results/experiment_runs.csv with real runs before analysis.\n', encoding='utf-8')
        print('Input has headers only. Populate raw_results/experiment_runs.csv with real runs before analysis.')
        return
    required = {'system','algorithm','seed'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f'Missing required columns: {sorted(missing)}')
    for m in METRICS:
        if m in df.columns:
            df[m] = pd.to_numeric(df[m], errors='coerce')

    # Flat one-row-per-metric summary; this is easier for manuscripts, reviewers, and CI checks
    # than a multi-index/multi-row header CSV.
    write_flat_summary(df, out/'summary_statistics.csv')

    tests = []
    if 'speedup' in df.columns:
        for system, g in df.dropna(subset=['speedup']).groupby('system'):
            pivot = g.pivot_table(index='seed', columns='algorithm', values='speedup', aggfunc='mean')
            pivot = pivot.dropna(axis=1, how='any')
            if pivot.shape[1] >= 3 and pivot.shape[0] >= 2:
                stat, p = stats.friedmanchisquare(*[pivot[c].values for c in pivot.columns])
                tests.append({'system':system,'test':'Friedman','metric':'speedup','statistic':stat,'p_value':p,'p_bonferroni':'','rank_biserial':'','comparison':'','methods':';'.join(pivot.columns),'status':'ok','notes':''})
            algs = list(pivot.columns)
            n_pairs = max(1, len(algs)*(len(algs)-1)//2)
            for i,a in enumerate(algs):
                for b in algs[i+1:]:
                    pair = pivot[[a,b]].dropna()
                    if pair.shape[0] < 2:
                        tests.append({'system':system,'test':'Wilcoxon_Bonferroni','metric':'speedup','comparison':f'{a} vs {b}','statistic':'','p_value':'','p_bonferroni':'','rank_biserial':'','methods':'','status':'not_run','notes':'fewer than two paired observations'})
                        continue
                    diff = pair[a].to_numpy(dtype=float) - pair[b].to_numpy(dtype=float)
                    if np.allclose(diff, 0.0):
                        tests.append({'system':system,'test':'Wilcoxon_Bonferroni','metric':'speedup','comparison':f'{a} vs {b}','statistic':0.0,'p_value':1.0,'p_bonferroni':1.0,'rank_biserial':0.0,'methods':'','status':'identical','notes':'all paired differences are zero; no Wilcoxon warning emitted'})
                        continue
                    try:
                        st, p = stats.wilcoxon(pair[a], pair[b], zero_method='wilcox')
                        tests.append({'system':system,'test':'Wilcoxon_Bonferroni','metric':'speedup','comparison':f'{a} vs {b}','statistic':st,'p_value':p,'p_bonferroni':min(p*n_pairs,1.0),'rank_biserial':rank_biserial_from_wilcoxon(pair[a], pair[b]),'methods':'','status':'ok','notes':''})
                    except ValueError as exc:
                        tests.append({'system':system,'test':'Wilcoxon_Bonferroni','metric':'speedup','comparison':f'{a} vs {b}','statistic':'','p_value':'','p_bonferroni':'','rank_biserial':rank_biserial_from_wilcoxon(pair[a], pair[b]),'methods':'','status':'not_run','notes':str(exc)})
    pd.DataFrame(tests).to_csv(out/'statistical_tests.csv', index=False)
    manifest = {'input': args.input, 'rows': int(len(df)), 'note': 'All reported rows were retained; no best-run filtering is performed by this script.', 'summary_format': 'flat one-row-per-system-algorithm-metric'}
    (out/'analysis_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
