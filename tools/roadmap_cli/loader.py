"""Load and validate roadmap.yaml and progress.yaml, constructing the dataclass tree."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import jsonschema
import yaml

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
    RoleTarget,
    Roadmap,
    Tier,
    Topic,
    Week,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
ROADMAP_PATH = REPO_ROOT / "roadmap" / "roadmap.yaml"
PROGRESS_PATH = REPO_ROOT / "progress" / "progress.yaml"
SCHEMA_DIR = Path(__file__).resolve().parent / "schema"
SUPPORTED_ROADMAP_VERSION = 1


class LoadError(Exception):
    """Raised for usage/load errors — callers should exit 2."""


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _load_schema(name: str) -> dict:
    with (SCHEMA_DIR / name).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _to_date(value) -> date:
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value))


def _stringify_dates(obj):
    """PyYAML parses unquoted YYYY-MM-DD as date objects; jsonschema's "date" format check
    expects strings. Recursively stringify dates for schema validation only."""
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _stringify_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_stringify_dates(v) for v in obj]
    return obj


def _build_day(raw: dict) -> DayEntry:
    measurement = None
    if raw.get("measurement"):
        measurement = Measurement(**raw["measurement"])
    return DayEntry(
        id=raw["id"],
        date=_to_date(raw["date"]),
        day_type=raw["day_type"],
        objective=raw["objective"],
        domain=raw["domain"],
        topic=raw["topic"],
        artifact=raw["artifact"],
        verification=raw["verification"],
        notes_topic=raw["notes_topic"],
        effort_hours=raw["effort_hours"],
        tier=raw["tier"],
        priority=raw["priority"],
        gate=list(raw["gate"]),
        minimum_viable=raw["minimum_viable"],
        prerequisites=list(raw.get("prerequisites", [])),
        from_scratch_of=raw.get("from_scratch_of"),
        measurement=measurement,
        language=raw.get("language", "python"),
        language_exception=raw.get("language_exception"),
        offline=raw.get("offline", True),
        offline_fallback=raw.get("offline_fallback"),
        serving=raw.get("serving"),
        generic_concept=raw.get("generic_concept"),
    )


def load_roadmap(path: Path = ROADMAP_PATH) -> Roadmap:
    if not path.exists():
        raise LoadError(
            f"roadmap.yaml not found at {path}. Expected path: {ROADMAP_PATH}. "
            "Run `roadmap init` or create it per contracts/roadmap-schema.md."
        )
    raw = _load_yaml(path)
    version = raw.get("version")
    if version != SUPPORTED_ROADMAP_VERSION:
        raise LoadError(
            f"Unsupported roadmap.yaml schema version {version!r}; "
            f"this build supports version {SUPPORTED_ROADMAP_VERSION}."
        )
    schema = _load_schema("roadmap.schema.json")
    jsonschema.validate(instance=_stringify_dates(raw), schema=schema)

    domains = {
        did: Domain(id=did, **d) for did, d in raw["domains"].items()
    }
    roles = {
        rid: RoleTarget(id=rid, **r) for rid, r in raw["roles"].items()
    }
    topics = {
        tid: Topic(id=tid, **t) for tid, t in raw["topics"].items()
    }
    weeks = []
    for w in raw["weeks"]:
        days = [_build_day(d) for d in w["days"]]
        review = ReviewCheckpoint(**w["review"])
        weeks.append(
            Week(
                number=w["number"],
                theme=w["theme"],
                domains=list(w["domains"]),
                outcome=w["outcome"],
                days=days,
                review=review,
            )
        )
    milestones = [PromotionMilestone(**m) for m in raw["milestones"]]

    return Roadmap(
        version=version,
        start_date=_to_date(raw["start_date"]),
        end_date=_to_date(raw["end_date"]),
        total_days=raw["total_days"],
        weekday_hours=raw["weekday_hours"],
        weekend_hours=raw["weekend_hours"],
        primary_role=raw["primary_role"],
        secondary_role=raw["secondary_role"],
        domains=domains,
        roles=roles,
        topics=topics,
        weeks=weeks,
        milestones=milestones,
        interview_imminent_plan=dict(raw["interview_imminent_plan"]),
    )


def load_progress(path: Path = PROGRESS_PATH) -> ProgressRecord:
    if not path.exists():
        # Fresh start — cli-contract.md's Error handling table: exit 0, `today` returns day 1.
        return ProgressRecord(version=1, roadmap_version=SUPPORTED_ROADMAP_VERSION,
                               started=date.today(), entries=[])
    raw = _load_yaml(path) or {}
    schema = _load_schema("progress.schema.json")
    jsonschema.validate(instance=_stringify_dates(raw), schema=schema)

    entries = []
    for e in raw.get("entries", []):
        resolve_results = [ResolveResult(**r) for r in e.get("resolve_results", [])]
        entries.append(
            DayProgress(
                day=e["day"],
                status=ProgressStatus(e["status"]),
                date=_to_date(e["date"]),
                commit=e.get("commit"),
                gate_passed=e.get("gate_passed"),
                journal_ref=e.get("journal_ref"),
                resolve_results=resolve_results,
            )
        )
    return ProgressRecord(
        version=raw.get("version", 1),
        roadmap_version=raw.get("roadmap_version", SUPPORTED_ROADMAP_VERSION),
        started=_to_date(raw["started"]) if raw.get("started") else date.today(),
        entries=entries,
    )
