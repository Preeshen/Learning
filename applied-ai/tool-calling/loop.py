"""A tool-calling agent loop built from scratch, with retry on malformed tool calls.

Offline by default: `FixtureModel` replays recorded (prompt -> response) pairs instead of
calling a live LLM API, per FR-034 and R-006. Swap in a real client behind the same
`generate(messages) -> ToolCallResponse` interface when a live API budget is available.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ToolCallResponse:
    tool_name: str | None
    arguments_raw: str  # the raw (possibly malformed) JSON string the model produced
    is_final_answer: bool = False
    final_answer: str | None = None


@dataclass
class ToolCallResult:
    success: bool
    retries: int
    final_answer: str | None
    error: str | None = None


class MalformedToolCallError(ValueError):
    pass


def parse_arguments(raw: str) -> dict:
    """Parse the model's raw tool-call arguments. Raise MalformedToolCallError (not ValueError
    directly) so callers can distinguish 'the model misbehaved' from any other bug."""
    raise NotImplementedError


def run_tool_loop(
    objective: str,
    generate: Callable[[list[dict]], ToolCallResponse],
    tools: dict[str, Callable[..., str]],
    max_retries: int = 2,
) -> ToolCallResult:
    """Run a single-tool-use loop: call `generate`, parse and execute the tool call, retry on
    malformed arguments up to `max_retries` times.

    The retry is the point of this exercise: a malformed tool call is a prompt-shaped bug, not a
    transient failure — simply re-sending the identical conversation reproduces the same
    malformed output, so the retry must tell the model what went wrong.
    """
    raise NotImplementedError


@dataclass
class FixtureModel:
    """Replays a scripted sequence of responses — the offline-default backend (R-006)."""

    script: list[ToolCallResponse] = field(default_factory=list)
    _index: int = 0

    def generate(self, messages: list[dict]) -> ToolCallResponse:
        response = self.script[self._index]
        self._index += 1
        return response
