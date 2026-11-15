"""Tests for the FR-035 content policy: secrets, licensed material, NDA analogues.

roadmap-policy: ignore-file -- this file necessarily contains synthetic secret-shaped
strings, a pasted-looking problem statement, and NDA-adjacent wording, because those are
exactly what it tests. Every credential here is fabricated.

A scan that cries wolf gets bypassed, so the negative cases below matter as much as the
positive ones. Every secret-shaped string here is synthetic.
"""

from __future__ import annotations

import pytest

from tools.roadmap_cli import policy


# --- secrets -------------------------------------------------------------

@pytest.mark.parametrize("snippet,expected_label", [
    ("client = Anthropic(api_key='sk-ant-" + "A" * 40 + "')", "Anthropic API key"),
    ("KEY = 'sk-" + "b" * 40 + "'", "OpenAI API key"),
    ("aws_key = 'AKIA" + "Q" * 16 + "'", "AWS access key id"),
    ("token = 'ghp_" + "c" * 36 + "'", "GitHub token"),
    ("hf = 'hf_" + "d" * 34 + "'", "Hugging Face token"),
    ("-----BEGIN RSA PRIVATE KEY-----", "private key block"),
])
def test_secret_shapes_are_detected(snippet, expected_label):
    assert expected_label in policy.find_secrets(snippet)


@pytest.mark.parametrize("snippet", [
    "api_key = os.environ['ANTHROPIC_API_KEY']",
    "api_key = os.getenv('OPENAI_API_KEY')",
    'api_key = "your-api-key-here"',
    'token = "placeholder"',
    'password = "changeme"',
    'secret = "${VAULT_SECRET}"',
    'api_key = "sk-xxxxxxxxxxxxxxxxxxxx"',
    "# Remember to set api_key before running",
])
def test_placeholders_and_env_lookups_stay_quiet(snippet):
    """The common honest patterns must not fire, or the scan gets ignored."""
    assert policy.find_secrets(snippet) == []


def test_long_hardcoded_api_key_assignment_is_flagged():
    assert policy.find_secrets("api_key = 'f8a93bc1d7e45092aa31'") != []


# --- licensed material ---------------------------------------------------

def test_pasted_problem_statement_is_detected():
    pasted = (
        "Given an integer array nums, return the indices of the two numbers that add up "
        "to target.\n\n"
        "Example 1:\n\n"
        "Input: nums = [2,7,11,15], target = 9\n"
        "Output: [0,1]\n\n"
        "Constraints:\n\n"
        "2 <= nums.length <= 10000\n"
    )
    assert policy.looks_like_problem_statement(pasted)


def test_title_and_url_reference_is_fine():
    """R-007's approved shape: title plus link, no statement text."""
    allowed = ("## Arrays and hashing\n\n"
               "- Two Sum: https://leetcode.com/problems/two-sum/\n"
               "- Group Anagrams: https://leetcode.com/problems/group-anagrams/\n")
    assert not policy.looks_like_problem_statement(allowed)


def test_a_single_marker_alone_does_not_fire():
    """One marker is ordinary prose; the threshold is two distinct markers."""
    assert not policy.looks_like_problem_statement(
        "The harness reads a fixture.\nInput: a list of tokens from the tokenizer.\n")


def test_own_notes_describing_a_solution_do_not_fire():
    notes = ("## Internal mechanisms\n\n"
             "A hash map turns the complement lookup into O(1), so one pass suffices. "
             "The trade is O(n) extra space.\n")
    assert not policy.looks_like_problem_statement(notes)


# --- NDA-adjacent work ---------------------------------------------------

def test_nda_adjacent_wording_is_detected():
    text = "An agent that performs code review triage on incoming merge requests."
    assert "code review triage" in policy.nda_adjacent_terms(text)


def test_unrelated_agent_work_is_not_flagged():
    text = "An agent that scores retrieval trajectories against a labelled trace set."
    assert policy.nda_adjacent_terms(text) == []


@pytest.mark.parametrize("path,allowed", [
    ("specs/001-ai-engineering-roadmap/spec.md", True),
    (".specify/memory/constitution.md", True),
    ("tools/roadmap_cli/policy.py", True),
    ("promoted/briefs/flagship.md", True),
    ("applied-ai/react-loop-scratch/react.py", False),
    ("dsa/arrays-hashing/solutions.py", False),
])
def test_governance_files_may_name_the_restriction(path, allowed):
    """spec.md has to be able to state FR-042 without tripping the check."""
    assert policy.is_allowlisted(path) is allowed


def test_live_repo_has_no_blocking_policy_findings():
    """Regression guard: the committed tree must stay clean under FR-035."""
    from tools.roadmap_cli.cli import _scan_paths, _tracked_text_files

    blocking = [f for f in _scan_paths(_tracked_text_files()) if f[0] == "BLOCK"]
    assert blocking == [], blocking
