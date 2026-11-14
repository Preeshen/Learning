"""Token-cost and latency tracking for the day-6 tool-calling loop.

Wraps run_tool_loop with instrumentation rather than modifying it — the loop stays reusable
without a tracking dependency baked in.
"""

from __future__ import annotations

import importlib.util
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

_LOOP_SPEC = importlib.util.spec_from_file_location(
    "tool_calling_loop",
    Path(__file__).resolve().parents[1] / "tool-calling" / "loop.py",
)
loop_module = importlib.util.module_from_spec(_LOOP_SPEC)
sys.modules["tool_calling_loop"] = loop_module
_LOOP_SPEC.loader.exec_module(loop_module)


# List prices as of this day's measurement — illustrative, not live-fetched (FR-034: offline).
COST_PER_1K_INPUT_TOKENS = 0.003
COST_PER_1K_OUTPUT_TOKENS = 0.015


@dataclass
class RequestRecord:
    input_tokens: int
    output_tokens: int
    latency_seconds: float

    @property
    def cost(self) -> float:
        return (
            (self.input_tokens / 1000) * COST_PER_1K_INPUT_TOKENS
            + (self.output_tokens / 1000) * COST_PER_1K_OUTPUT_TOKENS
        )


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 characters per token for English text.

    Good enough for budgeting, not accurate enough for billing — a real deployment would use
    the provider's tokenizer.
    """
    return max(1, len(text) // 4)


@dataclass
class BudgetTracker:
    records: list[RequestRecord] = field(default_factory=list)

    def run_tracked(
        self, objective: str, generate, tools: dict, max_retries: int = 2
    ):
        messages_seen = {"input_chars": 0, "output_chars": 0}

        def tracked_generate(messages: list[dict]):
            for m in messages:
                messages_seen["input_chars"] += len(m["content"])
            start = time.perf_counter()
            response = generate(messages)
            elapsed = time.perf_counter() - start
            output_text = response.final_answer or response.arguments_raw or ""
            messages_seen["output_chars"] += len(output_text)
            self.records.append(RequestRecord(
                input_tokens=estimate_tokens(" ".join(m["content"] for m in messages)),
                output_tokens=estimate_tokens(output_text),
                latency_seconds=elapsed,
            ))
            return response

        return loop_module.run_tool_loop(objective, tracked_generate, tools, max_retries)

    @property
    def total_cost(self) -> float:
        return sum(r.cost for r in self.records)

    def percentile_latency(self, p: float) -> float:
        if not self.records:
            return 0.0
        latencies = sorted(r.latency_seconds for r in self.records)
        idx = min(len(latencies) - 1, int(len(latencies) * p))
        return latencies[idx]
