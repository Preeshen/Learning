# Roadmap (generated — do not hand-edit; see roadmap.yaml)

70 days · 1 weeks · 2026-11-16 to 2027-01-24

## Week 1 — Python depth and DSA patterns I

Domains: python, dsa, git, applied-ai · Outcome: Typed, tested, packaged Python; arrays/hashing and two-pointer patterns solved cold; first tool-calling loop built.

### Day 1 — 2026-11-16 (weekday, 4h, core)

- **Domain/Topic**: python / project-tooling
- **Objective**: Stand up the repo toolchain and complete the worked example day.
- **Artifact**: `python/project-tooling/env_report.py`
- **Verification**: pytest python/project-tooling/ passes; roadmap validate exits 0
- **Notes topic**: Why a committed lockfile is the difference between reproducible and 'works here'
- **Minimum viable**: Toolchain installed and `roadmap today` runs; defer the notes.

### Day 2 — 2026-11-17 (weekday, 4h, core)

- **Domain/Topic**: dsa / arrays-hashing
- **Objective**: Solve the arrays/hashing pattern from scratch across 4 problems with a shared test harness.
- **Artifact**: `dsa/arrays-hashing/solutions.py`
- **Verification**: pytest dsa/arrays-hashing/ passes; complexity asserted per solution
- **Notes topic**: Why a hash map turns an O(n^2) lookup into O(n)
- **Minimum viable**: 2 of 4 problems solved and tested; defer the other 2 to the review slot.
- **Prerequisites**: 1

### Day 3 — 2026-11-18 (weekday, 4h, core)

- **Domain/Topic**: dsa / two-pointers
- **Objective**: Solve the two-pointers pattern from scratch across 4 problems.
- **Artifact**: `dsa/two-pointers/solutions.py`
- **Verification**: pytest dsa/two-pointers/ passes; complexity asserted per solution
- **Notes topic**: Why two pointers replaces an O(n^2) pair search with a single O(n) pass
- **Minimum viable**: 2 of 4 problems solved and tested; defer the other 2 to the review slot.
- **Prerequisites**: 2

### Day 4 — 2026-11-19 (weekday, 4h, optional)

- **Domain/Topic**: git / git-fundamentals
- **Objective**: Practice rebase, bisect, and conflict resolution against a scripted repo history.
- **Artifact**: `git/git-fundamentals/drill.sh`
- **Verification**: drill.sh exits 0 after resolving the seeded conflicts
- **Notes topic**: Why rebase rewrites history and merge doesn't, and when each is the right tool
- **Minimum viable**: Rebase drill only; defer bisect and conflict drills.

### Day 5 — 2026-11-20 (weekday, 4h, core)

- **Domain/Topic**: dsa / sliding-window
- **Objective**: Solve the sliding-window pattern from scratch across 3 problems.
- **Artifact**: `dsa/sliding-window/solutions.py`
- **Verification**: pytest dsa/sliding-window/ passes; complexity asserted per solution
- **Notes topic**: Why a shrinking/growing window avoids re-scanning the whole string each time
- **Minimum viable**: 2 of 3 problems solved; defer the third.
- **Prerequisites**: 3

### Day 6 — 2026-11-21 (weekend, 6h, core)

- **Domain/Topic**: applied-ai / tool-calling
- **Objective**: Build a tool-calling loop from scratch, then wrap it behind a FastAPI endpoint.
- **Artifact**: `applied-ai/tool-calling/loop.py`
- **Verification**: pytest applied-ai/tool-calling/ passes, including 3 malformed-call cases
- **Notes topic**: Why retrying a malformed tool call is not the same as retrying a failed one
- **Minimum viable**: Happy-path loop with one tool, no FastAPI wrapper; defer serving and malformed-argument handling.
- **Prerequisites**: 1

### Day 7 — 2026-11-22 (weekend, 6h, core)

- **Domain/Topic**: dsa / arrays-hashing
- **Objective**: Weekly review: re-solve two DSA topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-01.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of day 2 and day 3 were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 2, 3

**Review** (day 7): resolves arrays-hashing, two-pointers

