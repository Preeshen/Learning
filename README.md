# AI Engineering Learning Playground

A 19-week, 133-day structured programme toward AI engineering interview and portfolio readiness,
governed by [`.specify/memory/constitution.md`](.specify/memory/constitution.md) and specified in
[`specs/001-ai-engineering-roadmap/`](specs/001-ai-engineering-roadmap/).

## Start a session

```powershell
uv sync                      # first time only: creates .venv, installs the roadmap CLI
uv run roadmap today         # what to build today
```

ML and Applied AI days need their optional dependency groups the first time you reach one:

```powershell
uv sync --extra ml --extra applied-ai   # numpy/torch/scikit-learn, fastapi, mcp, etc.
```

Each topic's `NOTES.md` must carry all eleven sections required by constitution Principle IV.
Start a new topic by copying the template:

```powershell
Copy-Item tools/templates/NOTES.template.md <domain>/<topic>/NOTES.md
```

Build it, verify it, fill in `NOTES.md`, commit, then:

```powershell
uv run roadmap check         # mechanised day-completion gate
uv run roadmap complete --built "..." --broke "..." --learned "..."
```

Weekly, or before a push:

```powershell
uv run roadmap audit         # every completed day, not just today
uv run roadmap scan          # secrets, licensed material, third-party-owned work
```

Install the pre-commit hook once to get both automatically — the content scan blocks a
commit, the day gate only warns:

```powershell
Copy-Item tools/hooks/pre-commit .git/hooks/pre-commit
```

See [`specs/001-ai-engineering-roadmap/quickstart.md`](specs/001-ai-engineering-roadmap/quickstart.md)
for the full bootstrap and validation walkthrough, and
[`specs/001-ai-engineering-roadmap/contracts/cli-contract.md`](specs/001-ai-engineering-roadmap/contracts/cli-contract.md)
for every `roadmap` command.

## Layout

- `roadmap/roadmap.yaml` — single source of truth for the 133-day programme (never hand-edit
  `roadmap/ROADMAP.md`; it is generated)
- `progress/` — machine-readable status (`progress.yaml`) and the prose journal (`journal.md`)
- `python/`, `dsa/`, `git/`, `systems/`, `ml/`, `applied-ai/`, `cloud/` — the seven in-scope
  domains; each day's artifact, test, and `NOTES.md` land under a topic subdirectory here
- `promoted/README.md` — pointer records for CV projects, built in separate repositories
- `tools/roadmap_cli/` — the `roadmap` CLI and validator
