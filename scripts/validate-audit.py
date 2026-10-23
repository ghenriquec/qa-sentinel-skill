#!/usr/bin/env python3
"""Validate the artifact contract of a QA Sentinel audit package.

This is structural validation, not a determination of audit completeness,
the presence/absence of defects, or the quality of the evidence.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

REQUIRED = (
    "qa-audit-report.md",
    "qa-bug-table.md",
    "qa-test-matrix.md",
    "qa-traceability-matrix.md",
    "qa-discovered-rules.json",
    "qa-business-rules-matrix.md",
    "qa-rule-source-comparison.md",
    "qa-domain-gaps.md",
    "qa-rule-conflicts.md",
    "qa-evidence-index.md",
)
MODES = {"Independent", "Integrated", "Hybrid"}


def validate(directory: Path) -> list[str]:
    errors: list[str] = []
    if not directory.is_dir():
        return [f"Not an audit directory: {directory}"]

    for filename in REQUIRED:
        path = directory / filename
        if path.is_symlink():
            errors.append(f"Symlink is not an acceptable audit artifact: {filename}")
        elif not path.is_file():
            errors.append(f"Missing audit artifact: {filename}")
        else:
            try:
                if not path.read_text(encoding="utf-8").strip():
                    errors.append(f"Empty audit artifact: {filename}")
            except (OSError, UnicodeError) as exc:
                errors.append(f"Unreadable audit artifact {filename}: {type(exc).__name__}")

    json_path = directory / "qa-discovered-rules.json"
    if any("qa-discovered-rules.json" in error for error in errors):
        return errors

    try:
        document = json.loads(json_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid qa-discovered-rules.json: {type(exc).__name__}")
        return errors

    if not isinstance(document, dict):
        return errors + ["qa-discovered-rules.json must be a JSON object"]

    if not isinstance(document.get("schema_version"), str) or not document["schema_version"].strip():
        errors.append("Missing schema_version")
    mode = document.get("operation_mode")
    if not isinstance(mode, str) or mode not in MODES:
        errors.append("operation_mode must be Independent, Integrated or Hybrid")

    generated = document.get("generated_at")
    if not isinstance(generated, str):
        errors.append("generated_at must be an ISO-8601 timestamp")
    else:
        try:
            stamp = datetime.fromisoformat(generated.replace("Z", "+00:00"))
            if stamp.tzinfo is None or stamp.utcoffset() is None:
                errors.append("generated_at must include a timezone offset")
        except ValueError:
            errors.append("generated_at must be an ISO-8601 timestamp")

    rules = document.get("rules")
    if not isinstance(rules, list):
        errors.append("rules must be an array")
        return errors

    seen: set[str] = set()
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            errors.append(f"rules[{index}] must be an object")
            continue
        rule_id = rule.get("id")
        if not isinstance(rule_id, str) or not rule_id.strip():
            errors.append(f"rules[{index}] missing non-empty id")
        elif rule_id in seen:
            errors.append(f"Duplicate rule id: {rule_id}")
        else:
            seen.add(rule_id)
        if not isinstance(rule.get("sources"), list):
            errors.append(f"rules[{index}] sources must be an array")
        if not isinstance(rule.get("origins"), list):
            errors.append(f"rules[{index}] origins must be an array")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Path to an audit output directory")
    args = parser.parse_args()
    errors = validate(args.directory)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("VALID: QA Sentinel audit artifact structure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
