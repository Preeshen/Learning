"""Contract tests for the roadmap CLI, against the live week-1 fixture + progress state."""

from __future__ import annotations

import json
import time

from datetime import date

from typer.testing import CliRunner

from tools.roadmap_cli.cli import app
from tools.roadmap_cli.loader import topics_due
from tools.roadmap_cli.models import DayProgress, ProgressRecord, ProgressStatus, Topic

runner = CliRunner()


def _fake_roadmap_with_topics(topics: dict[str, Topic]):
    from tools.roadmap_cli.models import Roadmap

    return Roadmap(
        version=1, start_date=date(2026, 11, 16), end_date=date(2027, 1, 24), total_days=70,
        weekday_hours=4, weekend_hours=6, primary_role="agentic-ai", secondary_role="fde",
        domains={}, roles={}, topics=topics, weeks=[], milestones=[], interview_imminent_plan={},
    )


def test_today_runs_under_one_second():
    start = time.perf_counter()
    result = runner.invoke(app, ["today"])
    elapsed = time.perf_counter() - start
    assert result.exit_code == 0
    assert elapsed < 1.0


def test_today_json():
    result = runner.invoke(app, ["today", "1", "--json"])
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


def test_topics_due_includes_topic_whose_interval_has_elapsed():
    # T033: a topic is "due" once first_day + resurface_after[n] <= completed-day count.
    topics = {
        "t1": Topic(id="t1", name="T1", domain="dsa", first_day=2, resurface_after=[7, 21]),
        "t2": Topic(id="t2", name="T2", domain="dsa", first_day=5, resurface_after=[7, 21]),
    }
    roadmap = _fake_roadmap_with_topics(topics)
    # 9 completed days: t1's first_day(2) + resurface_after[0](7) = 9 <= 9 -> due.
    # t2's first_day(5) + 7 = 12 > 9 -> not due.
    progress = ProgressRecord(
        version=1, roadmap_version=1, started=date(2026, 11, 16),
        entries=[
            DayProgress(day=i, status=ProgressStatus.COMPLETE, date=date(2026, 11, 16))
            for i in range(1, 10)
        ],
    )
    assert topics_due(roadmap, progress) == ["t1"]


def test_topics_due_empty_when_nothing_due():
    topics = {"t1": Topic(id="t1", name="T1", domain="dsa", first_day=1, resurface_after=[7, 21])}
    roadmap = _fake_roadmap_with_topics(topics)
    progress = ProgressRecord(version=1, roadmap_version=1, started=date(2026, 11, 16), entries=[])
    assert topics_due(roadmap, progress) == []


def test_check_day1_all_pass():
    result = runner.invoke(app, ["check", "1"])
    assert result.exit_code == 0
    assert "day complete" in result.stdout


def test_validate_strict_exits_zero_against_the_complete_roadmap():
    # All 10 weeks are now authored; roadmap validate --strict must pass clean (quickstart S-1).
    result = runner.invoke(app, ["validate", "--strict"])
    assert result.exit_code == 0
    assert "0 error(s), 0 warning(s)" in result.stdout


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


def test_review_writes_generated_section_and_refuses_overwrite(tmp_path, monkeypatch):
    import tools.roadmap_cli.cli as cli_module
    import tools.roadmap_cli.loader as loader_module

    fixture_progress = tmp_path / "progress.yaml"
    fixture_progress.write_text(
        "version: 1\nroadmap_version: 1\nstarted: '2026-11-16'\nentries: []\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        cli_module, "load_progress", lambda: loader_module.load_progress(fixture_progress)
    )

    out_path = cli_module.REPO_ROOT / "progress" / "reviews" / "week-01.md"
    if out_path.exists():
        out_path.unlink()

    result = runner.invoke(app, ["review", "1"])
    assert result.exit_code == 0
    assert out_path.exists()
    content = out_path.read_text(encoding="utf-8")
    assert "## Generated" in content
    assert "Completed:" in content

    # Re-running without --regenerate must refuse.
    result2 = runner.invoke(app, ["review", "1"])
    assert result2.exit_code == 1
    out_path.unlink()


def test_review_three_of_seven_days_skipped_names_recovery_point(tmp_path, monkeypatch):
    """T041: simulate a week with 3 of 7 days missed; review must name the recovery rule
    and a re-entry point rather than silently accumulating a backlog (SC-006)."""
    import tools.roadmap_cli.cli as cli_module
    import tools.roadmap_cli.loader as loader_module

    fixture_progress = tmp_path / "progress.yaml"
    fixture_progress.write_text(
        "version: 1\nroadmap_version: 1\nstarted: '2026-11-16'\nentries:\n"
        "- {day: 1, status: skipped, date: '2026-11-16', journal_ref: day-001}\n"
        "- {day: 2, status: skipped, date: '2026-11-17', journal_ref: day-002}\n"
        "- {day: 3, status: skipped, date: '2026-11-18', journal_ref: day-003}\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        cli_module, "load_progress", lambda: loader_module.load_progress(fixture_progress)
    )

    out_path = cli_module.REPO_ROOT / "progress" / "reviews" / "week-01.md"
    if out_path.exists():
        out_path.unlink()

    result = runner.invoke(app, ["review", "1"])
    assert result.exit_code == 0
    content = out_path.read_text(encoding="utf-8")
    assert "consecutive days skipped" in content
    assert "Re-entry point: day 4" in content
    out_path.unlink()


def test_coverage_lists_unmet_milestone_prerequisite_days():
    result = runner.invoke(app, ["coverage", "--json"])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    milestones = payload["milestones"]
    assert len(milestones) == 3
    for m in milestones:
        assert "unmet_prerequisite_days" in m
        if not m["ready"]:
            assert len(m["unmet_prerequisite_days"]) > 0


def test_render_check_passes_when_in_sync():
    runner.invoke(app, ["render"])
    result = runner.invoke(app, ["render", "--check"])
    assert result.exit_code == 0
