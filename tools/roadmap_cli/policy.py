"""Content policy for FR-035: no secrets, no licensed material, no third-party analogues.

FR-035 was the one requirement with no mechanism at all. It is also the one where a slip
costs most: the learner's master's thesis is owned by an industry partner, so an artifact
that reproduces or closely mirrors that work is a real problem, not a style issue.

None of these checks can be exhaustive. They are tuned to catch the specific, likely
mistakes — pasting a problem statement, committing a key, naming the NDA'd domain — and to
stay quiet otherwise, because a scan that cries wolf gets bypassed.

Extend the lists below as the programme goes on; they are meant to be edited.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Secrets
# ---------------------------------------------------------------------------
# Shapes rather than entropy: entropy scanners produce false positives on test fixtures
# and base64 blobs, which this repository will have plenty of.
SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("Anthropic API key", re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("OpenAI API key", re.compile(r"\bsk-(?!ant-)[A-Za-z0-9]{32,}")),
    ("AWS access key id", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("AWS secret access key", re.compile(
        r"aws_secret_access_key\s*[:=]\s*['\"]?[A-Za-z0-9/+=]{40}")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("Hugging Face token", re.compile(r"\bhf_[A-Za-z0-9]{34,}")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9\-]{10,}")),
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("bearer token literal", re.compile(r"Authorization\s*[:=]\s*['\"]?Bearer\s+[A-Za-z0-9._\-]{20,}")),
]

# A real key assigned to a variable, as opposed to a placeholder. Checked separately so
# that os.environ lookups and obvious dummies stay quiet.
ASSIGNED_KEY = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|passwd)\b\s*[:=]\s*['\"]([^'\"\n]{12,})['\"]")
# Substring, not full match: real placeholders carry a suffix or prefix
# ("your-api-key-here", "sk-xxxx...", "<TOKEN>"). A genuine high-entropy key is very
# unlikely to contain any of these words, and SECRET_PATTERNS catches known key shapes
# independently of this heuristic.
PLACEHOLDER_VALUES = re.compile(
    r"(?i)(your|placeholder|changeme|change-me|dummy|example|sample|fake|redacted|"
    r"not-?a-?real|todo|tbd|insert|xxxx|\.\.\.|^<|^\$\{|^os\.|^getenv)")

# ---------------------------------------------------------------------------
# Licensed material
# ---------------------------------------------------------------------------
# Judge problem statements are copyrighted. R-007 settled that this repository references
# them by title and URL only; these markers catch a pasted statement.
PROBLEM_STATEMENT_MARKERS = [
    re.compile(r"(?im)^\s*Example\s*\d+\s*:\s*$"),
    re.compile(r"(?im)^\s*Constraints\s*:\s*$"),
    re.compile(r"(?im)^\s*(?:Input|Output)\s*:\s*\S"),
    re.compile(r"(?i)\bGiven an (?:integer )?array\b.{0,80}\breturn\b"),
    re.compile(r"(?i)\byou (?:are given|may assume)\b.{0,60}\b(?:array|string|tree|linked list)\b"),
]
# Two or more distinct markers in one file is the signal. One alone is ordinary prose
# ("Input: a list of tokens") and would fire constantly.
PROBLEM_STATEMENT_THRESHOLD = 2

# ---------------------------------------------------------------------------
# Third-party-owned work (FR-035, FR-042)
# ---------------------------------------------------------------------------
# The thesis built an agent orchestrator that triaged code review from merge requests, and
# an industry partner owns it. Nothing here may reproduce it or be a close public analogue.
# These terms are already public in spec.md's FR-042, so listing them leaks nothing new.
NDA_ADJACENT_TERMS = [
    "code review triage",
    "code-review-triage",
    "review triage agent",
    "merge request triage",
    "merge-request triage",
    "pr triage agent",
    "triage the merge request",
]

# Paths that are allowed to discuss the restriction without tripping the check.
NDA_DISCUSSION_ALLOWLIST = (
    ".specify/",
    "specs/",
    "tools/roadmap_cli/policy.py",
    "promoted/briefs/",
    "progress/",
)


# A file may opt out, but only by saying so in its own text and therefore in the diff.
# The canonical case is a scanner's own test fixtures; the learner will have others.
POLICY_IGNORE_MARKER = "roadmap-policy: ignore-file"


def is_ignored(text: str) -> bool:
    """True when a file explicitly opts out of the content scan.

    Deliberately requires the marker to be visible in the file rather than configured
    elsewhere: an exemption should be reviewable in the same diff that relies on it.
    """
    head = "\n".join(text.splitlines()[:40])
    return POLICY_IGNORE_MARKER in head


def find_secrets(text: str) -> list[str]:
    """Return a label per secret-shaped match. Empty list means nothing matched."""
    hits = [label for label, pattern in SECRET_PATTERNS if pattern.search(text)]
    for match in ASSIGNED_KEY.finditer(text):
        value = match.group(2).strip()
        if PLACEHOLDER_VALUES.search(value):
            continue
        if value.startswith(("os.environ", "getenv", "env.", "${")):
            continue
        hits.append(f"hardcoded {match.group(1).lower()}")
    return sorted(set(hits))


def looks_like_problem_statement(text: str) -> bool:
    """True when a file appears to contain a pasted judge problem statement."""
    matched = sum(1 for pattern in PROBLEM_STATEMENT_MARKERS if pattern.search(text))
    return matched >= PROBLEM_STATEMENT_THRESHOLD


def nda_adjacent_terms(text: str) -> list[str]:
    """Return the NDA-adjacent terms present in the text."""
    lowered = text.lower()
    return sorted({term for term in NDA_ADJACENT_TERMS if term in lowered})


def is_allowlisted(repo_relative_path: str) -> bool:
    """Governance and planning files may name the restriction they describe."""
    normalised = repo_relative_path.replace("\\", "/")
    return normalised.startswith(NDA_DISCUSSION_ALLOWLIST)
