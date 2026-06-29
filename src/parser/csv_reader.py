#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import pandas as pd


def read_benchmark(path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Read a benchmark represented by classes.csv, edges.csv, and safety.csv.

    This Phase 3A reader is deliberately simple and reproducible. It does not claim to be a
    Clang/LLVM parser. The final artifact can replace this reader with a source-code parser
    while preserving the same normalized tables.
    """
    root = Path(path)
    classes = pd.read_csv(root / 'classes.csv')
    edges = pd.read_csv(root / 'edges.csv')
    safety = pd.read_csv(root / 'safety.csv') if (root / 'safety.csv').exists() else pd.DataFrame()
    required_classes = {'class_id', 'local_time'}
    required_edges = {'caller', 'callee', 'count', 'comm_cost', 'tgap', 'async_eligible'}
    if missing := required_classes - set(classes.columns):
        raise ValueError(f'classes.csv missing columns: {sorted(missing)}')
    if missing := required_edges - set(edges.columns):
        raise ValueError(f'edges.csv missing columns: {sorted(missing)}')
    return classes, edges, safety
