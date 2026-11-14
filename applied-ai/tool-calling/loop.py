"""A tool-calling agent loop built from scratch, with retry on malformed tool calls.

Offline by default: `FixtureModel` replays recorded (prompt -> response) pairs instead of
calling a live LLM API, per FR-034 and R-006. Swap in a real client behind the same
`generate(messages) -> ToolCallResponse` interface when a live API budget is available.
"""

from __future__ import annotations

import json
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
    """Parse the model's raw tool-call arguments. Raises MalformedToolCallError, not ValueError
    directly, so callers can distinguish 'the model misbehaved' from any other bug."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise MalformedToolCallError(f"invalid JSON arguments: {raw!r}") from exc


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
    messages = [{"role": "user", "content": objective}]
    retries = 0

    while True:
        response = generate(messages)

        if response.is_final_answer:
            return ToolCallResult(success=True, retries=retries, final_answer=response.final_answer)

        if response.tool_name not in tools:
            return ToolCallResult(
                success=False, retries=retries, final_answer=None,
                error=f"unknown tool: {response.tool_name}",
            )

        try:
            args = parse_arguments(response.arguments_raw)
        except MalformedToolCallError as exc:
            retries += 1
            if retries > max_retries:
                return ToolCallResult(
                    success=False, retries=retries, final_answer=None,
                    error=f"gave up after {max_retries} retries: {exc}",
                )
            # Tell the model what broke — a bare retry would just reproduce the same error.
            messages.append({"role": "assistant", "content": f"tool_call: {response.tool_name}({response.arguments_raw})"})
            messages.append({"role": "user", "content": f"Error: {exc}. Fix the arguments and retry."})
            continue

        tool_fn = tools[response.tool_name]
        result = tool_fn(**args)
        messages.append({"role": "assistant", "content": f"tool_call: {response.tool_name}({args})"})
        messages.append({"role": "user", "content": f"Tool result: {result}"})
        # A fixture-backed run always terminates because FixtureModel's script is finite;
        # a live model would be prompted to decide whether to call another tool or answer.


@dataclass
class FixtureModel:
    """Replays a scripted sequence of responses — the offline-default backend (R-006)."""

    script: list[ToolCallResponse] = field(default_factory=list)
    _index: int = 0

    def generate(self, messages: list[dict]) -> ToolCallResponse:
        response = self.script[self._index]
        self._index += 1
        return response
