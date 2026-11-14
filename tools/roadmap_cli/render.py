"""Generate roadmap/ROADMAP.md and roadmap/milestones.md from roadmap.yaml.

The only module that writes these two files — roadmap.yaml is the sole source of truth and
must never be hand-edited to match them.
"""

from __future__ import annotations

from pathlib import Path

from tools.roadmap_cli.models import Roadmap

REPO_ROOT = Path(__file__).resolve().parents[2]
ROADMAP_MD = REPO_ROOT / "roadmap" / "ROADMAP.md"
MILESTONES_MD = REPO_ROOT / "roadmap" / "milestones.md"


def render_roadmap_md(r: Roadmap) -> str:
    lines = [
        "# Roadmap (generated — do not hand-edit; see roadmap.yaml)",
        "",
        f"{r.total_days} days · {len(r.weeks)} weeks · {r.start_date} to {r.end_date}",
        "",
    ]
    for week in r.weeks:
        lines.append(f"## Week {week.number} — {week.theme}")
        lines.append("")
        lines.append(f"Domains: {', '.join(week.domains)} · Outcome: {week.outcome}")
        lines.append("")
        for day in week.days:
            lines.append(
                f"### Day {day.id} — {day.date} ({day.day_type}, {day.effort_hours}h, "
                f"{day.priority})"
            )
            lines.append("")
            lines.append(f"- **Domain/Topic**: {day.domain} / {day.topic}")
            lines.append(f"- **Objective**: {day.objective}")
            lines.append(f"- **Artifact**: `{day.artifact}`")
            lines.append(f"- **Verification**: {day.verification}")
            lines.append(f"- **Notes topic**: {day.notes_topic}")
            lines.append(f"- **Minimum viable**: {day.minimum_viable}")
            if day.prerequisites:
                lines.append(f"- **Prerequisites**: {', '.join(str(p) for p in day.prerequisites)}")
            lines.append("")
        lines.append(f"**Review** (day {week.review.day}): resolves {', '.join(week.review.resolves)}")
        lines.append("")
    return "\n".join(lines) + "\n"


def render_milestones_md(r: Roadmap) -> str:
    lines = ["# Promotion Milestones (generated — do not hand-edit; see roadmap.yaml)", ""]
    for m in r.milestones:
        lines.append(f"## {m.name} (`{m.id}`)")
        lines.append("")
        lines.append(f"- **Opens after day**: {m.after_day}")
        lines.append(f"- **Prerequisite days**: {', '.join(str(d) for d in m.prerequisite_days)}")
        lines.append(f"- **Purpose**: {m.purpose.strip()}")
        lines.append("- **Demonstrates**:")
        for d in m.demonstrates:
            lines.append(f"  - {d}")
        lines.append(f"- **Supports roles**: {', '.join(m.supports_roles)}")
        lines.append(f"- **Record**: this project is built in a separate repository; "
                      f"record its pointer in `{m.record_path}`")
        lines.append("")
    return "\n".join(lines) + "\n"


def render(r: Roadmap) -> None:
    ROADMAP_MD.parent.mkdir(parents=True, exist_ok=True)
    ROADMAP_MD.write_text(render_roadmap_md(r), encoding="utf-8")
    MILESTONES_MD.write_text(render_milestones_md(r), encoding="utf-8")


def is_stale(r: Roadmap) -> bool:
    if not ROADMAP_MD.exists() or not MILESTONES_MD.exists():
        return True
    return (
        ROADMAP_MD.read_text(encoding="utf-8") != render_roadmap_md(r)
        or MILESTONES_MD.read_text(encoding="utf-8") != render_milestones_md(r)
    )
