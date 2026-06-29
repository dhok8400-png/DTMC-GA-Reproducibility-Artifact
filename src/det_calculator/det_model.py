#!/usr/bin/env python3
from __future__ import annotations
import math
import pandas as pd


def evaluate_partition(classes: pd.DataFrame, edges: pd.DataFrame, partition: dict[str, int], visits: pd.Series | None = None) -> dict[str, float]:
    """Evaluate a candidate modularization with a compact DET-inspired model.

    The model is intentionally simple for Phase 3A: it is executable, deterministic, and
    sufficient for validating the artifact pipeline. It does not replace final measured runtime
    validation on full benchmarks.
    """
    local = {str(r.class_id): float(r.local_time) for r in classes.itertuples()}
    if visits is None:
        visits = pd.Series({c: 1.0 for c in local})
    # Scale visits to a moderate expected workload.
    v = {c: float(visits.get(c, 1.0)) for c in local}
    scale = max(sum(v.values()), 1.0)
    v = {c: 1.0 + 5.0 * val / scale for c, val in v.items()}
    serial_work = sum(local[c] * v[c] for c in local)
    serial_call_overhead = sum(float(e.count) * float(e.comm_cost) for e in edges.itertuples())
    sequential_runtime = serial_work + serial_call_overhead
    modules = sorted(set(partition.values()))
    module_work = {m: 0.0 for m in modules}
    for c, t in local.items():
        module_work[partition[c]] += t * v[c]
    cross_comm = 0.0
    overlap_credit = 0.0
    cross_edges = 0
    speedup_mq = 0.0
    for e in edges.itertuples():
        caller, callee = str(e.caller), str(e.callee)
        count, comm, tgap = float(e.count), float(e.comm_cost), float(e.tgap)
        if partition[caller] != partition[callee]:
            cross_edges += 1
            cross_comm += count * comm
            if bool(getattr(e, 'async_eligible', False)):
                # A conservative overlap credit bounded by callee work and communication cost.
                benefit = min(tgap, local.get(callee, 0.0) * 0.65) * count * 0.16
                overlap_credit += benefit
                speedup_mq += benefit
            else:
                speedup_mq += max(0.0, 0.03 * count - 0.02 * comm)
    balance_values = list(module_work.values())
    mean_work = sum(balance_values) / len(balance_values)
    std_work = math.sqrt(sum((x - mean_work) ** 2 for x in balance_values) / len(balance_values)) if balance_values else 0.0
    load_balance = max(0.0, 1.0 - (std_work / mean_work if mean_work else 0.0))
    parallel_runtime = max(balance_values) + cross_comm - overlap_credit
    parallel_runtime = max(parallel_runtime, sequential_runtime * 0.05)
    speedup = sequential_runtime / parallel_runtime
    communication_overhead = cross_comm / sequential_runtime if sequential_runtime else 0.0
    traditional_mq = _traditional_mq(edges, partition)
    return {
        'sequential_runtime_s': sequential_runtime,
        'parallel_runtime_s': parallel_runtime,
        'predicted_speedup': speedup,
        'speedup': speedup,
        'communication_overhead': communication_overhead,
        'load_balance': load_balance,
        'mq': speedup_mq,
        'mq_traditional': traditional_mq,
        'modules': len(modules),
        'cross_edges': cross_edges,
        'module_work_cv': 1.0 - load_balance,
    }


def _traditional_mq(edges: pd.DataFrame, partition: dict[str, int]) -> float:
    intra = 0.0; inter = 0.0
    for e in edges.itertuples():
        w = float(e.count)
        if partition[str(e.caller)] == partition[str(e.callee)]:
            intra += w
        else:
            inter += w
    return intra / (intra + inter) if (intra + inter) else 0.0
