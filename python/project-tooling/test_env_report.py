import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "env_report", Path(__file__).resolve().parent / "env_report.py"
)
env_report = importlib.util.module_from_spec(_SPEC)
sys.modules["env_report"] = env_report
_SPEC.loader.exec_module(env_report)


def test_build_report_has_expected_keys():
    report = env_report.build_report()
    assert set(report) == {
        "python_version", "platform", "executable",
        "pinned_dependency_count", "lockfile_committed",
    }


def test_python_version_is_312_or_newer():
    report = env_report.build_report()
    major, minor, _ = (int(x) for x in report["python_version"].split("."))
    assert (major, minor) >= (3, 12)
