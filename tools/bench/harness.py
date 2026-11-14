"""Shared timing/memory/baseline-comparison helper for benchmarks.json (Principle V)."""

from __future__ import annotations

import json
import time
import tracemalloc
from pathlib import Path
from typing import Any, Callable


def time_it(fn: Callable[[], Any], repeats: int = 5) -> float:
    """Return the median wall-clock seconds across `repeats` calls."""
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        fn()
        samples.append(time.perf_counter() - start)
    samples.sort()
    return samples[len(samples) // 2]


def memory_of(fn: Callable[[], Any]) -> int:
    """Return peak traced memory in bytes while running `fn` once."""
    tracemalloc.start()
    try:
        fn()
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return peak


def write_benchmark(
    path: Path,
    metric: str,
    baseline: str,
    method: str,
    result: float,
    baseline_result: float | None = None,
    unit: str = "seconds",
) -> None:
    """Commit a measurement to `<topic>/benchmarks.json`, matching Measurement's contract."""
    payload = {
        "metric": metric,
        "baseline": baseline,
        "method": method,
        "result": result,
        "unit": unit,
    }
    if baseline_result is not None:
        payload["baseline_result"] = baseline_result
        if baseline_result:
            payload["improvement_ratio"] = baseline_result / result if result else None
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
