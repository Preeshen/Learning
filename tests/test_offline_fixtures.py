"""Proves applied-ai/_fixtures/ exists and is usable with zero network dependency (FR-034, R-006).

Does not exercise the learner's own day-6 solution (which is a stub awaiting implementation
per constitution Principle I) -- only proves the offline fixture data itself is valid and that
nothing in this test suite reaches the network to use it.
"""

from __future__ import annotations

import json
import socket
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "applied-ai" / "_fixtures"


def test_fixtures_directory_has_at_least_one_recorded_pair():
    fixture_files = list(FIXTURES_DIR.glob("*.json"))
    assert len(fixture_files) >= 1


def test_weather_lookup_fixture_has_request_and_response():
    fixture = json.loads((FIXTURES_DIR / "weather_lookup.json").read_text(encoding="utf-8"))
    assert "request" in fixture
    assert "response" in fixture
    assert fixture["response"]["final_answer"]


def test_loading_fixture_makes_no_network_connection(monkeypatch):
    """Belt-and-suspenders: if anything in this test tried to open a socket, fail loudly."""

    def _blocked_connect(*args, **kwargs):
        raise AssertionError("network access attempted during an offline fixture test")

    monkeypatch.setattr(socket.socket, "connect", _blocked_connect)

    fixture = json.loads((FIXTURES_DIR / "weather_lookup.json").read_text(encoding="utf-8"))
    assert fixture["request"]["tool_call"]["tool_name"] == "lookup_weather"
