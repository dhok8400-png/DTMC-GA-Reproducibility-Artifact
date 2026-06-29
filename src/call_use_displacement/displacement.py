#!/usr/bin/env python3
from __future__ import annotations
import pandas as pd
from .safety_rules import decide_call_use_displacement

BOOL_COLS = [
    'preserves_data_dependence','preserves_anti_dependence','preserves_output_dependence',
    'preserves_control_dependence','no_unsafe_aliasing','no_unordered_side_effects',
    'preserves_exception_order','preserves_object_lifetime','no_volatile_or_atomic_reordering',
    'synchronization_before_first_use'
]


def apply_safe_displacement(edges: pd.DataFrame, safety: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    out = edges.copy()
    out['displacement_allowed'] = False
    out['displacement_reason'] = ''
    out['tgap_original'] = out['tgap']
    if safety.empty:
        return out, pd.DataFrame(columns=['call_use_pair_id','allowed','reasons'])
    decisions = []
    safety_index = safety.set_index('call_use_pair_id')
    for i, row in out.iterrows():
        pair = row.get('call_use_pair_id')
        if pair not in safety_index.index or not bool(row.get('async_eligible', False)):
            continue
        s = safety_index.loc[pair]
        kwargs = {c: str(s[c]).lower() in ['true','1','yes','y'] for c in BOOL_COLS}
        decision = decide_call_use_displacement(**kwargs)
        extra_gap = float(s.get('additional_gap', 0.0)) if decision.allowed else 0.0
        out.at[i, 'displacement_allowed'] = decision.allowed
        out.at[i, 'displacement_reason'] = ';'.join(decision.reasons)
        out.at[i, 'tgap'] = float(row['tgap']) + extra_gap
        decisions.append({'call_use_pair_id': pair, 'allowed': decision.allowed, 'reasons': ';'.join(decision.reasons), 'additional_gap_applied': extra_gap})
    return out, pd.DataFrame(decisions)
