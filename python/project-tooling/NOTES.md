# Project tooling

<!--
Migrated to the eleven-section template (constitution v1.1.0, Principle IV / FR-038) on
2026-11-15. The four sections below carry your original day-1 prose verbatim, moved under
the closest-matching new heading:

  "Problem it solves" -> Why it matters
  "Mechanism"         -> Internal mechanisms
  "Failure modes"     -> Failure modes and common mistakes
  "Trade-offs"        -> Alternatives and trade-offs

Seven sections are genuinely new and are yours to fill. `roadmap check 1` will keep
failing until they have bodies — that is correct, not a regression.
-->

## Learning objectives

<!-- What can you do now that you could not before? Be specific and testable. -->

## Prerequisites

<!-- Which concepts and which earlier topics does this one assume? -->

## Conceptual explanation

<!-- The idea in plain prose, no code. -->

## Why it matters

"Works on my machine" is not a deliverable — a dependency set that isn't
pinned and committed is not reproducible, it's a snapshot of whatever happened to be installed
when it last worked.

## Internal mechanisms

`uv sync` resolves every dependency (including transitive ones) and writes exact
versions to `uv.lock`. Committing that file means a clean checkout plus `uv sync` reproduces the
exact environment, not "approximately the same packages." `env_report.py` reads `uv.lock` back and
reports what's actually pinned, rather than trusting that the environment matches intent.

## Real-world applications

<!-- Where does this appear in production systems you know of or have read about? -->

## Alternatives and trade-offs

`uv`'s resolver is fast but still has to redo work `pip` already did if this repo
ever needs a second package manager for some tool `uv` can't install — not a concern yet since this
programme has no competing packaging requirement.

## Failure modes and common mistakes

A lockfile that exists but is `.gitignore`d is worse than no lockfile — it gives
false confidence that the environment is pinned when only the author's machine is. Editing
`pyproject.toml` without re-running `uv sync` leaves the lockfile stale and silently out of sync.

## Interview questions

<!-- At least three questions, each with the answer you would actually say out loud. -->

1.
2.
3.

## Assessment criteria

<!-- How would you judge whether someone else understands this? -->

## Revision notes

<!-- The compressed form — what you re-read the night before an interview. -->
