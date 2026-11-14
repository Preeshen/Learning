"""Day 1 worked example: report the reproducible environment this repo runs on.

Reads pyproject.toml and uv.lock so the report reflects what is actually pinned, rather than
what happens to be installed on this machine right now.
"""

from __future__ import annotations

import platform
import sys
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def read_pinned_dependencies() -> list[str]:
    lock_path = REPO_ROOT / "uv.lock"
    if not lock_path.exists():
        return []
    data = tomllib.loads(lock_path.read_text(encoding="utf-8"))
    return sorted(
        f"{pkg['name']}=={pkg['version']}"
        for pkg in data.get("package", [])
        if pkg.get("name") != "ai-engineering-roadmap"
    )


def build_report() -> dict:
    return {
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "executable": sys.executable,
        "pinned_dependency_count": len(read_pinned_dependencies()),
        "lockfile_committed": (REPO_ROOT / "uv.lock").exists(),
    }


def main() -> None:
    report = build_report()
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
