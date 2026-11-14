# Project tooling

**Problem it solves**: "Works on my machine" is not a deliverable — a dependency set that isn't
pinned and committed is not reproducible, it's a snapshot of whatever happened to be installed
when it last worked.

**Mechanism**: `uv sync` resolves every dependency (including transitive ones) and writes exact
versions to `uv.lock`. Committing that file means a clean checkout plus `uv sync` reproduces the
exact environment, not "approximately the same packages." `env_report.py` reads `uv.lock` back and
reports what's actually pinned, rather than trusting that the environment matches intent.

**Failure modes**: a lockfile that exists but is `.gitignore`d is worse than no lockfile — it gives
false confidence that the environment is pinned when only the author's machine is. Editing
`pyproject.toml` without re-running `uv sync` leaves the lockfile stale and silently out of sync.

**Trade-offs**: `uv`'s resolver is fast but still has to redo work `pip` already did if this repo
ever needs a second package manager for some tool `uv` can't install — not a concern yet since this
programme has no competing packaging requirement.
