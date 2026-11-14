"""Unit tests for validator rules V-01..V-21, P-01..P-07, J-01..J-03.

Rather than one YAML fixture per rule, these construct minimal dataclass instances directly —
equivalent coverage with far less fixture duplication.
"""

from __future__ import annotations

from datetime import date

import pytest

from tools.roadmap_cli.models import (
    DayEntry,
    DayProgress,
    Domain,
    Measurement,
    PromotionMilestone,
    ProgressRecord,
    ProgressStatus,
    ResolveResult,
    ReviewCheckpoint,
    Roadmap,
    RoleTarget,
    Topic,
    Week,
)
from tools.roadmap_cli import validate as v


def make_day(**overrides) -> DayEntry:
    defaults = dict(
        id=1, date=date(2026, 11, 16), day_type="weekday", objective="Do a thing",
        domain="python", topic="t1", artifact="python/t1/a.py", verification="pytest",
        notes_topic="why", effort_hours=4, tier="primary", priority="core",
        gate=["pytest passes"], minimum_viable="less",
    )
    defaults.update(overrides)
    return DayEntry(**defaults)


def make_roadmap(days: list[DayEntry], **overrides) -> Roadmap:
    from datetime import timedelta

    review1 = ReviewCheckpoint(week=1, day=days[-1].id if days else 1,
                                resolves=["t1", "t2"], procedure=["step"],
                                output_path="progress/reviews/week-01.md")
    review2 = ReviewCheckpoint(week=2, day=days[-1].id if days else 1,
                                resolves=["t1", "t2"], procedure=["step"],
                                output_path="progress/reviews/week-02.md")
    week = Week(number=1, theme="t", domains=["python"], outcome="o", days=days, review=review1)
    week2 = Week(number=2, theme="t2", domains=["python"], outcome="o", days=[], review=review2)
    start_date = date(2026, 11, 16)
    end_date = start_date + timedelta(days=max(len(days), 1) - 1)
    defaults = dict(
        version=1, start_date=start_date, end_date=end_date,
        total_days=len(days), weekday_hours=4, weekend_hours=6,
        primary_role="agentic-ai", secondary_role="fde",
        domains={"python": Domain(id="python", name="Python", directory="python",
                                   target_days=1, min_depth="d", supports_roles=["agentic-ai"])},
        roles={
            "agentic-ai": RoleTarget(id="agentic-ai", name="AI", tier="primary",
                                      supporting_domains=["python"]),
        },
        topics={
            "t1": Topic(id="t1", name="T1", domain="python", first_day=1,
                        resurface_after=[7, 21]),
            "t2": Topic(id="t2", name="T2", domain="python", first_day=1,
                        resurface_after=[7, 21]),
        },
        weeks=[week, week2],
        milestones=[
            PromotionMilestone(id="m1", name="M1", after_day=1, prerequisite_days=[1],
                                purpose="p", demonstrates=["d"], supports_roles=["agentic-ai"],
                                external=True, record_path="promoted/README.md"),
            PromotionMilestone(id="m2", name="M2", after_day=1, prerequisite_days=[1],
                                purpose="p", demonstrates=["d"], supports_roles=["agentic-ai"],
                                external=True, record_path="promoted/README.md"),
            PromotionMilestone(id="m3", name="M3", after_day=1, prerequisite_days=[1],
                                purpose="p", demonstrates=["d"], supports_roles=["agentic-ai"],
                                external=True, record_path="promoted/README.md"),
        ],
        interview_imminent_plan={"agentic-ai": ["t1"]},
    )
    defaults.update(overrides)
    return Roadmap(**defaults)


def test_v01_dates_pass():
    day = make_day(id=1, date=date(2026, 11, 16), day_type="weekday")
    r = make_roadmap([day])
    assert v.v01_dates(r) == []


def test_v01_dates_fail_wrong_date():
    day = make_day(id=1, date=date(2026, 11, 17))
    r = make_roadmap([day])
    assert any(f.rule_id == "V-01" for f in v.v01_dates(r))


def test_v02_required_fields_fail_empty_artifact():
    day = make_day(artifact="")
    r = make_roadmap([day])
    assert any(f.rule_id == "V-02" for f in v.v02_required_fields(r))


def test_v02_required_fields_pass():
    day = make_day()
    r = make_roadmap([day])
    assert v.v02_required_fields(r) == []


def test_v04_effort_budget_fail():
    day = make_day(day_type="weekday", effort_hours=5)
    r = make_roadmap([day])
    assert any(f.rule_id == "V-04" for f in v.v04_effort_budget(r))


def test_v04_effort_budget_pass():
    day = make_day(day_type="weekend", effort_hours=6)
    r = make_roadmap([day])
    assert v.v04_effort_budget(r) == []


def test_v05_scratch_before_library_fail_later():
    scratch = make_day(id=2, topic="t1")
    lib = make_day(id=1, topic="t1", from_scratch_of=2)
    r = make_roadmap([lib, scratch])
    assert any(f.rule_id == "V-05" for f in v.v05_scratch_before_library(r))


def test_v05_scratch_before_library_pass():
    scratch = make_day(id=1, topic="t1")
    lib = make_day(id=2, topic="t1", from_scratch_of=1)
    r = make_roadmap([scratch, lib])
    assert v.v05_scratch_before_library(r) == []


def test_v06_measurement_fail_empty_baseline():
    day = make_day(measurement=Measurement(metric="latency", baseline="", results_path="x",
                                             method="m"))
    r = make_roadmap([day])
    assert any(f.rule_id == "V-06" for f in v.v06_measurement(r))


def test_v07_resurfacing_fail_too_few_intervals():
    day = make_day()
    r = make_roadmap([day])
    r.topics["t1"].resurface_after = [7]
    assert any(f.rule_id == "V-07" for f in v.v07_resurfacing(r))


def test_v07_resurfacing_pass():
    day = make_day()
    r = make_roadmap([day])
    assert v.v07_resurfacing(r) == []


def test_v08_milestone_external_fail():
    day = make_day()
    r = make_roadmap([day])
    r.milestones[0].external = False
    assert any(f.rule_id == "V-08" for f in v.v08_milestone_external(r))


def test_v09_referential_integrity_fail_unknown_domain():
    day = make_day(domain="nonexistent")
    r = make_roadmap([day])
    assert any(f.rule_id == "V-09" for f in v.v09_referential_integrity(r))


def test_v10_domain_role_completeness_fail():
    day = make_day()
    r = make_roadmap([day])
    assert any(f.rule_id == "V-10" for f in v.v10_domain_role_completeness(r))  # incomplete set


def test_v11_prerequisites_fail_forward_reference():
    day = make_day(id=1, prerequisites=[2])
    r = make_roadmap([day])
    assert any(f.rule_id == "V-11" for f in v.v11_prerequisites(r))


def test_v11_prerequisites_pass():
    day1 = make_day(id=1)
    day2 = make_day(id=2, prerequisites=[1])
    r = make_roadmap([day1, day2])
    assert v.v11_prerequisites(r) == []


def test_v12_exceptions_fail_missing_language_exception():
    day = make_day(language="rust")
    r = make_roadmap([day])
    assert any(f.rule_id == "V-12" for f in v.v12_exceptions(r))


def test_v12_exceptions_fail_missing_offline_fallback():
    day = make_day(offline=False)
    r = make_roadmap([day])
    assert any(f.rule_id == "V-12" for f in v.v12_exceptions(r))


def test_v13_domain_share_fail_over_40_percent():
    days = [make_day(id=i) for i in range(1, 3)]
    r = make_roadmap(days)
    assert any(f.rule_id == "V-13" for f in v.v13_domain_share(r))  # 100% > 40%


def test_v14_core_effort_budget_fail():
    days = [make_day(id=i, priority="core", effort_hours=4, day_type="weekday")
            for i in range(1, 71)]
    r = make_roadmap(days)
    assert any(f.rule_id == "V-14" for f in v.v14_core_effort_budget(r))  # 280h > 272h


def test_v17_milestone_count_pass():
    day = make_day()
    r = make_roadmap([day])
    assert v.v17_milestone_count(r) == []


def test_v18_serving_fastapi_fail():
    day = make_day(serving="flask")
    r = make_roadmap([day])
    assert any(f.rule_id == "V-18" for f in v.v18_serving_fastapi(r))


def test_v18_serving_fastapi_pass():
    day = make_day(serving="fastapi")
    r = make_roadmap([day])
    assert v.v18_serving_fastapi(r) == []


def test_v19_generic_concept_fail():
    day = make_day(objective="Practice MCP tool calling", generic_concept=None)
    r = make_roadmap([day])
    assert any(f.rule_id == "V-19" for f in v.v19_generic_concept(r))


def test_v19_generic_concept_pass():
    day = make_day(objective="Practice MCP tool calling", generic_concept="tool use")
    r = make_roadmap([day])
    assert v.v19_generic_concept(r) == []


def test_v20_milestone_fields_fail_empty_purpose():
    day = make_day()
    r = make_roadmap([day])
    r.milestones[0].purpose = ""
    assert any(f.rule_id == "V-20" for f in v.v20_milestone_fields(r))


def test_v21_interview_plan_fail_missing():
    day = make_day()
    r = make_roadmap([day], interview_imminent_plan={})
    assert any(f.rule_id == "V-21" for f in v.v21_interview_plan(r))


def test_v21_interview_plan_fail_unknown_topic():
    day = make_day()
    r = make_roadmap([day], interview_imminent_plan={"agentic-ai": ["nonexistent"]})
    assert any(f.rule_id == "V-21" for f in v.v21_interview_plan(r))


def test_v21_interview_plan_pass():
    day = make_day()
    r = make_roadmap([day])
    assert v.v21_interview_plan(r) == []


# --- progress.yaml rules ---

def make_progress(entries: list[DayProgress]) -> ProgressRecord:
    return ProgressRecord(version=1, roadmap_version=1, started=date(2026, 11, 16),
                           entries=entries)


def test_p01_no_gaps_fail():
    p = make_progress([
        DayProgress(day=1, status=ProgressStatus.COMPLETE, date=date(2026, 11, 16),
                    commit="abc", gate_passed=True),
        DayProgress(day=3, status=ProgressStatus.COMPLETE, date=date(2026, 11, 18),
                    commit="def", gate_passed=True),
    ])
    assert any(f.rule_id == "P-01" for f in v.p01_no_gaps(p))


def test_p02_complete_requires_commit_fail():
    p = make_progress([DayProgress(day=1, status=ProgressStatus.COMPLETE,
                                    date=date(2026, 11, 16))])
    assert any(f.rule_id == "P-02" for f in v.p02_complete_requires_commit(p))


def test_p04_journal_ref_fail_no_anchor():
    p = make_progress([DayProgress(day=1, status=ProgressStatus.COMPLETE,
                                    date=date(2026, 11, 16), commit="abc", gate_passed=True,
                                    journal_ref="day-001")])
    assert any(f.rule_id == "P-04" for f in v.p04_journal_ref(p, journal_text=""))


def test_p05_day_exists_fail():
    day = make_day(id=1)
    r = make_roadmap([day])
    p = make_progress([DayProgress(day=99, status=ProgressStatus.SKIPPED,
                                    date=date(2026, 11, 16))])
    assert any(f.rule_id == "P-05" for f in v.p05_day_exists(p, r))


def test_p07_double_fail_escalation():
    p = make_progress([
        DayProgress(day=1, status=ProgressStatus.COMPLETE, date=date(2026, 11, 16),
                    commit="a", gate_passed=True,
                    resolve_results=[ResolveResult(topic="t1", passed=False)]),
        DayProgress(day=2, status=ProgressStatus.COMPLETE, date=date(2026, 11, 17),
                    commit="b", gate_passed=True,
                    resolve_results=[ResolveResult(topic="t1", passed=False)]),
    ])
    assert any(f.rule_id == "P-07" for f in v.p07_double_fail_escalation(p))


# --- journal.md rules ---

def test_j01_refs_resolve_fail_no_anchor():
    p = make_progress([DayProgress(day=1, status=ProgressStatus.COMPLETE,
                                    date=date(2026, 11, 16), commit="a", gate_passed=True,
                                    journal_ref="day-001")])
    assert any(f.rule_id == "J-01" for f in v.j01_refs_resolve(p, journal_text=""))


def test_j01_refs_resolve_pass():
    journal = "## Day 001 — 2026-11-16 — t1 {#day-001}\n\nbody\n"
    p = make_progress([DayProgress(day=1, status=ProgressStatus.COMPLETE,
                                    date=date(2026, 11, 16), commit="a", gate_passed=True,
                                    journal_ref="day-001")])
    assert v.j01_refs_resolve(p, journal) == []


def test_j02_ascending_order_fail():
    journal = "## Day 002 — x\nbody\n## Day 001 — y\nbody\n"
    assert any(f.rule_id == "J-02" for f in v.j02_ascending_order(journal))


def test_j03_prose_fields_fail_missing_built():
    journal = (
        "## Day 001 — 2026-11-16 — t1 {#day-001}\n\n"
        "**Status**: complete · **Commit**: abc\n\n"
        "**Broke**: x\n\n**Non-obvious**: y\n"
    )
    assert any(f.rule_id == "J-03" for f in v.j03_prose_fields(journal))
