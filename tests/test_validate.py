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
from tools.roadmap_cli.validate import REPO_ROOT


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


def test_v15_tier_split_fail_when_outside_tolerance():
    # All days tier=primary -> 100% primary, 0% secondary/remaining: all three tiers miss
    # their target by more than +-5 points.
    days = [make_day(id=i, tier="primary") for i in range(1, 11)]
    r = make_roadmap(days)
    findings = v.v15_tier_split(r)
    fired_tiers = {f.message.split(":")[0].split()[-1] for f in findings if f.rule_id == "V-15"}
    assert {"primary", "secondary", "remaining"} <= fired_tiers


def test_v15_tier_split_pass_within_tolerance():
    # 6 primary / 3 secondary / 1 remaining = 60/30/10 -- secondary is 5 points over (30 vs 25,
    # within tolerance), remaining is 5 points under (10 vs 15, within tolerance).
    days = (
        [make_day(id=i, tier="primary") for i in range(1, 7)]
        + [make_day(id=i, tier="secondary") for i in range(7, 10)]
        + [make_day(id=10, tier="remaining")]
    )
    r = make_roadmap(days)
    assert v.v15_tier_split(r) == []


def test_week1_front_loads_python_and_dsa_ahead_of_lower_priority_domains():
    """T050/FR-031/FR-033: the live roadmap.yaml's week 1 theme must advance python/dsa
    (front-loaded per the primary role's needs) rather than lower-priority domains."""
    from tools.roadmap_cli.loader import load_roadmap

    live_roadmap = load_roadmap()
    week1 = next(w for w in live_roadmap.weeks if w.number == 1)
    assert "python" in week1.domains
    assert "dsa" in week1.domains
    # Lower-priority-for-primary-role domains (git) are not what week 1 is themed around.
    assert "git" not in week1.domains or len(week1.domains) > 2


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
    """A compliant plan: >=6 topics spanning >=3 domains (FR-026 as amended)."""
    r = make_roadmap([make_day()])
    for tid, dom in [("t3", "dsa"), ("t4", "dsa"), ("t5", "systems"), ("t6", "systems")]:
        r.topics[tid] = Topic(id=tid, name=tid.upper(), domain=dom, first_day=1,
                              resurface_after=[7, 21])
    r.interview_imminent_plan = {"agentic-ai": ["t1", "t2", "t3", "t4", "t5", "t6"]}
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


# ---------------------------------------------------------------------------
# Constitution v1.1.0 amendment rules (V-22..V-24, strengthened V-21)
# ---------------------------------------------------------------------------

def test_v22_day_building_milestone_project_fails():
    """A day whose artifact sits under a milestone's project scope breaches Principle VII."""
    day = make_day(id=1, topic="t1", artifact="applied-ai/milestone1-triage-agent-scaffold/triage.py")
    r = make_roadmap([day])
    findings = v.v22_no_milestone_implementation(r)
    assert any(f.rule_id == "V-22" and f.severity == "error" for f in findings)


def test_v22_day_topic_naming_milestone_fails():
    """Naming a day's topic after a milestone is the same breach by another route."""
    r = make_roadmap([make_day(id=1, topic="t1", objective="Scaffold the m1 milestone project core")])
    r.topics["t1"].id = "milestone1-triage-agent-eval"
    r.all_days()[0].topic = "milestone1-triage-agent-eval"
    r.topics["milestone1-triage-agent-eval"] = r.topics.pop("t1")
    findings = v.v22_no_milestone_implementation(r)
    assert any(f.rule_id == "V-22" for f in findings)


def test_v22_generic_pattern_day_passes():
    r = make_roadmap([make_day(id=1, artifact="applied-ai/agent-error-handling/retry.py")])
    assert v.v22_no_milestone_implementation(r) == []


def test_v22_prose_reference_to_milestone_is_not_a_breach():
    """A review day asking 'is milestone m1 ready to start?' is legitimate, not a breach.

    Regression guard: scanning the free-text objective produced false positives on
    weekly-review days and on pattern days noting which milestone they feed.
    """
    review = make_day(id=1, topic="t1", artifact="progress/reviews/week-01.md",
                      objective="Weekly review. Milestone check: is m1 ready to start?")
    feeds = make_day(id=2, topic="t2", artifact="ml/quantization/quantize.py",
                     objective="Quantize a model — this feeds the m1 milestone directly.")
    r = make_roadmap([review, feeds])
    assert v.v22_no_milestone_implementation(r) == []


def test_v23_cloud_day_without_cost_or_teardown_fails():
    day = make_day(id=1, domain="cloud", artifact="cloud/iam-budgets/setup.md")
    r = make_roadmap([day])
    r.domains["cloud"] = r.domains["python"]
    findings = v.v23_cloud_cost_discipline(r)
    assert any(f.rule_id == "V-23" and "estimated_cost" in f.message for f in findings)
    assert any(f.rule_id == "V-23" and "teardown" in f.message for f in findings)


def test_v23_cloud_day_with_both_passes():
    """Budget-alert day first, then a costed day with teardown: compliant."""
    budget = make_day(id=1, domain="cloud", artifact="cloud/iam-budgets/setup.md",
                      estimated_cost="$0", teardown=["none required"], is_budget_setup=True)
    day = make_day(id=2, domain="cloud", artifact="cloud/s3/ingest.py",
                   estimated_cost="$0 (free tier, 5 GB)", teardown=["aws s3 rb s3://bucket --force"])
    r = make_roadmap([budget, day])
    r.domains["cloud"] = r.domains["python"]
    assert v.v23_cloud_cost_discipline(r) == []


def test_v23_cloud_day_before_budget_day_fails():
    """A cloud day sequenced before the budget-alert day breaches the cost discipline."""
    budget = make_day(id=5, domain="cloud", topic="t2", artifact="cloud/iam-budgets/setup.md",
                      estimated_cost="$0", teardown=["none"], is_budget_setup=True)
    other = make_day(id=2, domain="cloud", artifact="cloud/s3/x.py",
                     estimated_cost="$0", teardown=["rb"])
    r = make_roadmap([other, budget])
    r.domains["cloud"] = r.domains["python"]
    findings = v.v23_cloud_cost_discipline(r)
    assert any(f.rule_id == "V-23" and "budget" in f.message.lower() for f in findings)


def test_v24_blocked_dsa_days_fail():
    """DSA must be a continuous track, not consecutive DSA-only days."""
    days = [make_day(id=i, domain="dsa", topic="t1", artifact=f"dsa/p{i}/s.py") for i in range(1, 5)]
    r = make_roadmap(days)
    r.domains["dsa"] = r.domains["python"]
    findings = v.v24_dsa_continuous(r)
    assert any(f.rule_id == "V-24" for f in findings)


def test_v24_dsa_hours_pushing_day_over_budget_fails():
    day = make_day(id=1, day_type="weekday", effort_hours=6, dsa_hours=1)
    r = make_roadmap([day])
    r.weekday_hours = 6
    findings = v.v24_dsa_continuous(r)
    assert any(f.rule_id == "V-24" and "budget" in f.message.lower() for f in findings)


def test_v24_main_plus_dsa_within_budget_passes():
    day = make_day(id=1, day_type="weekday", effort_hours=5, dsa_hours=1)
    r = make_roadmap([day])
    r.weekday_hours = 6
    assert [f for f in v.v24_dsa_continuous(r) if "budget" in f.message.lower()] == []


def test_v21_thin_interview_plan_fails():
    """FR-026 strengthened: >=6 topics spanning >=3 domains per role."""
    r = make_roadmap([make_day(id=1)])
    r.interview_imminent_plan = {"agentic-ai": ["t1", "t2"]}
    findings = v.v21_interview_plan(r)
    assert any(f.rule_id == "V-21" and ">=6" in f.message for f in findings)


# ---------------------------------------------------------------------------
# NOTES.md completeness (Principle IV / FR-038)
# ---------------------------------------------------------------------------

def _notes(**bodies) -> str:
    """Build a NOTES.md with the given sections filled; others present but empty."""
    out = ["# Topic\n"]
    for section in v.REQUIRED_NOTES_SECTIONS:
        key = section.lower().replace(" ", "_").replace("-", "_")
        out.append(f"## {section}\n\n{bodies.get(key, '')}\n")
    return "\n".join(out)


def test_notes_shipped_template_is_incomplete():
    """The unfilled template must fail: all eleven sections present, none with a body."""
    template = (REPO_ROOT / "tools" / "templates" / "NOTES.template.md").read_text(
        encoding="utf-8"
    )
    missing = v.notes_missing_sections(template)
    assert len(missing) == len(v.REQUIRED_NOTES_SECTIONS)


def test_notes_guidance_comment_does_not_count_as_filled():
    text = "# T\n\n## Learning objectives\n\n<!-- what can you do now? -->\n"
    assert "Learning objectives" in v.notes_missing_sections(text)


def test_notes_bare_list_skeleton_does_not_count_as_filled():
    text = "# T\n\n## Interview questions\n\n1.\n2.\n3.\n"
    assert "Interview questions" in v.notes_missing_sections(text)


def test_notes_four_section_stub_reports_seven_missing():
    """The pre-amendment stub shape: the old four headings, none of them required names."""
    old_stub = ("# Arrays & hashing\n\n**Problem it solves**:\n\n**Mechanism**:\n\n"
                "**Failure modes**:\n\n**Trade-offs**:\n")
    assert len(v.notes_missing_sections(old_stub)) == 11


def test_notes_fully_written_passes():
    bodies = {
        section.lower().replace(" ", "_").replace("-", "_"): f"Real prose for {section}."
        for section in v.REQUIRED_NOTES_SECTIONS
    }
    assert v.notes_missing_sections(_notes(**bodies)) == []


def test_notes_one_empty_section_is_reported():
    bodies = {
        section.lower().replace(" ", "_").replace("-", "_"): f"Prose for {section}."
        for section in v.REQUIRED_NOTES_SECTIONS
    }
    del bodies["revision_notes"]
    assert v.notes_missing_sections(_notes(**bodies)) == ["Revision notes"]


# ---------------------------------------------------------------------------
# Rules de-hardcoded by the 133-day restructure (step 5)
# ---------------------------------------------------------------------------

def test_v03_week_count_is_derived_not_hardcoded():
    """V-03 asserted 10 weeks; it must derive the count from total_days."""
    # make_roadmap builds 2 weeks; declaring 21 days means 3 are expected.
    r = make_roadmap([make_day(id=i) for i in range(1, 15)])
    r.total_days = 21
    findings = [f for f in v.v03_structure(r) if "weeks" in f.message]
    assert findings and "expected 3 weeks" in findings[0].message, findings


def test_v10_requires_the_cloud_domain():
    r = make_roadmap([make_day()])
    assert any(f.rule_id == "V-10" and "cloud" in f.message
               for f in v.v10_domain_role_completeness(r))


def test_v10_rejects_embedded_ml_as_a_role():
    """FR-029 dropped Embedded ML as a target role."""
    r = make_roadmap([make_day()])
    msgs = " ".join(f.message for f in v.v10_domain_role_completeness(r))
    assert "embedded-ml" not in msgs


def test_v14_core_cap_is_derived_from_the_day_type_budgets():
    """The 272h cap was 85% of a 320h programme; it must follow the budget instead."""
    days = [make_day(id=i, day_type="weekday", effort_hours=6, dsa_hours=0)
            for i in range(1, 15)]
    r = make_roadmap(days)
    r.total_days = 14
    r.weekday_hours = 6
    findings = v.v14_core_effort_budget(r)
    # 14 weekday days x 6h = 84h budget, cap 71.4h, core 84h -> over by 12.6h
    assert findings and "71.4h cap" in findings[0].message, findings


def test_v19_and_v23_skip_review_days():
    """A weekly review naming a milestone teaches nothing and provisions nothing."""
    review = make_day(id=1, domain="cloud", artifact="progress/reviews/week-01.md",
                      objective="Weekly review. Milestone readiness: Production MCP server.")
    r = make_roadmap([review])
    r.domains["cloud"] = r.domains["python"]
    assert v.v19_generic_concept(r) == []
    assert v.v23_cloud_cost_discipline(r) == []


# ---------------------------------------------------------------------------
# D2: Principle III made verifiable across topics (V-25)
# ---------------------------------------------------------------------------

def test_v25_framework_day_before_its_scratch_topic_fails():
    scratch = make_day(id=5, topic="t2", artifact="applied-ai/scratch/loop.py")
    framework = make_day(id=2, topic="t1", artifact="applied-ai/framework/graph.py",
                         rebuilds_topic="t2")
    r = make_roadmap([framework, scratch])
    r.topics["t2"].first_day = 5
    findings = v.v25_rebuilds_after_scratch(r)
    assert any(f.rule_id == "V-25" and "not earlier" in f.message for f in findings)


def test_v25_framework_day_after_its_scratch_topic_passes():
    scratch = make_day(id=1, topic="t2", artifact="applied-ai/scratch/loop.py")
    framework = make_day(id=4, topic="t1", artifact="applied-ai/framework/graph.py",
                         rebuilds_topic="t2")
    r = make_roadmap([scratch, framework])
    r.topics["t2"].first_day = 1
    assert v.v25_rebuilds_after_scratch(r) == []


def test_v25_unknown_rebuilds_topic_fails():
    r = make_roadmap([make_day(id=1, rebuilds_topic="does-not-exist")])
    assert any(f.rule_id == "V-25" and "not a declared topic" in f.message
               for f in v.v25_rebuilds_after_scratch(r))


def test_v25_self_reference_fails():
    """Same-topic pairs belong to from_scratch_of (V-05), not rebuilds_topic."""
    r = make_roadmap([make_day(id=1, topic="t1", rebuilds_topic="t1")])
    assert any(f.rule_id == "V-25" and "its own topic" in f.message
               for f in v.v25_rebuilds_after_scratch(r))


# ---------------------------------------------------------------------------
# D1: Principle VIII, the skeleton-first half
# ---------------------------------------------------------------------------

STUB_SOURCE = """def two_sum(nums, target):
    \"\"\"O(n) time. A hash map turns the complement lookup into O(1).\"\"\"
    raise NotImplementedError
"""

DONE_SOURCE = """def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return seen[target - n], i
        seen[n] = i
    return None
"""


def test_skeleton_artifact_is_detected_as_unimplemented():
    assert v.artifact_is_unimplemented(STUB_SOURCE)


def test_implemented_artifact_passes():
    assert not v.artifact_is_unimplemented(DONE_SOURCE)


def test_stub_marker_in_a_comment_does_not_count():
    """Discussing NotImplementedError in a comment is not an unimplemented artifact."""
    text = (
        "# The skeleton raised NotImplementedError until this was written.\n"
        "def f():\n"
        "    return 1\n"
    )
    assert not v.artifact_is_unimplemented(text)
