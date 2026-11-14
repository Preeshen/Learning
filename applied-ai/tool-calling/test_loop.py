import importlib.util
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

_SPEC = importlib.util.spec_from_file_location(
    "tool_calling_loop", Path(__file__).resolve().parent / "loop.py"
)
loop_module = importlib.util.module_from_spec(_SPEC)
sys.modules["tool_calling_loop"] = loop_module
_SPEC.loader.exec_module(loop_module)

_API_SPEC = importlib.util.spec_from_file_location(
    "tool_calling_api", Path(__file__).resolve().parent / "api.py"
)
api_module = importlib.util.module_from_spec(_API_SPEC)
sys.modules["tool_calling_api"] = api_module
_API_SPEC.loader.exec_module(api_module)

ToolCallResponse = loop_module.ToolCallResponse
FixtureModel = loop_module.FixtureModel
run_tool_loop = loop_module.run_tool_loop
parse_arguments = loop_module.parse_arguments
MalformedToolCallError = loop_module.MalformedToolCallError


def _lookup_weather(city: str) -> str:
    return f"weather for {city}: sunny"


TOOLS = {"lookup_weather": _lookup_weather}


def test_parse_arguments_valid_json():
    assert parse_arguments('{"city": "Paris"}') == {"city": "Paris"}


def test_parse_arguments_malformed_raises():
    with pytest.raises(MalformedToolCallError):
        parse_arguments('{"city": "Paris"')  # missing closing brace


def test_happy_path_single_tool_call():
    script = [
        ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"}'),
        ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                          final_answer="It's sunny in Paris."),
    ]
    model = FixtureModel(script=script)
    result = run_tool_loop("What's the weather in Paris?", model.generate, TOOLS)
    assert result.success
    assert result.retries == 0
    assert result.final_answer == "It's sunny in Paris."


# --- the 3 malformed-call cases the gate requires ---

def test_malformed_call_recovers_on_retry():
    """Case 1: malformed JSON once, then the model corrects itself."""
    script = [
        ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"'),  # malformed
        ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"}'),  # fixed
        ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                          final_answer="Sunny."),
    ]
    model = FixtureModel(script=script)
    result = run_tool_loop("weather?", model.generate, TOOLS)
    assert result.success
    assert result.retries == 1


def test_malformed_call_gives_up_after_max_retries():
    """Case 2: the model never recovers; the loop must give up rather than retry forever."""
    script = [
        ToolCallResponse(tool_name="lookup_weather", arguments_raw="not json")
        for _ in range(5)
    ]
    model = FixtureModel(script=script)
    result = run_tool_loop("weather?", model.generate, TOOLS, max_retries=2)
    assert not result.success
    assert result.retries == 3  # initial + 2 retries before giving up
    assert "gave up" in result.error


def test_malformed_call_unknown_tool_name():
    """Case 3: a different malformed-call shape — a tool name the model hallucinated."""
    script = [ToolCallResponse(tool_name="forecast_weather_v2", arguments_raw="{}")]
    model = FixtureModel(script=script)
    result = run_tool_loop("weather?", model.generate, TOOLS)
    assert not result.success
    assert "unknown tool" in result.error


# --- FastAPI wrapper (FR-030a) ---

client = TestClient(api_module.app)


def test_api_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_run_endpoint():
    response = client.post("/run", json={"objective": "What's the weather in Paris?"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    assert "Paris" in payload["final_answer"]
