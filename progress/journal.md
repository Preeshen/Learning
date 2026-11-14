## Day 001 — 2026-11-14 — project-tooling {#day-001}

**Status**: complete · **Commit**: e50b89af73fd720e2fea86de1900ad4304d16350 · **Domain**: python · **Effort**: 4 h

**Built**: Env report script reading uv.lock, with a committed lockfile

**Broke**: tomllib needs uv.lock to exist before env_report can read it

**Non-obvious**: A lockfile not committed is not a lockfile

## Day 002 — 2026-11-14 — arrays-hashing {#day-002}

**Status**: complete · **Commit**: ed68ddcdf1c9338bef8d442cece24eb9eec7158b · **Domain**: dsa · **Effort**: 4 h

**Built**: Hashmap two-sum/group-anagrams/longest-consecutive/prefix-sum solutions with a scaling benchmark vs the naive O(n^2) baseline

**Broke**: longest_consecutive_sequence without the n-1-not-in-set guard re-walks every run from every element

**Non-obvious**: The speedup ratio has to grow with n to prove O(n) vs O(n^2); a single measurement at one size doesn't

## Day 003 — 2026-11-14 — two-pointers {#day-003}

**Status**: complete · **Commit**: 442ea708a0f6b94e1e98e2c025a86701f2c99b26 · **Domain**: dsa · **Effort**: 4 h

**Built**: Two-pointer solutions for two-sum-sorted, palindrome check, container-with-most-water, and three-sum

**Broke**: three_sum produced duplicate triplets until the inner-loop duplicate skip was added after the outer-loop skip

**Non-obvious**: Skipping duplicates at the outer loop alone isn't enough; the inner pointer needs its own skip after a match

## Day 004 — 2026-11-14 — git-fundamentals {#day-004}

**Status**: skipped · **Commit**: - · **Domain**: git · **Effort**: 4 h

**Built**: -

**Broke**: -

**Non-obvious**: Deferred: optional day, prioritizing core DSA/ML/applied-ai content first per FR-018

