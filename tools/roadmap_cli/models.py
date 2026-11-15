"""Dataclasses mirroring data-model.md's entities.

Field names and required/optional status match data-model.md exactly, so the loader can
construct these directly from parsed YAML without renaming.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class DayType(str, Enum):
    WEEKDAY = "weekday"
    WEEKEND = "weekend"


class Tier(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    REMAINING = "remaining"


class Priority(str, Enum):
    CORE = "core"
    OPTIONAL = "optional"


class ProgressStatus(str, Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    SKIPPED = "skipped"
    CARRIED = "carried"


@dataclass
class Measurement:
    metric: str
    baseline: str
    results_path: str
    method: str


@dataclass
class DayEntry:
    id: int
    date: date
    day_type: DayType
    objective: str
    domain: str
    topic: str
    artifact: str
    verification: str
    notes_topic: str
    effort_hours: float
    tier: Tier
    priority: Priority
    gate: list[str]
    minimum_viable: str
    prerequisites: list[int] = field(default_factory=list)
    from_scratch_of: int | None = None
    measurement: Measurement | None = None
    language: str = "python"
    language_exception: str | None = None
    offline: bool = True
    offline_fallback: str | None = None
    serving: str | None = None
    generic_concept: str | None = None
    # Constitution v1.1.0: DSA runs as a continuous daily track (FR-037), accounted
    # separately from the day's main artifact effort.
    dsa_hours: float = 0.0
    # Constitution v1.1.0 cloud cost discipline (FR-040).
    estimated_cost: str | None = None
    teardown: list[str] = field(default_factory=list)
    is_budget_setup: bool = False


@dataclass
class ReviewCheckpoint:
    week: int
    day: int
    resolves: list[str]
    procedure: list[str]
    output_path: str


@dataclass
class Week:
    number: int
    theme: str
    domains: list[str]
    outcome: str
    days: list[DayEntry]
    review: ReviewCheckpoint


@dataclass
class Domain:
    id: str
    name: str
    directory: str
    target_days: int
    min_depth: str
    supports_roles: list[str]


@dataclass
class Topic:
    id: str
    name: str
    domain: str
    first_day: int
    resurface_after: list[int]
    references: list[dict] = field(default_factory=list)


@dataclass
class PromotionMilestone:
    id: str
    name: str
    after_day: int
    prerequisite_days: list[int]
    purpose: str
    demonstrates: list[str]
    supports_roles: list[str]
    external: bool
    record_path: str


@dataclass
class RoleTarget:
    id: str
    name: str
    tier: Tier
    supporting_domains: list[str]
    evidence_required: list[str] = field(default_factory=list)


@dataclass
class Roadmap:
    version: int
    start_date: date
    end_date: date
    total_days: int
    weekday_hours: float
    weekend_hours: float
    primary_role: str
    secondary_role: str
    domains: dict[str, Domain]
    roles: dict[str, RoleTarget]
    topics: dict[str, Topic]
    weeks: list[Week]
    milestones: list[PromotionMilestone]
    interview_imminent_plan: dict[str, list[str]]

    def all_days(self) -> list[DayEntry]:
        days: list[DayEntry] = []
        for week in self.weeks:
            days.extend(week.days)
        return sorted(days, key=lambda d: d.id)

    def day_by_id(self, day_id: int) -> DayEntry | None:
        for day in self.all_days():
            if day.id == day_id:
                return day
        return None


@dataclass
class ResolveResult:
    topic: str
    passed: bool


@dataclass
class DayProgress:
    day: int
    status: ProgressStatus
    date: date
    commit: str | None = None
    gate_passed: bool | None = None
    journal_ref: str | None = None
    resolve_results: list[ResolveResult] = field(default_factory=list)


@dataclass
class ProgressRecord:
    version: int
    roadmap_version: int
    started: date
    entries: list[DayProgress]

    def entry_for(self, day_id: int) -> DayProgress | None:
        for entry in self.entries:
            if entry.day == day_id:
                return entry
        return None

    def current_day(self) -> int:
        """Lowest day id whose status is neither complete nor skipped."""
        completed_or_skipped = {
            e.day for e in self.entries
            if e.status in (ProgressStatus.COMPLETE, ProgressStatus.SKIPPED)
        }
        day_id = 1
        while day_id in completed_or_skipped:
            day_id += 1
        return day_id
