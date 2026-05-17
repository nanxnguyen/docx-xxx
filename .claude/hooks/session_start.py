#!/usr/bin/env python3

from __future__ import annotations

import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def run(cmd: list[str]) -> str:
    try:
        completed = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        return completed.stdout.strip()
    except Exception:
        return ""


branch = run(["git", "branch", "--show-current"]) or "(no-branch)"
changed = run(["git", "status", "--short"])
changed_count = len([line for line in changed.splitlines() if line.strip()])

print("Claude Code session context")
print(f"- repo: {ROOT.name}")
print(f"- cwd: {os.getcwd()}")
print(f"- branch: {branch}")
print(f"- changed files: {changed_count}")
print("- repo type: documentation-only workspace")
print("- primary workflow: edit markdown topics, guides, and lightweight shell script")
print("- do not touch _Archive unless user explicitly asks")
