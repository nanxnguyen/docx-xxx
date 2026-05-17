#!/usr/bin/env python3

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def exists(*names: str) -> bool:
    return any((ROOT / name).exists() for name in names)


def has_bin(name: str) -> bool:
    return shutil.which(name) is not None


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    candidates: list[list[str]] = []

    if (ROOT / "package.json").exists():
        if has_bin("pnpm"):
            candidates.append(["pnpm", "lint"])
        if has_bin("npm"):
            candidates.append(["npm", "run", "lint", "--silent"])
        if has_bin("yarn"):
            candidates.append(["yarn", "lint"])
        if has_bin("bun"):
            candidates.append(["bun", "run", "lint"])

    if exists("biome.json", "biome.jsonc") and has_bin("biome"):
        candidates.append(["biome", "check", "."])

    if exists("eslint.config.js", "eslint.config.mjs", ".eslintrc", ".eslintrc.js", ".eslintrc.cjs", ".eslintrc.json") and has_bin("eslint"):
        candidates.append(["eslint", "."])

    if exists(".prettierrc", ".prettierrc.json", ".prettierrc.js", "prettier.config.js", "prettier.config.cjs") and has_bin("prettier"):
        candidates.append(["prettier", "--check", "."])

    if not candidates:
        print("Lint: no configured linter found, skipping.")
        return 0

    for cmd in candidates:
        result = run(cmd)
        if result.returncode == 0:
            print(f"Lint OK: {' '.join(cmd)}")
            return 0

    print("Lint failed for all detected commands.")
    for cmd in candidates:
        result = run(cmd)
        print(f"- {' '.join(cmd)} -> exit {result.returncode}")
        output = (result.stdout or result.stderr).strip()
        if output:
            print(output[:1200])
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
