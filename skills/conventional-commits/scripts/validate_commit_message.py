#!/usr/bin/env python3
"""Validate a commit message against common Conventional Commits 1.0.0 rules."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADER_RE = re.compile(
    r"^(?P<type>[A-Za-z][A-Za-z0-9-]*)(?:\((?P<scope>[^()\r\n]+)\))?(?P<breaking>!)?: (?P<description>\S.*)$"
)
FOOTER_RE = re.compile(r"^(?:[A-Za-z0-9-]+|BREAKING CHANGE|BREAKING-CHANGE)(?:: | #).+$")
BREAKING_FOOTER_RE = re.compile(r"^(BREAKING CHANGE|BREAKING-CHANGE): .+$")
COMMON_TYPES = {
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
}


def read_message(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8").strip("\n")
    if args.message:
        return args.message.strip("\n")
    return sys.stdin.read().strip("\n")


def validate(message: str, strict_types: bool) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []

    if not message.strip():
        return ["ERROR: commit message is empty"]

    lines = message.splitlines()
    header = lines[0]
    match = HEADER_RE.match(header)
    if not match:
        return [
            "ERROR: header must match 'type(scope)!: description' or 'type: description'",
            "ERROR: require ': ' after the type/scope prefix and a non-empty description",
        ]

    typ = match.group("type")
    description = match.group("description")

    if typ.lower() != typ:
        warnings.append("type should be lowercase for consistency")

    if strict_types and typ.lower() not in COMMON_TYPES:
        errors.append(
            "type is not in the common set: "
            + ", ".join(sorted(COMMON_TYPES))
        )

    if description.endswith("."):
        warnings.append("description should usually not end with a period")

    if len(header) > 100:
        warnings.append("header is longer than 100 characters")

    if len(lines) > 1 and lines[1].strip():
        errors.append("body or footers must begin after a blank line")

    footer_lines = collect_footer_lines(lines)
    for line_no, line in footer_lines:
        if not FOOTER_RE.match(line):
            errors.append(f"line {line_no}: footer is not a valid git-trailer style token")
        if line.startswith("Breaking Change") or line.startswith("breaking change"):
            errors.append(f"line {line_no}: BREAKING CHANGE footer token must be uppercase")

    has_bang = bool(match.group("breaking"))
    has_breaking_footer = any(BREAKING_FOOTER_RE.match(line) for _, line in footer_lines)
    if has_breaking_footer and not any(line.strip() == "" for line in lines[1:]):
        errors.append("breaking-change footer must be separated from the header by a blank line")

    if has_bang and not has_breaking_footer:
        warnings.append("breaking change is marked with !; footer is optional but often clearer")

    return [f"ERROR: {e}" for e in errors] + [f"WARN: {w}" for w in warnings]


def collect_footer_lines(lines: list[str]) -> list[tuple[int, str]]:
    if len(lines) < 3:
        return []

    result: list[tuple[int, str]] = []
    for index in range(len(lines) - 1, 1, -1):
        line = lines[index]
        if not line.strip():
            break
        if FOOTER_RE.match(line) or line.startswith(("BREAKING CHANGE", "BREAKING-CHANGE", "Breaking Change", "breaking change")):
            result.append((index + 1, line))
            continue
        if result:
            result.append((index + 1, line))
    return list(reversed(result))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message", nargs="?", help="Commit message to validate. Reads stdin when omitted.")
    parser.add_argument("--file", help="Read commit message from a file.")
    parser.add_argument("--strict-types", action="store_true", help="Require the common conventional type set.")
    args = parser.parse_args()

    problems = validate(read_message(args), args.strict_types)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1 if any(item.startswith("ERROR:") for item in problems) else 0

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
