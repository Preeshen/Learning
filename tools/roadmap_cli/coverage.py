"""FR-024/SC-008 role-coverage reporting."""

from __future__ import annotations

from tools.roadmap_cli.models import ProgressRecord, ProgressStatus, Roadmap


def domain_share(r: Roadmap) -> dict[str, float]:
    total = r.total_days
    counts: dict[str, int] = {}
    for day in r.all_days():
        counts[day.domain] = counts.get(day.domain, 0) + 1
    return {domain_id: count / total for domain_id, count in counts.items()}


def role_coverage(r: Roadmap, progress: ProgressRecord) -> list[dict]:
    completed_days = {
        e.day for e in progress.entries if e.status == ProgressStatus.COMPLETE
    }
    rows = []
    for role_id, role in r.roles.items():
        supporting_days = [
            d for d in r.all_days() if role_id in r.domains.get(d.domain).supports_roles
        ]
        done = [d for d in supporting_days if d.id in completed_days]
        readiness = (len(done) / len(supporting_days)) if supporting_days else 0.0
        row = {
            "role_id": role_id,
            "name": role.name,
            "tier": role.tier,
            "days": len(supporting_days),
            "done": len(done),
            "readiness": readiness,
            "supporting_day_ids": [d.id for d in supporting_days],
        }
        if role.evidence_required:
            # Evidence is satisfied when at least one completed supporting day carries a
            # measurement — a crude but mechanical proxy for "demonstrable artifact".
            satisfied = sum(
                1 for d in done if d.measurement is not None
            )
            row["evidence_total"] = len(role.evidence_required)
            row["evidence_satisfied"] = min(satisfied, len(role.evidence_required))
        rows.append(row)
    return rows


def milestone_status(r: Roadmap, progress: ProgressRecord) -> list[dict]:
    """FR-020/US4: for each milestone, whether its prerequisite days are all complete, and if
    not, which specific days are still unmet (spec.md US4 Acceptance Scenario 3)."""
    completed_days = {
        e.day for e in progress.entries if e.status == ProgressStatus.COMPLETE
    }
    rows = []
    for m in r.milestones:
        unmet = [d for d in m.prerequisite_days if d not in completed_days]
        rows.append({
            "id": m.id,
            "name": m.name,
            "ready": len(unmet) == 0,
            "unmet_prerequisite_days": unmet,
            "purpose": m.purpose,
            "demonstrates": m.demonstrates,
            "supports_roles": m.supports_roles,
            "record_path": m.record_path,
        })
    return rows


def role_detail(r: Roadmap, progress: ProgressRecord, role_id: str) -> dict:
    completed_days = {
        e.day for e in progress.entries if e.status == ProgressStatus.COMPLETE
    }
    supporting_days = [
        d for d in r.all_days() if role_id in r.domains.get(d.domain).supports_roles
    ]
    return {
        "role_id": role_id,
        "days": [
            {"id": d.id, "domain": d.domain, "topic": d.topic,
             "done": d.id in completed_days}
            for d in supporting_days
        ],
    }
