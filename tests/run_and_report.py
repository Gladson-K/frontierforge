"""Run every focused testcase and record full logs in docs/TEST-RESULTS.md.

Usage: python tests/run_and_report.py [--docker]
Exit status is non-zero if any recorded command fails; the report is always written.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "docs" / "TEST-RESULTS.md"
TEST_LINE = re.compile(r"^(test_\S+) \(([^)]+)\) \.\.\. (ok|FAIL|ERROR|skipped.*)$", re.MULTILINE)


def git_output(args):
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def build_commands(include_docker):
    python = sys.executable
    shown = ".venv/bin/python" if python.endswith("/bin/python") else python
    commands = [
        ("local", f"{shown} -m unittest discover -s tests -v",
         [python, "-m", "unittest", "discover", "-s", "tests", "-v"]),
    ]
    for module in ("test_engines", "test_photonic", "test_cellular",
                   "test_reversible", "test_reservoir"):
        commands.append(("local", f"{shown} -m unittest discover -s tests -p {module}.py -v",
                         [python, "-m", "unittest", "discover", "-s", "tests",
                          "-p", f"{module}.py", "-v"]))
    for demo in ("quantum-demo", "neuro-demo", "risk", "photonic-demo",
                 "ca-demo", "reversible-demo", "reservoir-demo"):
        commands.append(("cli", f"{shown} -m frontierforge.cli {demo}",
                         [python, "-m", "frontierforge.cli", demo]))
    if include_docker:
        for name in ("quantum", "neuro", "bayes", "photonic", "cellular",
                     "reversible", "reservoir", "tests"):
            commands.append((
                "docker",
                f"docker build -f docker/Dockerfile.{name} -t frontierforge:{name} . && docker run --rm frontierforge:{name}",
                f"docker build -f docker/Dockerfile.{name} -t frontierforge:{name} . && docker run --rm frontierforge:{name}",
            ))
    return commands


def run(command):
    kind, display, argv = command
    started = time.monotonic()
    try:
        if isinstance(argv, str):
            completed = subprocess.run(argv, cwd=ROOT, shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, text=True,
                                       timeout=1200)
            log, code = completed.stdout, completed.returncode
        else:
            completed = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, text=True,
                                       timeout=1200)
            log, code = completed.stdout, completed.returncode
    except subprocess.TimeoutExpired as exc:
        log, code = (exc.stdout or "") + "\nTIMEOUT after 1200 seconds\n", 124
    return {
        "display": display,
        "code": code,
        "seconds": round(time.monotonic() - started, 3),
        "log": log.rstrip() or "(no output)",
        "tests": TEST_LINE.findall(log),
    }


def fence(text):
    return "````text\n" + text.rstrip() + "\n````"


def render(results, include_docker):
    passed = sum(1 for result in results if result["code"] == 0)
    total_tests = sum(len(result["tests"]) for result in results)
    lines = [
        "# FrontierForge V2 test results",
        "",
        f"- Generated (UTC): `{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}`",
        f"- Python: `{sys.version.split()[0]}`",
        f"- Branch: `{git_output(['rev-parse', '--abbrev-ref', 'HEAD'])}`",
        f"- Commit: `{git_output(['rev-parse', '--short', 'HEAD'])}`",
        f"- Commands passed: `{passed}/{len(results)}`",
        f"- Testcase lines captured: `{total_tests}`",
        f"- Docker pipelines included: `{include_docker}`",
        "",
        "Every command below is recorded even when it fails; full combined "
        "stdout/stderr is preserved in the log blocks. A green status here is "
        "local verification evidence, not a product safety or legal claim.",
        "",
        "## Summary",
        "",
        "| # | Kind | Command | Exit | Seconds | Testcases | Status |",
        "| --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for index, (command, result) in enumerate(zip(build_commands(include_docker), results), 1):
        kind = command[0]
        status = "PASS" if result["code"] == 0 else "FAIL"
        lines.append(
            f"| {index} | {kind} | `{result['display']}` | {result['code']} | "
            f"{result['seconds']} | {len(result['tests'])} | {status} |")
    lines.append("")
    for index, (command, result) in enumerate(zip(build_commands(include_docker), results), 1):
        lines.extend([
            f"## {index}. {command[0]} — {result['display']}",
            "",
            f"- Exit code: `{result['code']}`",
            f"- Duration: `{result['seconds']}s`",
            "",
        ])
        if result["tests"]:
            lines.extend([
                "### Testcase results",
                "",
                "| Test | Module | Result |",
                "| --- | --- | --- |",
            ])
            for name, module, status in result["tests"]:
                lines.append(f"| `{name}` | `{module}` | `{status}` |")
            lines.append("")
        lines.extend(["### Full log", "", fence(result["log"]), ""])
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--docker", action="store_true",
                        help="include Docker build/run pipelines")
    args = parser.parse_args()
    commands = build_commands(args.docker)
    results = [run(command) for command in commands]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(render(results, args.docker), encoding="utf-8")
    failures = [result for result in results if result["code"] != 0]
    print(f"Wrote {REPORT.relative_to(ROOT)}: "
          f"{len(results) - len(failures)}/{len(results)} commands passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
