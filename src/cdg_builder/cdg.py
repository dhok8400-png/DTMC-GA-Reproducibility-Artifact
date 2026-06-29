#!/usr/bin/env python3
from __future__ import annotations
import pandas as pd


def normalize_edges(edges: pd.DataFrame) -> pd.DataFrame:
    out = edges.copy()
    out['count'] = pd.to_numeric(out['count'], errors='raise')
    out['comm_cost'] = pd.to_numeric(out['comm_cost'], errors='raise')
    out['tgap'] = pd.to_numeric(out['tgap'], errors='coerce').fillna(0.0)
    out['async_eligible'] = out['async_eligible'].astype(str).str.lower().isin(['true','1','yes','y'])
    if 'call_use_pair_id' not in out.columns:
        out['call_use_pair_id'] = out['caller'].astype(str) + '_' + out['callee'].astype(str)
    return out


def class_list(classes: pd.DataFrame, edges: pd.DataFrame) -> list[str]:
    return sorted(set(classes['class_id']).union(edges['caller']).union(edges['callee']))
