from pathlib import Path
import sys
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.parser.csv_reader import read_benchmark
from src.cdg_builder.cdg import normalize_edges
from src.dtmc_analyzer.dtmc_matrix import build_transition_matrix, expected_visits
from src.call_use_displacement.displacement import apply_safe_displacement
from src.ga_optimizer.optimizer import optimize


def test_demo_benchmark_loads_and_optimizes():
    classes, edges, safety = read_benchmark(ROOT / 'benchmarks/demo_eight_class')
    edges = normalize_edges(edges)
    edges, decisions = apply_safe_displacement(edges, safety)
    P = build_transition_matrix(edges, sorted(set(classes.class_id).union(edges.caller).union(edges.callee)))
    assert all(abs(P.sum(axis=1) - 1.0) < 1e-9)
    visits = expected_visits(P, start='A', horizon=20)
    result = optimize(classes, edges, visits, algorithm='DTMC-GA', seed=1, generations=4, population_size=8)
    assert result.metrics['speedup'] > 0
    assert 0 <= result.metrics['communication_overhead'] <= 1
    assert len(result.partition) == len(classes)
