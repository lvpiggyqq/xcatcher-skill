#!/usr/bin/env python3
"""Validate public marketplace manifests against their canonical schemas."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from jsonschema import Draft7Validator, Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
CASES = (
    (
        "plugin.json",
        "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        Draft202012Validator,
    ),
    (
        "mcp.json",
        "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
        Draft202012Validator,
    ),
    (
        ".cursor-plugin/plugin.json",
        "https://raw.githubusercontent.com/cursor/plugins/main/schemas/plugin.schema.json",
        Draft7Validator,
    ),
)


def load_remote_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "xcatcher-manifest-ci/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def main() -> None:
    for relative_path, schema_url, validator_class in CASES:
        document = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
        schema = load_remote_json(schema_url)
        validator = validator_class(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
        if errors:
            rendered = "\n".join(f"- {'/'.join(map(str, error.path))}: {error.message}" for error in errors)
            raise AssertionError(f"{relative_path} failed validation:\n{rendered}")
        print(f"PASS: {relative_path}")

    expected_json = (
        ".mcp.json",
        ".codex-plugin/plugin.json",
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        ".github/plugin/marketplace.json",
        "gemini-extension.json",
    )
    for relative_path in expected_json:
        json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
        print(f"PASS: {relative_path}")

    assert (ROOT / "assets/xcatcher-400.png").stat().st_size > 0
    assert (ROOT / "skills/xcatcher/SKILL.md").is_file()


if __name__ == "__main__":
    main()
