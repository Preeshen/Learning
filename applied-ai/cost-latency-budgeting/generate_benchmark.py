"""Run once to produce benchmarks.json — the day-12 measurement (Principle V)."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "budget_tracker", Path(__file__).resolve().parent / "budget_tracker.py"
)
budget_tracker = importlib.util.module_from_spec(_SPEC)
sys.modules["budget_tracker"] = budget_tracker
_SPEC.loader.exec_module(budget_tracker)

loop_module = sys.modules["tool_calling_loop"]


def _lookup_weather(city: str) -> str:
    return f"weather for {city}: sunny"


TOOLS = {"lookup_weather": _lookup_weather}


def main() -> None:
    tracker = budget_tracker.BudgetTracker()
    for _ in range(20):
        script = [
            loop_module.ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"}'),
            loop_module.ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                                          final_answer="It is 15C and overcast in Paris."),
        ]
        model = loop_module.FixtureModel(script=script)
        tracker.run_tracked("What's the weather in Paris?", model.generate, TOOLS)

    baseline_cost_per_request = 0.002  # day-6's loop, unmeasured — treated as "no visibility"
    payload = {
        "metric": "cost",
        "baseline": "day-6 tool-calling loop, unmeasured",
        "method": "run 20 requests through the loop; report total tokens, cost at list price, "
                  "and p50/p95 wall-clock latency",
        "requests": 20,
        "total_cost_usd": tracker.total_cost,
        "p50_latency_seconds": tracker.percentile_latency(0.50),
        "p95_latency_seconds": tracker.percentile_latency(0.95),
        "note": "day 6 produced a working loop with zero cost/latency visibility; this day adds "
                "the instrumentation that turns 'it works' into 'it costs $X and runs in Yms,' "
                "which is the difference between a demo and something you'd put a budget alert on.",
    }
    out_path = Path(__file__).resolve().parent / "benchmarks.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_path}")
    print(f"total cost: ${tracker.total_cost:.6f} · p50: {tracker.percentile_latency(0.50)*1000:.2f}ms "
          f"· p95: {tracker.percentile_latency(0.95)*1000:.2f}ms")


if __name__ == "__main__":
    main()
