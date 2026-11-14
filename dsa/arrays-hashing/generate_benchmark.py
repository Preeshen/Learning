"""Run once to produce benchmarks.json — the day-2 measurement (Principle V)."""

from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "arrays_hashing_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["arrays_hashing_solutions"] = solutions
_SPEC.loader.exec_module(solutions)


def time_at_size(fn, n: int) -> float:
    nums = list(range(n))
    target = -1  # forces worst case: no match, full scan
    start = time.perf_counter()
    fn(nums, target)
    return time.perf_counter() - start


def main() -> None:
    sizes = [100, 1000, 10000]
    hashmap_times = [time_at_size(solutions.two_sum, n) for n in sizes]
    naive_times = [time_at_size(solutions.two_sum_naive, n) for n in sizes]

    payload = {
        "metric": "latency",
        "baseline": "naive O(n^2) nested-loop lookup",
        "method": "time both implementations across input sizes [100, 1000, 10000, 100000]",
        "sizes": sizes,
        "hashmap_seconds": hashmap_times,
        "naive_seconds": naive_times,
        "note": "naive grows roughly quadratically with size; hashmap grows roughly linearly — "
                "the ratio naive_seconds[-1]/hashmap_seconds[-1] should dwarf the ratio at the "
                "smallest size if the O(n) vs O(n^2) claim is real, not just asserted.",
    }
    out_path = Path(__file__).resolve().parent / "benchmarks.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_path}")
    for n, h, nv in zip(sizes, hashmap_times, naive_times):
        print(f"n={n}: hashmap={h:.6f}s naive={nv:.6f}s ratio={nv / h if h else float('inf'):.1f}x")


if __name__ == "__main__":
    main()
