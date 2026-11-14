"""Token-cost and latency tracking for the day-6 tool-calling loop.

Wrap run_tool_loop with instrumentation rather than modifying it — the loop stays reusable
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
    raise NotImplementedError


@dataclass
class BudgetTracker:
    records: list[RequestRecord] = field(default_factory=list)

    def run_tracked(
        self, objective: str, generate, tools: dict, max_retries: int = 2
    ):
        """Wrap `generate` to record input/output token estimates and wall-clock latency per
        call into self.records, then delegate to loop_module.run_tool_loop."""
        raise NotImplementedError

    @property
    def total_cost(self) -> float:
        raise NotImplementedError

    def percentile_latency(self, p: float) -> float:
        raise NotImplementedError
