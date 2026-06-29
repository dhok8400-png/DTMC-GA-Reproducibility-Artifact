from __future__ import annotations
import csv
from pathlib import Path
from typing import Iterable


def read_csv(path: str | Path) -> list[dict[str, str]]:
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def ensure_columns(rows: Iterable[dict[str, str]], required: set[str]) -> None:
    rows = list(rows)
    if not rows:
        return
    missing = required - set(rows[0].keys())
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
