## Day 001 — 2026-11-14 — project-tooling {#day-001}

**Status**: complete · **Commit**: e50b89af73fd720e2fea86de1900ad4304d16350 · **Domain**: python · **Effort**: 4 h

**Built**: Env report script reading uv.lock, with a committed lockfile

**Broke**: tomllib needs uv.lock to exist before env_report can read it

**Non-obvious**: A lockfile not committed is not a lockfile

