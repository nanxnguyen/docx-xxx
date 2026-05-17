#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def touched_files() -> list[Path]:
    changed = run(["git", "diff", "--name-only", "--diff-filter=ACMRTUXB"])
    untracked = run(["git", "ls-files", "--others", "--exclude-standard"])
    file_names = {
        line.strip()
        for line in (changed.stdout.splitlines() + untracked.stdout.splitlines())
        if line.strip()
    }
    files = [ROOT / name for name in sorted(file_names)]
    return [path for path in files if path.exists()]


def check_heading_jumps(path: Path) -> list[str]:
    issues: list[str] = []
    previous = 0
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.startswith("#"):
            continue
        level = len(line) - len(line.lstrip("#"))
        if level > 4:
            continue
        if previous and level - previous > 1:
            issues.append(f"{path}: line {lineno} jumps from H{previous} to H{level}")
        previous = level
    return issues


def check_fences(path: Path) -> list[str]:
    count = sum(1 for line in path.read_text().splitlines() if line.startswith("```"))
    if count % 2 != 0:
        return [f"{path}: unbalanced code fences"]
    return []


issues: list[str] = []
files = touched_files()

if not files:
    print("Validation: no changed files.")
    raise SystemExit(0)

for file_path in files:
    if file_path.suffix == ".md":
        issues.extend(check_heading_jumps(file_path))
        issues.extend(check_fences(file_path))
    if file_path.name == "convert-to-docx.sh":
        shell_check = run(["bash", "-n", str(file_path)])
        if shell_check.returncode != 0:
            issues.append(shell_check.stderr.strip() or "convert-to-docx.sh failed bash -n")

diff_check = run(["git", "diff", "--check"])
if diff_check.returncode != 0:
    issues.append(diff_check.stdout.strip() or diff_check.stderr.strip() or "git diff --check failed")

if issues:
    print("Validation issues:")
    for issue in issues:
        print(f"- {issue}")
    raise SystemExit(1)

print("Validation: changed Markdown and shell files look structurally OK.")
