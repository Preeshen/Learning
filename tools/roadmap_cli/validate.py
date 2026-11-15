"""Validator rules V-01..V-24 (roadmap.yaml), P-01..P-07 (progress.yaml), J-01..J-03 (journal.md).

Each rule function returns a list of Finding. See contracts/roadmap-schema.md and
contracts/progress-schema.md for the authoritative rule definitions this mirrors.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path

from tools.roadmap_cli.models import DayProgress, ProgressRecord, ProgressStatus, Roadmap

REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Finding:
    rule_id: str
    severity: str  # "error" | "warn"
    message: str


# ---------------------------------------------------------------------------
# roadmap.yaml rules
# ---------------------------------------------------------------------------

def v01_dates(r: Roadmap) -> list[Finding]:
    findings = []
    expected_end = r.start_date + timedelta(days=r.total_days - 1)
    if expected_end != r.end_date:
        findings.append(Finding("V-01", "error",
            f"end_date {r.end_date} does not equal start_date + total_days - 1 ({expected_end})"))
    for day in r.all_days():
        expected_date = r.start_date + timedelta(days=day.id - 1)
        if day.date != expected_date:
            findings.append(Finding("V-01", "error",
                f"day {day.id}: date {day.date} != derived {expected_date}"))
        is_weekend = expected_date.weekday() >= 5
        expected_type = "weekend" if is_weekend else "weekday"
        if day.day_type != expected_type:
            findings.append(Finding("V-01", "error",
                f"day {day.id}: day_type {day.day_type} != derived {expected_type}"))
    return findings


def v02_required_fields(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        for field_name in ("artifact", "verification", "notes_topic", "minimum_viable"):
            if not getattr(day, field_name):
                findings.append(Finding("V-02", "error",
                    f"day {day.id}: `{field_name}` is empty"))
        if not day.gate:
            findings.append(Finding("V-02", "error", f"day {day.id}: `gate` has no entries"))
    return findings


def v03_structure(r: Roadmap) -> list[Finding]:
    findings = []
    if len(r.weeks) != 10:
        findings.append(Finding("V-03", "error", f"expected 10 weeks, found {len(r.weeks)}"))
    seen_days: set[int] = set()
    for week in r.weeks:
        if len(week.days) != 7:
            findings.append(Finding("V-03", "error",
                f"week {week.number}: expected 7 days, found {len(week.days)}"))
        for day in week.days:
            if day.id in seen_days:
                findings.append(Finding("V-03", "error", f"day id {day.id} duplicated"))
            seen_days.add(day.id)
    if seen_days and (min(seen_days) != 1 or max(seen_days) != len(seen_days)):
        findings.append(Finding("V-03", "error",
            "day ids are not contiguous 1..N with no gaps"))
    return findings


def v04_effort_budget(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        budget = r.weekday_hours if day.day_type == "weekday" else r.weekend_hours
        if day.effort_hours > budget:
            findings.append(Finding("V-04", "error",
                f"day {day.id}: effort_hours {day.effort_hours} exceeds {day.day_type} "
                f"budget {budget}"))
    return findings


def v05_scratch_before_library(r: Roadmap) -> list[Finding]:
    findings = []
    by_id = {d.id: d for d in r.all_days()}
    for day in r.all_days():
        if day.from_scratch_of is not None:
            scratch = by_id.get(day.from_scratch_of)
            if scratch is None:
                findings.append(Finding("V-05", "error",
                    f"day {day.id}: from_scratch_of {day.from_scratch_of} does not exist"))
            elif scratch.id >= day.id:
                findings.append(Finding("V-05", "error",
                    f"day {day.id}: from_scratch_of {day.from_scratch_of} is not earlier"))
            elif scratch.topic != day.topic:
                findings.append(Finding("V-05", "error",
                    f"day {day.id}: from_scratch_of {day.from_scratch_of} has a different topic"))
    return findings


def v06_measurement(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        if day.measurement is not None:
            m = day.measurement
            for field_name in ("metric", "baseline", "results_path", "method"):
                if not getattr(m, field_name):
                    findings.append(Finding("V-06", "error",
                        f"day {day.id}: measurement.{field_name} is empty"))
    return findings


def v07_resurfacing(r: Roadmap) -> list[Finding]:
    findings = []
    for tid, topic in r.topics.items():
        intervals = topic.resurface_after
        if len(intervals) < 2:
            findings.append(Finding("V-07", "error",
                f"topic {tid}: fewer than 2 resurface_after intervals"))
        elif list(intervals) != sorted(set(intervals)) or len(set(intervals)) != len(intervals):
            findings.append(Finding("V-07", "error",
                f"topic {tid}: resurface_after intervals not strictly increasing"))

    resolve_counts: dict[str, int] = {}
    for week in r.weeks:
        for tid in week.review.resolves:
            resolve_counts[tid] = resolve_counts.get(tid, 0) + 1

    # FR-015 scopes the "resurface twice" requirement to DSA problem sets and core ML concepts,
    # not every topic in every domain.
    review_days = sorted(w.review.day for w in r.weeks)
    for tid, topic in r.topics.items():
        if topic.domain not in ("dsa", "ml"):
            continue
        reviews_after = [d for d in review_days if d > topic.first_day]
        required = min(2, len(reviews_after))
        count = resolve_counts.get(tid, 0)
        if count < required:
            if required < 2:
                findings.append(Finding("V-07", "error",
                    f"topic {tid}: introduced on day {topic.first_day} with only "
                    f"{len(reviews_after)} review checkpoint(s) remaining — appears in "
                    f"{count} of the {required} slot(s) actually available"))
            else:
                findings.append(Finding("V-07", "error",
                    f"topic {tid}: appears in fewer than 2 checkpoints' resolves"))
    return findings


def v08_milestone_external(r: Roadmap) -> list[Finding]:
    findings = []
    for m in r.milestones:
        if not m.external:
            findings.append(Finding("V-08", "error", f"milestone {m.id}: external is not true"))
        if m.record_path.startswith("/") or ".." in m.record_path:
            findings.append(Finding("V-08", "error",
                f"milestone {m.id}: record_path looks unsafe: {m.record_path}"))
    return findings


def v09_referential_integrity(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        if day.domain not in r.domains:
            findings.append(Finding("V-09", "error", f"day {day.id}: unknown domain {day.domain}"))
        if day.topic not in r.topics:
            findings.append(Finding("V-09", "error", f"day {day.id}: unknown topic {day.topic}"))
    return findings


def v10_domain_role_completeness(r: Roadmap) -> list[Finding]:
    findings = []
    expected_domains = {"python", "dsa", "git", "systems", "ml", "applied-ai"}
    if set(r.domains) != expected_domains:
        findings.append(Finding("V-10", "error",
            f"domains must be exactly {expected_domains}, found {set(r.domains)}"))
    expected_roles = {"agentic-ai", "fde", "ml-engineer", "inference", "embedded-ml",
                      "test-validation"}
    if set(r.roles) != expected_roles:
        findings.append(Finding("V-10", "error",
            f"roles must be exactly {expected_roles}, found {set(r.roles)}"))
    primary = [rid for rid, role in r.roles.items() if role.tier == "primary"]
    secondary = [rid for rid, role in r.roles.items() if role.tier == "secondary"]
    if len(primary) != 1:
        findings.append(Finding("V-10", "error", f"expected exactly 1 primary role, found {primary}"))
    if len(secondary) != 1:
        findings.append(Finding("V-10", "error", f"expected exactly 1 secondary role, found {secondary}"))
    return findings


def v11_prerequisites(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        for p in day.prerequisites:
            if p >= day.id:
                findings.append(Finding("V-11", "error",
                    f"day {day.id}: prerequisite {p} is not earlier"))
    return findings


def v12_exceptions(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        if day.language != "python" and not day.language_exception:
            findings.append(Finding("V-12", "error",
                f"day {day.id}: language {day.language} requires language_exception"))
        if not day.offline and not day.offline_fallback:
            findings.append(Finding("V-12", "error",
                f"day {day.id}: offline is false and requires offline_fallback"))
    return findings


def v13_domain_share(r: Roadmap) -> list[Finding]:
    findings = []
    total = r.total_days
    counts: dict[str, int] = {}
    for day in r.all_days():
        counts[day.domain] = counts.get(day.domain, 0) + 1
    for domain_id, count in counts.items():
        share = count / total
        if share > 0.40:
            findings.append(Finding("V-13", "warn",
                f"domain {domain_id}: {share:.0%} of days exceeds the 40% cap"))
    return findings


def v14_core_effort_budget(r: Roadmap) -> list[Finding]:
    findings = []
    core_total = sum(d.effort_hours for d in r.all_days() if d.priority == "core")
    if core_total > 272:
        findings.append(Finding("V-14", "warn",
            f"core effort {core_total}h exceeds the 272h budget by {core_total - 272}h"))
    return findings


def v15_tier_split(r: Roadmap) -> list[Finding]:
    findings = []
    total = r.total_days
    counts: dict[str, int] = {}
    for day in r.all_days():
        counts[day.tier] = counts.get(day.tier, 0) + 1
    targets = {"primary": 0.60, "secondary": 0.25, "remaining": 0.15}
    for tier, target in targets.items():
        share = counts.get(tier, 0) / total
        if abs(share - target) > 0.05:
            findings.append(Finding("V-15", "warn",
                f"tier {tier}: {share:.0%} is more than 5 points from target {target:.0%}"))
    return findings


def v16_remaining_evidence(r: Roadmap) -> list[Finding]:
    findings = []
    for rid, role in r.roles.items():
        if role.tier != "remaining":
            continue
        for requirement in role.evidence_required:
            # A day "satisfies" evidence if it supports this role and has a measurement
            # or is explicitly tagged — here we check at least one supporting day exists.
            supporting = [d for d in r.all_days()
                          if rid in r.domains.get(d.domain, type("x", (), {"supports_roles": []})()).supports_roles]
            if not supporting:
                findings.append(Finding("V-16", "warn",
                    f"role {rid}: evidence requirement '{requirement}' has no supporting day"))
    return findings


def v17_milestone_count(r: Roadmap) -> list[Finding]:
    findings = []
    if len(r.milestones) < 3:
        findings.append(Finding("V-17", "warn", f"expected >=3 milestones, found {len(r.milestones)}"))
    return findings


def v18_serving_fastapi(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        if day.serving is not None and day.serving != "fastapi":
            findings.append(Finding("V-18", "error",
                f"day {day.id}: serving {day.serving!r} must be 'fastapi'"))
    return findings


CLAUDE_TOOLING_MARKERS = ("claude code skill", "claude agent sdk", "mcp", "model context protocol")


def v19_generic_concept(r: Roadmap) -> list[Finding]:
    findings = []
    for day in r.all_days():
        haystack = f"{day.objective} {day.notes_topic} {day.artifact}".lower()
        if any(marker in haystack for marker in CLAUDE_TOOLING_MARKERS):
            if not day.generic_concept:
                findings.append(Finding("V-19", "error",
                    f"day {day.id}: references Claude-specific tooling but generic_concept is empty"))
    return findings


def v20_milestone_fields(r: Roadmap) -> list[Finding]:
    findings = []
    for m in r.milestones:
        if not m.purpose:
            findings.append(Finding("V-20", "error", f"milestone {m.id}: purpose is empty"))
        if not m.demonstrates:
            findings.append(Finding("V-20", "error", f"milestone {m.id}: demonstrates is empty"))
        if not m.supports_roles:
            findings.append(Finding("V-20", "error", f"milestone {m.id}: supports_roles is empty"))
    return findings


MIN_INTERVIEW_PLAN_TOPICS = 6
MIN_INTERVIEW_PLAN_DOMAINS = 3


def v21_interview_plan(r: Roadmap) -> list[Finding]:
    findings = []
    if not r.interview_imminent_plan:
        findings.append(Finding("V-21", "error", "interview_imminent_plan is missing or empty"))
        return findings
    all_topic_ids = set(r.topics)
    for role_id, topic_ids in r.interview_imminent_plan.items():
        if not topic_ids:
            findings.append(Finding("V-21", "error",
                f"interview_imminent_plan[{role_id}] is empty"))
        for tid in topic_ids:
            if tid not in all_topic_ids:
                findings.append(Finding("V-21", "error",
                    f"interview_imminent_plan[{role_id}] references unknown topic {tid}"))
        # FR-026 as strengthened by the v1.1.0 amendment: a drill path of two early
        # topics is a placeholder, not a plan.
        if len(topic_ids) < MIN_INTERVIEW_PLAN_TOPICS:
            findings.append(Finding("V-21", "error",
                f"interview_imminent_plan[{role_id}] has {len(topic_ids)} topics, "
                f">={MIN_INTERVIEW_PLAN_TOPICS} required"))
        plan_domains = {r.topics[t].domain for t in topic_ids if t in r.topics}
        if len(plan_domains) < MIN_INTERVIEW_PLAN_DOMAINS:
            findings.append(Finding("V-21", "error",
                f"interview_imminent_plan[{role_id}] spans {len(plan_domains)} domain(s), "
                f">={MIN_INTERVIEW_PLAN_DOMAINS} required"))
    return findings


def v22_no_milestone_implementation(r: Roadmap) -> list[Finding]:
    """Principle VII / FR-039: no day entry may implement a milestone's project.

    V-08 checks milestone definitions. This checks day entries, which is where the
    breach actually occurred: days named after milestones were building the projects
    while every other rule passed.
    """
    findings = []
    handles = {m.id for m in r.milestones}
    for i, _ in enumerate(r.milestones, start=1):
        handles.add(f"milestone{i}")
    # Only the topic id and artifact path are evidence of implementation. A day's prose
    # may legitimately reference a milestone — a weekly review asking "is milestone X
    # ready to start?", or a pattern day noting what it feeds — so the objective is
    # deliberately not scanned.
    for day in r.all_days():
        haystack = f"{day.topic} {day.artifact}".lower()
        for handle in sorted(h for h in handles if h):
            if handle.lower() in haystack:
                findings.append(Finding("V-22", "error",
                    f"day {day.id}: topic/artifact names milestone {handle!r} "
                    f"({day.artifact}) — day entries must not implement a portfolio "
                    f"project (constitution Principle VII); re-scope to the generic pattern"))
                break
    return findings


def v23_cloud_cost_discipline(r: Roadmap) -> list[Finding]:
    """FR-040: every cloud day needs a cost estimate, teardown, and budget-day ordering."""
    findings = []
    cloud_days = [d for d in r.all_days() if d.domain == "cloud"]
    if not cloud_days:
        return findings
    budget_days = [d for d in cloud_days if d.is_budget_setup]
    first_budget_id = min((d.id for d in budget_days), default=None)
    for day in cloud_days:
        if not day.estimated_cost:
            findings.append(Finding("V-23", "error",
                f"day {day.id}: cloud day has no estimated_cost"))
        if not day.teardown:
            findings.append(Finding("V-23", "error",
                f"day {day.id}: cloud day has no teardown steps"))
        if first_budget_id is None:
            findings.append(Finding("V-23", "error",
                f"day {day.id}: cloud days exist but no day is marked is_budget_setup — "
                f"budget alerts must be the first cloud exercise"))
        elif day.id < first_budget_id and not day.is_budget_setup:
            findings.append(Finding("V-23", "error",
                f"day {day.id}: sequenced before the budget-alert day "
                f"({first_budget_id}); no cloud resource may be provisioned first"))
    return findings


MAX_CONSECUTIVE_DSA_DAYS = 2


def v24_dsa_continuous(r: Roadmap) -> list[Finding]:
    """FR-037: DSA is a continuous daily track, not a block of DSA-only days.

    Also enforces that the day's main artifact effort plus its DSA hour fit the
    day-type budget (SC-016), which FR-027's per-day check alone does not cover.
    """
    findings = []
    run = 0
    for day in r.all_days():
        run = run + 1 if day.domain == "dsa" else 0
        if run > MAX_CONSECUTIVE_DSA_DAYS:
            findings.append(Finding("V-24", "error",
                f"day {day.id}: {run} consecutive DSA-only days — DSA must run as a "
                f"continuous daily track, not blocked days (max "
                f"{MAX_CONSECUTIVE_DSA_DAYS} consecutive)"))
            break
    for day in r.all_days():
        cap = r.weekday_hours if day.day_type == "weekday" else r.weekend_hours
        total = day.effort_hours + day.dsa_hours
        if total > cap:
            findings.append(Finding("V-24", "error",
                f"day {day.id}: main effort {day.effort_hours} h + DSA {day.dsa_hours} h "
                f"= {total} h exceeds the {day.day_type} budget of {cap} h"))
    return findings


ROADMAP_RULES = [
    v01_dates, v02_required_fields, v03_structure, v04_effort_budget, v05_scratch_before_library,
    v06_measurement, v07_resurfacing, v08_milestone_external, v09_referential_integrity,
    v10_domain_role_completeness, v11_prerequisites, v12_exceptions, v13_domain_share,
    v14_core_effort_budget, v15_tier_split, v16_remaining_evidence, v17_milestone_count,
    v18_serving_fastapi, v19_generic_concept, v20_milestone_fields, v21_interview_plan,
    v22_no_milestone_implementation, v23_cloud_cost_discipline, v24_dsa_continuous,
]


def validate_roadmap(r: Roadmap) -> list[Finding]:
    findings: list[Finding] = []
    for rule in ROADMAP_RULES:
        findings.extend(rule(r))
    return findings


# ---------------------------------------------------------------------------
# progress.yaml rules (P-01..P-07)
# ---------------------------------------------------------------------------

def p01_no_gaps(progress: ProgressRecord) -> list[Finding]:
    findings = []
    days = sorted(e.day for e in progress.entries)
    if len(days) != len(set(days)):
        findings.append(Finding("P-01", "error", "duplicate day values in progress entries"))
    if days and days != list(range(1, max(days) + 1)):
        findings.append(Finding("P-01", "error", "gap in progress entries' day sequence"))
    return findings


def p02_complete_requires_commit(progress: ProgressRecord) -> list[Finding]:
    findings = []
    for e in progress.entries:
        if e.status == ProgressStatus.COMPLETE:
            if not e.commit:
                findings.append(Finding("P-02", "error", f"day {e.day}: complete without commit"))
            if not e.gate_passed:
                findings.append(Finding("P-02", "error",
                    f"day {e.day}: complete without gate_passed: true"))
    return findings


def p03_commit_resolves(progress: ProgressRecord) -> list[Finding]:
    findings = []
    for e in progress.entries:
        if e.commit:
            result = subprocess.run(
                ["git", "cat-file", "-e", e.commit], cwd=REPO_ROOT, capture_output=True
            )
            if result.returncode != 0:
                findings.append(Finding("P-03", "error",
                    f"day {e.day}: commit {e.commit} does not resolve in this repository"))
    return findings


def p04_journal_ref(progress: ProgressRecord, journal_text: str) -> list[Finding]:
    findings = []
    anchors = set(re.findall(r"\{#([\w-]+)\}", journal_text))
    for e in progress.entries:
        if not e.journal_ref:
            findings.append(Finding("P-04", "error", f"day {e.day}: missing journal_ref"))
        elif e.journal_ref not in anchors:
            findings.append(Finding("P-04", "error",
                f"day {e.day}: journal_ref {e.journal_ref} has no matching anchor"))
    return findings


def p05_day_exists(progress: ProgressRecord, r: Roadmap) -> list[Finding]:
    findings = []
    valid_ids = {d.id for d in r.all_days()}
    for e in progress.entries:
        if e.day not in valid_ids:
            findings.append(Finding("P-05", "error", f"day {e.day}: no such DayEntry in roadmap"))
    return findings


def p06_stale_carried(progress: ProgressRecord) -> list[Finding]:
    findings = []
    current = progress.current_day()
    for e in progress.entries:
        if e.status == ProgressStatus.CARRIED and e.day < current:
            findings.append(Finding("P-06", "warn",
                f"day {e.day}: carried but older than current day {current} — should be resumed"))
    return findings


def p07_double_fail_escalation(progress: ProgressRecord) -> list[Finding]:
    findings = []
    fail_counts: dict[str, int] = {}
    for e in progress.entries:
        for rr in e.resolve_results:
            if not rr.passed:
                fail_counts[rr.topic] = fail_counts.get(rr.topic, 0) + 1
    for topic, count in fail_counts.items():
        if count >= 2:
            findings.append(Finding("P-07", "warn",
                f"topic {topic}: failed resolve {count} times — FR-016 escalation triggered"))
    return findings


PROGRESS_RULES = [p01_no_gaps, p02_complete_requires_commit, p03_commit_resolves]


def validate_progress(progress: ProgressRecord, r: Roadmap, journal_text: str) -> list[Finding]:
    findings: list[Finding] = []
    for rule in PROGRESS_RULES:
        findings.extend(rule(progress))
    findings.extend(p04_journal_ref(progress, journal_text))
    findings.extend(p05_day_exists(progress, r))
    findings.extend(p06_stale_carried(progress))
    findings.extend(p07_double_fail_escalation(progress))
    return findings


# ---------------------------------------------------------------------------
# journal.md rules (J-01..J-03)
# ---------------------------------------------------------------------------

def j01_refs_resolve(progress: ProgressRecord, journal_text: str) -> list[Finding]:
    findings = []
    anchors = re.findall(r"\{#([\w-]+)\}", journal_text)
    anchor_counts: dict[str, int] = {}
    for a in anchors:
        anchor_counts[a] = anchor_counts.get(a, 0) + 1
    for e in progress.entries:
        if e.journal_ref and anchor_counts.get(e.journal_ref, 0) != 1:
            findings.append(Finding("J-01", "error",
                f"journal_ref {e.journal_ref} resolves to "
                f"{anchor_counts.get(e.journal_ref, 0)} anchors, expected exactly 1"))
    return findings


def j02_ascending_order(journal_text: str) -> list[Finding]:
    findings = []
    day_numbers = [int(n) for n in re.findall(r"^## Day (\d+)", journal_text, re.MULTILINE)]
    if day_numbers != sorted(day_numbers):
        findings.append(Finding("J-02", "error", "journal entries are not in ascending day order"))
    return findings


def j03_prose_fields(journal_text: str) -> list[Finding]:
    findings = []
    sections = re.split(r"^## Day \d+.*$", journal_text, flags=re.MULTILINE)[1:]
    day_numbers = [int(n) for n in re.findall(r"^## Day (\d+)", journal_text, re.MULTILINE)]
    for day_number, section in zip(day_numbers, sections):
        if "**Status**: complete" in section:
            for label in ("**Built**", "**Broke**", "**Non-obvious**"):
                if label not in section:
                    findings.append(Finding("J-03", "warn",
                        f"day {day_number}: complete entry missing {label}"))
    return findings


def validate_journal(progress: ProgressRecord, journal_text: str) -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(j01_refs_resolve(progress, journal_text))
    findings.extend(j02_ascending_order(journal_text))
    findings.extend(j03_prose_fields(journal_text))
    return findings


# ---------------------------------------------------------------------------
# NOTES.md completeness (constitution v1.1.0 Principle IV / FR-038)
# ---------------------------------------------------------------------------

REQUIRED_NOTES_SECTIONS = (
    "Learning objectives",
    "Prerequisites",
    "Conceptual explanation",
    "Why it matters",
    "Internal mechanisms",
    "Real-world applications",
    "Alternatives and trade-offs",
    "Failure modes and common mistakes",
    "Interview questions",
    "Assessment criteria",
    "Revision notes",
)

_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_SECTION_HEADING = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def notes_missing_sections(notes_text: str) -> list[str]:
    """Return the required sections that are absent or have no body.

    Guidance comments are stripped first, so a template left unfilled counts as empty.
    A bare ordered-list skeleton ("1.\n2.\n3.") also counts as empty, since the template
    ships one under Interview questions.
    """
    text = _HTML_COMMENT.sub("", notes_text)
    bodies: dict[str, str] = {}
    matches = list(_SECTION_HEADING.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        bodies[m.group(1).strip().lower()] = text[m.end():end]

    missing = []
    for section in REQUIRED_NOTES_SECTIONS:
        body = bodies.get(section.lower())
        if body is None:
            missing.append(section)
            continue
        stripped = "\n".join(
            line for line in body.splitlines()
            if line.strip() and line.strip() not in {"1.", "2.", "3.", "-", "*"}
        ).strip()
        if not stripped:
            missing.append(section)
    return missing
