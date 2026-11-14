"""Contract tests for the roadmap CLI, against the live week-1 fixture + progress state."""

from __future__ import annotations

import json
import time

from typer.testing import CliRunner

from tools.roadmap_cli.cli import app

runner = CliRunner()


def test_today_runs_under_one_second():
    start = time.perf_counter()
    result = runner.invoke(app, ["today"])
    elapsed = time.perf_counter() - start
    assert result.exit_code == 0
    assert elapsed < 1.0


def test_today_json():
    result = runner.invoke(app, ["today", "--json"])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert "day" in payload
    assert "artifact" in payload


def test_today_specific_day():
    result = runner.invoke(app, ["today", "3"])
    assert result.exit_code == 0
    assert "Day 3" in result.stdout


def test_today_next_n():
    result = runner.invoke(app, ["today", "1", "--next", "3", "--json"])
    assert result.exit_code == 0
    days = json.loads(result.stdout)
    assert days == [1, 2, 3]


def test_today_days_until_interview():
    result = runner.invoke(app, ["today", "--days-until-interview", "3"])
    assert result.exit_code == 0
    assert "drill" in result.stdout.lower()


def test_check_day1_all_pass():
    result = runner.invoke(app, ["check", "1"])
    assert result.exit_code == 0
    assert "day complete" in result.stdout


def test_validate_exits_nonzero_on_missing_days():
    # Week-1-only fixture is intentionally incomplete (1 of 10 weeks) — V-03 must fire.
    result = runner.invoke(app, ["validate"])
    assert result.exit_code == 1
    assert "V-03" in result.stdout


def test_coverage_table():
    result = runner.invoke(app, ["coverage"])
    assert result.exit_code == 0
    assert "Readiness" in result.stdout


def test_coverage_role_detail():
    result = runner.invoke(app, ["coverage", "--role", "agentic-ai", "--json"])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert payload["role_id"] == "agentic-ai"
    assert "days" in payload


def test_render_check_passes_when_in_sync():
    runner.invoke(app, ["render"])
    result = runner.invoke(app, ["render", "--check"])
    assert result.exit_code == 0
