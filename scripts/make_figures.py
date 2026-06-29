#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Matplotlib only. No custom colors are specified to keep output portable and style-neutral.

def _save(fig, out: Path, stem: str):
    fig.tight_layout()
    fig.savefig(out/f'{stem}.png', dpi=300, bbox_inches='tight')
    fig.savefig(out/f'{stem}.pdf', bbox_inches='tight')
    plt.close(fig)

def grouped_bar(df, metric, ylabel, out, stem):
    summary = df.groupby(['system','algorithm'])[metric].mean().reset_index()
    systems = list(summary['system'].unique())
    algs = list(summary['algorithm'].unique())
    x = np.arange(len(systems)); width = 0.8/max(len(algs),1)
    fig, ax = plt.subplots(figsize=(11,6))
    for i, alg in enumerate(algs):
        vals=[summary[(summary.system==s)&(summary.algorithm==alg)][metric].mean() for s in systems]
        ax.bar(x + (i-(len(algs)-1)/2)*width, vals, width, label=alg)
    ax.set_ylabel(ylabel); ax.set_xlabel('Benchmark fixture')
    ax.set_xticks(x); ax.set_xticklabels(systems, rotation=30, ha='right')
    ax.legend(ncols=2, fontsize=8)
    ax.grid(axis='y', alpha=0.25)
    _save(fig,out,stem)

def main():
    ap=argparse.ArgumentParser(description='Generate Phase 3B manuscript figures from raw results.')
    ap.add_argument('--runs', default='raw_results/experiment_runs.csv')
    ap.add_argument('--out', default='figures')
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    runs=pd.read_csv(args.runs)
    if runs.empty: raise SystemExit('No rows in experiment_runs.csv; figures cannot be generated yet.')
    grouped_bar(runs, 'speedup', 'Speedup ratio', out, 'phase3B_speedup_by_system')
    grouped_bar(runs, 'communication_overhead', 'Communication overhead ratio', out, 'phase3B_communication_by_system')
    # legacy/compatibility speedup boxplot
    fig, ax = plt.subplots(figsize=(9,5.5))
    runs.boxplot(column='speedup', by='algorithm', rot=35, ax=ax)
    fig.suptitle(''); ax.set_title('Speedup distribution by algorithm')
    ax.set_ylabel('Speedup ratio'); ax.set_xlabel('Algorithm')
    _save(fig,out,'speedup_by_algorithm')
    # Runtime validation scatter
    rv_path=Path('raw_results/runtime_validation.csv')
    if rv_path.exists():
        rv=pd.read_csv(rv_path)
        fig, ax = plt.subplots(figsize=(6.5,6))
        ax.scatter(rv['predicted_speedup'], rv['measured_speedup'], alpha=0.55, s=16)
        lo=float(min(rv['predicted_speedup'].min(), rv['measured_speedup'].min()))
        hi=float(max(rv['predicted_speedup'].max(), rv['measured_speedup'].max()))
        ax.plot([lo,hi],[lo,hi], linestyle='--', linewidth=1)
        ax.set_xlabel('Predicted speedup'); ax.set_ylabel('Surrogate measured speedup')
        ax.set_title('Runtime validation: predicted vs surrogate measured speedup')
        ax.grid(alpha=0.25)
        _save(fig,out,'phase3B_runtime_validation')
    # MQ validation scatter
    mq_path=Path('raw_results/mq_validation.csv')
    if mq_path.exists():
        mq=pd.read_csv(mq_path)
        fig, ax = plt.subplots(figsize=(6.5,6))
        ax.scatter(mq['mq_speedup_based'], mq['measured_speedup'], alpha=0.55, s=16)
        ax.set_xlabel('Speedup-based MQ'); ax.set_ylabel('Surrogate measured speedup')
        ax.set_title('MQ validation on Phase 3B benchmark suite')
        ax.grid(alpha=0.25)
        _save(fig,out,'phase3B_mq_validation')
    # Ablation plot
    ab_path=Path('raw_results/ablation_results.csv')
    if ab_path.exists():
        ab=pd.read_csv(ab_path)
        summary=ab.groupby('variant')['difference_from_full_percent'].mean().sort_values()
        fig, ax = plt.subplots(figsize=(10,5.8))
        ax.barh(summary.index, summary.values)
        ax.axvline(0, linewidth=1)
        ax.set_xlabel('Difference from full DTMC-GA (%)')
        ax.set_title('Ablation effect on speedup')
        ax.grid(axis='x', alpha=0.25)
        _save(fig,out,'phase3B_ablation')
    # Latency sensitivity
    sens_path=Path('raw_results/sensitivity_results.csv')
    if sens_path.exists():
        sens=pd.read_csv(sens_path)
        lat=sens[sens['parameter']=='communication_latency']
        if not lat.empty:
            summary=lat.groupby('parameter_value')['speedup'].mean().reset_index()
            fig, ax = plt.subplots(figsize=(7,5))
            ax.plot(summary['parameter_value'], summary['speedup'], marker='o')
            ax.set_xlabel('Communication latency multiplier')
            ax.set_ylabel('Mean speedup')
            ax.set_title('Sensitivity to communication latency')
            ax.grid(alpha=0.25)
            _save(fig,out,'phase3B_sensitivity_latency')
    # Representative module sizes and communication heatmap for plugin_platform_24, seed 1, DTMC-GA.
    assign_path=Path('processed_results/module_assignments.csv')
    if assign_path.exists():
        assign=pd.read_csv(assign_path)
        rep='plugin_platform_24' if 'plugin_platform_24' in set(assign.system) else assign.system.iloc[0]
        sub=assign[(assign.system==rep)&(assign.algorithm=='DTMC-GA')& (assign.seed==1)]
        if not sub.empty:
            sizes=sub.groupby('module_id')['class_id'].count().sort_index()
            fig, ax = plt.subplots(figsize=(7,5))
            ax.bar([str(x) for x in sizes.index], sizes.values)
            ax.set_xlabel('Generated module'); ax.set_ylabel('Number of classes')
            ax.set_title(f'Module-size distribution: {rep}')
            ax.grid(axis='y', alpha=0.25)
            _save(fig,out,'phase3B_module_size_representative')
            # Heatmap
            edges=pd.read_csv(Path('benchmarks')/rep/'edges.csv')
            part=dict(zip(sub.class_id.astype(str), sub.module_id.astype(int)))
            modules=sorted(sizes.index.astype(int))
            mat=pd.DataFrame(0.0, index=modules, columns=modules)
            for _,e in edges.iterrows():
                a=part.get(str(e.caller)); b=part.get(str(e.callee))
                if a is not None and b is not None:
                    mat.loc[a,b]+=float(e['count'])
            fig, ax = plt.subplots(figsize=(6,5.5))
            im=ax.imshow(mat.values, aspect='auto')
            ax.set_xticks(range(len(modules))); ax.set_xticklabels(modules)
            ax.set_yticks(range(len(modules))); ax.set_yticklabels(modules)
            ax.set_xlabel('Callee module'); ax.set_ylabel('Caller module')
            ax.set_title(f'Inter-module call-weight matrix: {rep}')
            fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
            _save(fig,out,'phase3B_heatmap_representative')

if __name__=='__main__': main()
