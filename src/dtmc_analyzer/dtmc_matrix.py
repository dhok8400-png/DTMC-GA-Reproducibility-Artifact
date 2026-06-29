#!/usr/bin/env python3
from __future__ import annotations
import argparse
import pandas as pd
import numpy as np


def build_transition_matrix(edges: pd.DataFrame, classes: list[str] | None = None) -> pd.DataFrame:
    required = {'caller', 'callee', 'count'}
    if not required.issubset(edges.columns):
        raise ValueError(f'edges CSV must contain {required}')
    if classes is None:
        classes = sorted(set(edges['caller']).union(edges['callee']))
    matrix = pd.DataFrame(0.0, index=classes, columns=classes)
    for _, row in edges.iterrows():
        matrix.loc[row['caller'], row['callee']] += float(row['count'])
    row_sums = matrix.sum(axis=1)
    for c in classes:
        if row_sums.loc[c] == 0:
            matrix.loc[c, c] = 1.0
        else:
            matrix.loc[c, :] = matrix.loc[c, :] / row_sums.loc[c]
    return matrix


def expected_visits(matrix: pd.DataFrame, start: str, horizon: int = 100) -> pd.Series:
    """Finite-horizon expected visits from a starting class.

    A finite horizon is used so the function is well-defined even when the graph has cycles.
    It is suitable for Phase 3A demonstration and trace-correlation validation. Large-scale
    experiments can replace this with workload-specific trace aggregation.
    """
    classes = list(matrix.index)
    idx = classes.index(start)
    state = np.zeros(len(classes), dtype=float)
    state[idx] = 1.0
    visits = np.zeros(len(classes), dtype=float)
    P = matrix.to_numpy(dtype=float)
    for _ in range(horizon):
        visits += state
        state = state @ P
    return pd.Series(visits, index=classes)


def simulate_visits(matrix: pd.DataFrame, start: str, steps: int = 1000, seed: int = 1) -> pd.Series:
    rng = np.random.default_rng(seed)
    classes = list(matrix.index)
    current = start
    counts = {c: 0 for c in classes}
    for _ in range(steps):
        counts[current] += 1
        probs = matrix.loc[current].to_numpy(dtype=float)
        current = rng.choice(classes, p=probs)
    return pd.Series(counts, dtype=float)


def main() -> None:
    ap = argparse.ArgumentParser(description='Build DTMC transition matrix from call-edge counts.')
    ap.add_argument('--edges', required=True, help='CSV with caller,callee,count')
    ap.add_argument('--out', required=True, help='Output CSV path')
    args = ap.parse_args()
    edges = pd.read_csv(args.edges)
    matrix = build_transition_matrix(edges)
    matrix.to_csv(args.out)

if __name__ == '__main__':
    main()
