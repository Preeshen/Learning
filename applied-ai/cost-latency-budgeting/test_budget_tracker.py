import importlib.util
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


def test_estimate_tokens_roughly_4_chars_per_token():
    assert budget_tracker.estimate_tokens("a" * 40) == 10


def test_estimate_tokens_minimum_one():
    assert budget_tracker.estimate_tokens("") == 1


def test_run_tracked_records_one_entry_per_generate_call():
    script = [
        loop_module.ToolCallResponse(tool_name="lookup_weather", arguments_raw='{"city": "Paris"}'),
        loop_module.ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                                      final_answer="Sunny."),
    ]
    model = loop_module.FixtureModel(script=script)
    tracker = budget_tracker.BudgetTracker()
    result = tracker.run_tracked("weather?", model.generate, TOOLS)

    assert result.success
    assert len(tracker.records) == 2


def test_total_cost_is_positive_after_a_run():
    script = [
        loop_module.ToolCallResponse(tool_name=None, arguments_raw="", is_final_answer=True,
                                      final_answer="Done."),
    ]
    model = loop_module.FixtureModel(script=script)
    tracker = budget_tracker.BudgetTracker()
    tracker.run_tracked("objective", model.generate, TOOLS)

    assert tracker.total_cost > 0


def test_percentile_latency_empty_is_zero():
    tracker = budget_tracker.BudgetTracker()
    assert tracker.percentile_latency(0.95) == 0.0
