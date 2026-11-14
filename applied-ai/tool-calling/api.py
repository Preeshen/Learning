"""FastAPI wrapper exposing the tool-calling loop as a service (FR-030a).

Run with: uv run uvicorn applied_ai.tool_calling.api:app --reload
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

_SPEC = importlib.util.spec_from_file_location(
    "tool_calling_loop", Path(__file__).resolve().parent / "loop.py"
)
loop_module = importlib.util.module_from_spec(_SPEC)
sys.modules["tool_calling_loop"] = loop_module
_SPEC.loader.exec_module(loop_module)

app = FastAPI(title="Tool-calling loop", version="0.1.0")


def _lookup_weather(city: str) -> str:
    fixtures = {"paris": "15C, overcast", "tokyo": "22C, clear"}
    return fixtures.get(city.lower(), "unknown city")


TOOLS = {"lookup_weather": _lookup_weather}


class RunRequest(BaseModel):
    objective: str


class RunResponse(BaseModel):
    success: bool
    retries: int
    final_answer: str | None
    error: str | None


@app.post("/run", response_model=RunResponse)
def run(request: RunRequest) -> RunResponse:
    """Runs the loop against a fixture model scripted for a single weather lookup.

    A real deployment would route `generate` to a live LLM client; this endpoint exists to
    prove the loop is served over HTTP, not to be a general-purpose agent API.
    """
    responses = [
        loop_module.ToolCallResponse(
            tool_name="lookup_weather", arguments_raw='{"city": "Paris"}'
        ),
        loop_module.ToolCallResponse(
            tool_name=None, arguments_raw="", is_final_answer=True,
            final_answer="It is 15C and overcast in Paris.",
        ),
    ]
    model = loop_module.FixtureModel(script=responses)
    result = loop_module.run_tool_loop(request.objective, model.generate, TOOLS)
    return RunResponse(
        success=result.success, retries=result.retries,
        final_answer=result.final_answer, error=result.error,
    )


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
