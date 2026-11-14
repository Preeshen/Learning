"""Run once to produce benchmarks.json — the day-6 measurement (Principle V)."""

from __future__ import annotations

import importlib.util
import json
import random
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "tool_calling_loop", Path(__file__).resolve().parent / "loop.py"
)
loop_module = importlib.util.module_from_spec(_SPEC)
sys.modules["tool_calling_loop"] = loop_module
_SPEC.loader.exec_module(loop_module)


def _lookup_weather(city: str) -> str:
    return f"weather for {city}: sunny"


TOOLS = {"lookup_weather": _lookup_weather}


def scripted_trial(malformed_first: bool, rng: random.Random) -> loop_module.ToolCallResponse:
    if malformed_first:
        # a malformed call that *never* self-corrects in the no-retry condition
        bad_json = '{"city": "Paris"' + ("" if rng.random() < 0.5 else " ")
        return loop_module.ToolCallResponse(tool_name="lookup_weather", arguments_raw=bad_json)
    return loop_module.ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"}')


def run_trial(with_retry: bool, rng: random.Random) -> bool:
    malformed_first = rng.random() < 0.5  # 50% of trials start with a malformed call
    if with_retry:
        script = [
            scripted_trial(malformed_first, rng),
            loop_module.ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"}'),
            loop_module.ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                                          final_answer="Sunny."),
        ]
        max_retries = 2
    else:
        max_retries = 0  # no-retry baseline: give up immediately on a malformed call
        if malformed_first:
            script = [scripted_trial(True, rng)]  # loop exits on the malformed call itself
        else:
            script = [
                scripted_trial(False, rng),
                loop_module.ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                                              final_answer="Sunny."),
            ]

    model = loop_module.FixtureModel(script=script)
    result = loop_module.run_tool_loop("weather?", model.generate, TOOLS, max_retries=max_retries)
    return result.success


def main() -> None:
    rng = random.Random(0)
    trials = 20

    with_retry_successes = sum(run_trial(True, rng) for _ in range(trials))
    rng = random.Random(0)  # same malformed/clean sequence for a fair comparison
    no_retry_successes = sum(run_trial(False, rng) for _ in range(trials))

    payload = {
        "metric": "accuracy",
        "baseline": "no-retry loop (fails immediately on malformed tool call)",
        "method": "count successful completions out of 20 malformed-call trials, with and without retry",
        "trials": trials,
        "with_retry_successes": with_retry_successes,
        "no_retry_successes": no_retry_successes,
        "with_retry_success_rate": with_retry_successes / trials,
        "no_retry_success_rate": no_retry_successes / trials,
    }
    out_path = Path(__file__).resolve().parent / "benchmarks.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_path}")
    print(f"with retry: {with_retry_successes}/{trials} · no retry: {no_retry_successes}/{trials}")


if __name__ == "__main__":
    main()
