"""The `roadmap` CLI — see contracts/cli-contract.md for the full contract."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import typer
import yaml
from rich.console import Console

from tools.roadmap_cli import coverage as coverage_mod
from tools.roadmap_cli import render as render_mod
from tools.roadmap_cli.loader import (
    LoadError,
    PROGRESS_PATH,
    REPO_ROOT,
    load_progress,
    load_roadmap,
    topics_due,
)
from tools.roadmap_cli.models import DayEntry, ProgressStatus, Roadmap
from tools.roadmap_cli.validate import (
    REQUIRED_NOTES_SECTIONS,
    artifact_is_unimplemented,
    notes_missing_sections,
    validate_journal,
    validate_progress,
    validate_roadmap,
)

app = typer.Typer(add_completion=False)
console = Console()

JOURNAL_PATH = REPO_ROOT / "progress" / "journal.md"
__version__ = "0.1.0"


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", help="Show the CLI version and exit."),
):
    if version:
        console.print(f"roadmap {__version__}")
        raise typer.Exit(0)
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())


def _load_roadmap_or_exit() -> Roadmap:
    try:
        return load_roadmap()
    except LoadError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(2)


def _day_card(r: Roadmap, day: DayEntry, progress_entries: dict, due_topics: list[str]) -> None:
    status_line = (
        f"Day {day.id} of {r.total_days} · {day.date} · {day.day_type} · "
        f"{day.effort_hours} h · {day.priority} · tier: {day.tier}"
    )
    console.print(status_line)
    console.print(f"Domain: {day.domain} · Topic: {day.topic}")
    console.print()
    console.print("OBJECTIVE")
    console.print(f"  {day.objective}")
    console.print()
    console.print(f"ARTIFACT        {day.artifact}")
    console.print(f"VERIFICATION    {day.verification}")
    console.print(f"NOTES           {day.notes_topic}")
    console.print()
    topic = r.topics.get(day.topic)
    if topic and topic.references:
        console.print("REFERENCES (read the problem here before you start)")
        for ref in topic.references:
            console.print(f"  - {ref['title']}: {ref['url']}")
        console.print()
    console.print("GATE")
    for g in day.gate:
        console.print(f"  [ ] {g}")
    console.print()
    console.print("IF SHORT ON TIME")
    console.print(f"  {day.minimum_viable}")
    if day.prerequisites:
        console.print()
        statuses = []
        for p in day.prerequisites:
            entry = progress_entries.get(p)
            state = entry.status.value if entry else "pending"
            statuses.append(f"day {p} ({state})")
        console.print(f"PREREQUISITES   {', '.join(statuses)}")
    if due_topics:
        console.print()
        console.print(f"DUE FOR RESOLVE {', '.join(due_topics)}")


@app.command()
def today(
    day: int | None = typer.Argument(None),
    json_out: bool = typer.Option(False, "--json"),
    next_n: int | None = typer.Option(None, "--next"),
    days_until_interview: int | None = typer.Option(None, "--days-until-interview"),
):
    r = _load_roadmap_or_exit()
    progress = load_progress()
    progress_by_day = {e.day: e for e in progress.entries}

    if days_until_interview is not None:
        role = r.primary_role
        topics = r.interview_imminent_plan.get(role, [])
        if json_out:
            print(json.dumps({"role": role, "drill_topics": topics,
                                       "days_until_interview": days_until_interview}))
        else:
            console.print(f"Interview in {days_until_interview} days — drill subset for {role}:")
            for t in topics:
                console.print(f"  - {t}")
        raise typer.Exit(0)

    current = day if day is not None else progress.current_day()

    if next_n is not None:
        days = [d for d in r.all_days() if current <= d.id < current + next_n]
        if json_out:
            print(json.dumps([d.id for d in days]))
        else:
            for d in days:
                console.print(f"Day {d.id}: {d.objective}")
        raise typer.Exit(0)

    target = r.day_by_id(current)
    if target is None:
        console.print("Programme complete!")
        console.print()
        console.print("Milestones:")
        for m in coverage_mod.milestone_status(r, progress):
            if m["ready"]:
                console.print(f"  READY  {m['name']} ({m['id']}) — build in a separate repo; "
                              f"record at {m['record_path']}")
            else:
                console.print(f"  NOT YET  {m['name']} ({m['id']}) — "
                              f"unmet prerequisite days: {m['unmet_prerequisite_days']}")
        raise typer.Exit(0)

    due_topics = topics_due(r, progress)
    if json_out:
        print(json.dumps({"day": target.id, "objective": target.objective,
                                   "artifact": target.artifact, "due_for_resolve": due_topics}))
    else:
        _day_card(r, target, progress_by_day, due_topics)
    raise typer.Exit(0)


def _gate_results(r: Roadmap, day: DayEntry) -> list[tuple[str, bool, str]]:
    results = []

    artifact_path = REPO_ROOT / day.artifact
    results.append(("artifact exists", artifact_path.exists(), str(day.artifact)))

    test_dir = artifact_path.parent
    has_test_files = test_dir.exists() and any(test_dir.glob("test_*.py"))
    if has_test_files:
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_dir), "-q"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        tests_ok = proc.returncode == 0
        tests_msg = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else proc.stderr[:120]
    else:
        # Not every artifact is code (e.g. a weekly review's artifact is a generated .md file).
        # Absence of a test_*.py file means "not applicable," not "failing."
        tests_ok = True
        tests_msg = "not applicable — no test_*.py file for this artifact"
    results.append(("tests pass", tests_ok, tests_msg))

    if day.artifact.startswith("progress/reviews/"):
        # A review day's prose (Constitution audit, Next week) lives in the review file
        # itself; there is no separate topic NOTES.md to check.
        notes_ok = artifact_path.exists() and artifact_path.stat().st_size > 0
        notes_msg = str(day.artifact)
    else:
        notes_path = test_dir / "NOTES.md"
        if not notes_path.exists():
            notes_ok = False
            notes_msg = f"missing — copy tools/templates/NOTES.template.md to {notes_path.name}"
        else:
            # Constitution v1.1.0 Principle IV / FR-038: all eleven sections, each with a body.
            missing = notes_missing_sections(notes_path.read_text(encoding="utf-8"))
            notes_ok = not missing
            filled = len(REQUIRED_NOTES_SECTIONS) - len(missing)
            notes_msg = (f"{filled}/{len(REQUIRED_NOTES_SECTIONS)} sections"
                         + (f" — missing: {', '.join(missing)}" if missing else ""))
    results.append(("notes complete", notes_ok, notes_msg))

    # Principle VIII (skeleton-first half): a day cannot complete on an unimplemented stub.
    if artifact_path.exists() and artifact_path.suffix == ".py":
        stub = artifact_is_unimplemented(artifact_path.read_text(encoding="utf-8"))
        results.append(("implementation written", not stub,
                        "still a skeleton — NotImplementedError present" if stub
                        else "no stub markers remain"))

    measurement_ok = True
    measurement_msg = "no measurement required"
    if day.measurement is not None:
        results_path = REPO_ROOT / day.measurement.results_path
        measurement_ok = results_path.exists()
        measurement_msg = str(day.measurement.results_path)
    results.append(("measurement committed", measurement_ok, measurement_msg))

    commit_proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
                                  capture_output=True, text=True)
    commit_ok = commit_proc.returncode == 0
    results.append(("working tree has a commit", commit_ok, commit_proc.stdout.strip()[:8]))

    return results


@app.command()
def check(day: int | None = typer.Argument(None), json_out: bool = typer.Option(False, "--json")):
    r = _load_roadmap_or_exit()
    progress = load_progress()
    current = day if day is not None else progress.current_day()
    target = r.day_by_id(current)
    if target is None:
        console.print(f"No such day: {current}")
        raise typer.Exit(2)

    results = _gate_results(r, target)
    if json_out:
        print(json.dumps({"day": current,
                                   "results": [{"name": n, "passed": p, "detail": d}
                                               for n, p, d in results]}))
    else:
        console.print(f"Day {current} · {target.domain}/{target.topic}")
        console.print()
        failed = 0
        for name, passed, detail in results:
            mark = "[green]PASS[/green]" if passed else "[red]FAIL[/red]"
            failed += 0 if passed else 1
            console.print(f"  [{mark}] {name:<28} {detail}")
        console.print()
        console.print(f"{failed} of {len(results)} checks failed — "
                       f"{'day complete' if failed == 0 else 'day not complete'}.")
    raise typer.Exit(0 if all(p for _, p, _ in results) else 1)


def _save_progress(progress_entries: list[dict]) -> None:
    PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "roadmap_version": 1,
        "started": str(date.today()),
        "entries": progress_entries,
    }
    with PROGRESS_PATH.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(payload, fh, sort_keys=False)


def _raw_progress_entries() -> list[dict]:
    if not PROGRESS_PATH.exists():
        return []
    with PROGRESS_PATH.open("r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}
    return list(raw.get("entries", []))


@app.command()
def complete(
    built: str = typer.Option(None, "--built"),
    broke: str = typer.Option(None, "--broke"),
    learned: str = typer.Option(None, "--learned"),
    skip: bool = typer.Option(False, "--skip"),
    carry: bool = typer.Option(False, "--carry"),
    resolve: list[str] = typer.Option([], "--resolve"),
    force: bool = typer.Option(False, "--force"),
    day: int | None = typer.Argument(None),
):
    r = _load_roadmap_or_exit()
    progress = load_progress()
    current = day if day is not None else progress.current_day()
    target = r.day_by_id(current)
    if target is None:
        console.print(f"No such day: {current}")
        raise typer.Exit(2)

    status_proc = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT,
                                  capture_output=True, text=True)
    dirty = bool(status_proc.stdout.strip())

    resolve_results = []
    for item in resolve:
        topic, _, outcome = item.partition(":")
        resolve_results.append({"topic": topic, "passed": outcome == "pass"})

    entries = _raw_progress_entries()
    entries = [e for e in entries if e["day"] != current]

    if skip:
        entries.append({"day": current, "status": "skipped", "date": str(date.today()),
                         "journal_ref": f"day-{current:03d}"})
        _save_progress(entries)
        _append_journal(target, "skipped", built or "-", broke or "-", learned or "-", None)
        console.print(f"Day {current} recorded as skipped.")
        raise typer.Exit(0)

    if carry:
        entries.append({"day": current, "status": "carried", "date": str(date.today()),
                         "journal_ref": f"day-{current:03d}"})
        _save_progress(entries)
        console.print(f"Day {current} recorded as carried.")
        raise typer.Exit(0)

    if dirty:
        console.print("[red]Working tree is dirty — commit or stash before completing.[/red]")
        console.print(status_proc.stdout)
        raise typer.Exit(2)

    gate_results = _gate_results(r, target)
    gate_passed = all(p for _, p, _ in gate_results)
    if not gate_passed and not force:
        console.print("[red]Gate failed — refusing to record. Use --force to record honestly.[/red]")
        raise typer.Exit(1)

    if not built or not broke or not learned:
        console.print("[red]--built, --broke, and --learned are all required.[/red]")
        raise typer.Exit(2)

    commit_proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
                                  capture_output=True, text=True)
    if commit_proc.returncode != 0:
        console.print("[red]No commit found for this day.[/red]")
        raise typer.Exit(2)
    commit_sha = commit_proc.stdout.strip()

    entries.append({
        "day": current, "status": "complete", "date": str(date.today()),
        "commit": commit_sha, "gate_passed": gate_passed,
        "journal_ref": f"day-{current:03d}",
        "resolve_results": resolve_results,
    })
    _save_progress(entries)
    _append_journal(target, "complete", built, broke, learned, commit_sha, resolve_results)
    console.print(f"Day {current} recorded complete (commit {commit_sha[:8]}).")
    raise typer.Exit(0)


def _append_journal(day: DayEntry, status: str, built: str, broke: str, learned: str,
                     commit_sha: str | None, resolve_results: list[dict] | None = None) -> None:
    JOURNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = JOURNAL_PATH.read_text(encoding="utf-8") if JOURNAL_PATH.exists() else ""
    ref = f"day-{day.id:03d}"
    lines = [
        f"## Day {day.id:03d} — {date.today()} — {day.topic} {{#{ref}}}",
        "",
        f"**Status**: {status} · **Commit**: {commit_sha or '-'} · "
        f"**Domain**: {day.domain} · **Effort**: {day.effort_hours} h",
        "",
        f"**Built**: {built}",
        "",
        f"**Broke**: {broke}",
        "",
        f"**Non-obvious**: {learned}",
    ]
    if resolve_results:
        for rr in resolve_results:
            outcome = "PASSED" if rr["passed"] else "FAILED"
            lines.append("")
            lines.append(f"**Re-solve**: {rr['topic']} — {outcome}")
    lines.append("")
    lines.append("")
    JOURNAL_PATH.write_text(existing + "\n".join(lines), encoding="utf-8")


def _recovery_note(week_obj, progress) -> str:
    """FR-017: surface missed-day/consecutive-missed-day/missed-week recovery rules with a
    named re-entry point, directly in the review's Generated section."""
    week_day_ids = sorted(d.id for d in week_obj.days)
    statuses = {
        day_id: next(
            (e.status for e in progress.entries if e.day == day_id), ProgressStatus.PENDING
        )
        for day_id in week_day_ids
    }
    skipped_ids = [d for d in week_day_ids if statuses[d] == ProgressStatus.SKIPPED]
    re_entry = progress.current_day()

    if len(skipped_ids) == len(week_day_ids) and week_day_ids:
        return (f"- **Full week missed.** Re-entry point: day {re_entry}. "
                f"No renumbering — resume there next session.\n")

    consecutive_run = 0
    max_consecutive = 0
    for day_id in week_day_ids:
        if statuses[day_id] == ProgressStatus.SKIPPED:
            consecutive_run += 1
            max_consecutive = max(max_consecutive, consecutive_run)
        else:
            consecutive_run = 0

    if max_consecutive >= 3:
        return (f"- **3+ consecutive days skipped this week.** Re-entry point: day {re_entry}.\n")
    if skipped_ids:
        return (f"- Missed day(s) this week: {', '.join(str(d) for d in skipped_ids)}. "
                f"Re-entry point: day {re_entry}.\n")
    return ""


@app.command()
def review(week: int | None = typer.Argument(None), regenerate: bool = typer.Option(False, "--regenerate")):
    r = _load_roadmap_or_exit()
    progress = load_progress()
    week_obj = None
    if week is not None:
        week_obj = next((w for w in r.weeks if w.number == week), None)
    else:
        current = progress.current_day()
        week_obj = next((w for w in r.weeks if any(d.id == current for d in w.days)), r.weeks[0])
    if week_obj is None:
        console.print(f"No such week: {week}")
        raise typer.Exit(2)

    out_path = REPO_ROOT / week_obj.review.output_path
    if out_path.exists() and not regenerate:
        console.print(f"[red]{out_path} already exists. Use --regenerate to overwrite.[/red]")
        raise typer.Exit(1)

    completed = [e for e in progress.entries
                 if e.day in {d.id for d in week_obj.days} and e.status == ProgressStatus.COMPLETE]
    skipped = [e for e in progress.entries
               if e.day in {d.id for d in week_obj.days} and e.status == ProgressStatus.SKIPPED]
    carried = [e for e in progress.entries
               if e.day in {d.id for d in week_obj.days} and e.status == ProgressStatus.CARRIED]
    core_effort_used = sum(
        d.effort_hours for d in week_obj.days
        if d.priority == "core" and any(e.day == d.id and e.status == ProgressStatus.COMPLETE
                                         for e in progress.entries)
    )
    core_budget = sum(d.effort_hours for d in week_obj.days if d.priority == "core")

    recovery_note = _recovery_note(week_obj, progress)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    start = week_obj.days[0].date
    end = week_obj.days[-1].date
    content = f"""# Week {week_obj.number:02d} Review — {start} to {end}

## Generated

- Completed: {len(completed)} / {len(week_obj.days)} · Skipped: {len(skipped)} · Carried: {len(carried)}
- Core effort used: {core_effort_used} h of {core_budget} h budgeted
- Topics due for re-solve: {', '.join(week_obj.review.resolves)}
{recovery_note}
## Re-solve results

| Topic | Result | Action |
|---|---|---|

## Constitution audit

(fill in after auditing this week's commits against Principles I-VII)

## Next week

(cut optional days if behind; keep all core days — FR-007)
"""
    out_path.write_text(content, encoding="utf-8")
    console.print(f"Wrote {out_path}")
    raise typer.Exit(0)


@app.command()
def validate(strict: bool = typer.Option(False, "--strict"), json_out: bool = typer.Option(False, "--json")):
    r = _load_roadmap_or_exit()
    progress = load_progress()
    journal_text = JOURNAL_PATH.read_text(encoding="utf-8") if JOURNAL_PATH.exists() else ""

    findings = validate_roadmap(r)
    findings += validate_progress(progress, r, journal_text)
    findings += validate_journal(progress, journal_text)

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warn"]

    if json_out:
        print(json.dumps({
            "summary": f"{r.total_days} days · {len(r.weeks)} weeks · {len(r.topics)} topics · "
                       f"{len(r.milestones)} milestones",
            "errors": [f.message for f in errors],
            "warnings": [f.message for f in warnings],
        }))
    else:
        console.print(f"roadmap.yaml ................ {r.total_days} days · {len(r.weeks)} weeks · "
                      f"{len(r.topics)} topics · {len(r.milestones)} milestones")
        for f in errors:
            console.print(f"[red][ERROR][/red] {f.rule_id}  {f.message}")
        for f in warnings:
            console.print(f"[yellow][WARN][/yellow]  {f.rule_id}  {f.message}")
        console.print(f"{len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (strict and warnings):
        raise typer.Exit(1)
    raise typer.Exit(0)


@app.command()
def coverage(role: str | None = typer.Option(None, "--role"), json_out: bool = typer.Option(False, "--json")):
    r = _load_roadmap_or_exit()
    progress = load_progress()

    if role is not None:
        detail = coverage_mod.role_detail(r, progress, role)
        if json_out:
            print(json.dumps(detail))
        else:
            for d in detail["days"]:
                mark = "done" if d["done"] else "pending"
                console.print(f"  day {d['id']} ({d['domain']}/{d['topic']}) — {mark}")
        raise typer.Exit(0)

    rows = coverage_mod.role_coverage(r, progress)
    shares = coverage_mod.domain_share(r)
    milestones = coverage_mod.milestone_status(r, progress)
    if json_out:
        print(json.dumps({"roles": rows, "domain_share": shares, "milestones": milestones}))
    else:
        console.print(f"{'Role':<28}{'Tier':<12}{'Days':>6}{'Done':>6}{'Readiness':>12}")
        for row in rows:
            console.print(f"{row['name']:<28}{row['tier']:<12}{row['days']:>6}{row['done']:>6}"
                          f"{row['readiness']:>11.0%}")
        console.print()
        console.print("Domain share: " + " · ".join(f"{k} {v:.0%}" for k, v in shares.items()))
        console.print()
        console.print("Milestones:")
        for m in milestones:
            if m["ready"]:
                console.print(f"  [green]READY[/green] {m['name']} ({m['id']}) — "
                              f"build in a separate repo; record at {m['record_path']}")
            else:
                console.print(f"  [yellow]NOT YET[/yellow] {m['name']} ({m['id']}) — "
                              f"unmet prerequisite days: {m['unmet_prerequisite_days']}")
    raise typer.Exit(0)


@app.command()
def render(check_only: bool = typer.Option(False, "--check")):
    r = _load_roadmap_or_exit()
    if check_only:
        if render_mod.is_stale(r):
            console.print("[red]Generated files are stale or hand-edited.[/red]")
            raise typer.Exit(1)
        console.print("Generated files are up to date.")
        raise typer.Exit(0)
    render_mod.render(r)
    console.print(f"wrote {render_mod.ROADMAP_MD.relative_to(REPO_ROOT)} "
                  f"({r.total_days} days, {len(r.weeks)} weeks)")
    console.print(f"wrote {render_mod.MILESTONES_MD.relative_to(REPO_ROOT)} "
                  f"({len(r.milestones)} milestones)")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()
