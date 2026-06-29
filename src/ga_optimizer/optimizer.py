#!/usr/bin/env python3
from __future__ import annotations
import random, time
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from src.det_calculator.det_model import evaluate_partition

@dataclass
class OptimizationResult:
    partition: dict[str, int]
    metrics: dict[str, float]
    generation_log: list[dict]
    runtime_s: float


def _classes(classes: pd.DataFrame) -> list[str]:
    return list(classes['class_id'].astype(str))


def random_partition(class_ids: list[str], rng: random.Random, max_modules: int = 3) -> dict[str, int]:
    return {c: rng.randint(1, max_modules) for c in class_ids}


def _fitness(metrics: dict[str, float], mode: str) -> float:
    if mode == 'traditional':
        return metrics['mq_traditional'] + 0.05 * metrics['load_balance'] - 0.2 * metrics['communication_overhead']
    return metrics['speedup'] + 0.35 * metrics['load_balance'] + 0.12 * metrics['mq'] - 0.8 * metrics['communication_overhead']


def _mutate(partition: dict[str, int], rng: random.Random, max_modules: int) -> dict[str, int]:
    out = dict(partition)
    c = rng.choice(list(out.keys()))
    out[c] = rng.randint(1, max_modules)
    return out


def _crossover(a: dict[str, int], b: dict[str, int], rng: random.Random) -> dict[str, int]:
    keys = list(a.keys())
    return {k: (a[k] if rng.random() < 0.5 else b[k]) for k in keys}


def optimize(classes: pd.DataFrame, edges: pd.DataFrame, visits: pd.Series, algorithm: str, seed: int, max_modules: int = 3, population_size: int = 12, generations: int = 8) -> OptimizationResult:
    start = time.perf_counter()
    rng = random.Random(seed)
    class_ids = _classes(classes)
    if algorithm == 'RandomValidPartition':
        p = random_partition(class_ids, rng, max_modules)
        metrics = evaluate_partition(classes, edges, p, visits)
        return OptimizationResult(p, metrics, [], time.perf_counter() - start)
    if algorithm == 'FCA':
        p = _fca_partition(class_ids, edges, max_modules)
        metrics = evaluate_partition(classes, edges, p, visits)
        return OptimizationResult(p, metrics, [], time.perf_counter() - start)
    if algorithm == 'TraditionalMQ':
        p = _traditional_greedy(class_ids, edges, max_modules)
        metrics = evaluate_partition(classes, edges, p, visits)
        return OptimizationResult(p, metrics, [], time.perf_counter() - start)
    mode = 'traditional' if algorithm == 'Bunch' else 'speedup'
    pop = [random_partition(class_ids, rng, max_modules) for _ in range(population_size)]
    logs = []
    best_p = pop[0]; best_m = evaluate_partition(classes, edges, best_p, visits); best_f = _fitness(best_m, mode)
    for gen in range(generations):
        scored = []
        for p in pop:
            m = evaluate_partition(classes, edges, p, visits)
            scored.append((_fitness(m, mode), p, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        if scored[0][0] > best_f:
            best_f, best_p, best_m = scored[0]
        fits = [s[0] for s in scored]
        diversity = _diversity([s[1] for s in scored])
        logs.append({'generation': gen, 'best_fitness': best_f, 'median_fitness': sorted(fits)[len(fits)//2], 'diversity': diversity, 'elapsed_s': time.perf_counter() - start})
        new_pop = [scored[0][1], scored[1][1]]
        while len(new_pop) < population_size:
            p1 = _tournament(scored, rng)
            p2 = _tournament(scored, rng)
            child = _crossover(p1, p2, rng)
            if rng.random() < 0.30:
                child = _mutate(child, rng, max_modules)
            new_pop.append(child)
        pop = new_pop
    return OptimizationResult(best_p, best_m, logs, time.perf_counter() - start)


def _tournament(scored, rng: random.Random, k: int = 4) -> dict[str, int]:
    candidates = rng.sample(scored, k=min(k, len(scored)))
    return max(candidates, key=lambda x: x[0])[1]


def _diversity(pop: list[dict[str, int]]) -> float:
    if len(pop) < 2: return 0.0
    keys = list(pop[0].keys())
    total = 0; pairs = 0
    for i in range(len(pop)):
        for j in range(i+1, len(pop)):
            total += sum(1 for k in keys if pop[i][k] != pop[j][k]) / len(keys)
            pairs += 1
    return total / pairs if pairs else 0.0


def _fca_partition(class_ids: list[str], edges: pd.DataFrame, max_modules: int) -> dict[str, int]:
    # Greedy structural split by weighted outgoing degree.
    degree = {c: 0.0 for c in class_ids}
    for e in edges.itertuples():
        degree[str(e.caller)] += float(e.count)
        degree[str(e.callee)] += float(e.count) * 0.5
    ordered = sorted(class_ids, key=lambda c: degree[c], reverse=True)
    return {c: (i % max_modules) + 1 for i, c in enumerate(ordered)}


def _traditional_greedy(class_ids: list[str], edges: pd.DataFrame, max_modules: int) -> dict[str, int]:
    # Places heavy callers/callees together to maximize structural MQ.
    p = {c: ((i % max_modules) + 1) for i, c in enumerate(class_ids)}
    heavy = edges.sort_values('count', ascending=False).head(max_modules * 2)
    for i, e in enumerate(heavy.itertuples()):
        p[str(e.caller)] = (i % max_modules) + 1
        p[str(e.callee)] = p[str(e.caller)]
    return p
