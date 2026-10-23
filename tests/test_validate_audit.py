"""Regression tests for the generated QA audit artifact contract."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-audit.py"
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


class AuditValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name)
        for name in REQUIRED:
            (self.output / name).write_text("# Example evidence\n", encoding="utf-8")
        self.document = {
            "schema_version": "1.0",
            "operation_mode": "Independent",
            "generated_at": "2026-10-23T01:00:00Z",
            "rules": [
                {
                    "id": "BR-001",
                    "origins": ["qa-discovery"],
                    "sources": [],
                }
            ],
        }
        self.write_json()

    def write_json(self):
        (self.output / "qa-discovered-rules.json").write_text(
            json.dumps(self.document), encoding="utf-8"
        )

    def check(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.output)],
            capture_output=True, text=True, check=False
        )

    def test_valid_audit_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_artifact_fails(self):
        (self.output / "qa-test-matrix.md").unlink()
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing audit artifact: qa-test-matrix.md", result.stderr)

    def test_empty_artifact_fails(self):
        (self.output / "qa-bug-table.md").write_text("  \n", encoding="utf-8")
        self.assertIn("Empty audit artifact", self.check().stderr)

    def test_malformed_json_fails_without_traceback(self):
        (self.output / "qa-discovered-rules.json").write_text("{broken", encoding="utf-8")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Invalid qa-discovered-rules.json", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_duplicate_rule_id_fails(self):
        self.document["rules"].append(dict(self.document["rules"][0]))
        self.write_json()
        self.assertIn("Duplicate rule id: BR-001", self.check().stderr)

    def test_unknown_operation_mode_fails(self):
        self.document["operation_mode"] = "Other"
        self.write_json()
        self.assertIn("operation_mode must be", self.check().stderr)

    def test_timestamp_requires_timezone(self):
        self.document["generated_at"] = "2026-10-23T01:00:00"
        self.write_json()
        self.assertIn("timezone offset", self.check().stderr)

    def test_rules_must_be_array(self):
        self.document["rules"] = {}
        self.write_json()
        self.assertIn("rules must be an array", self.check().stderr)

    def test_nonexistent_directory_fails(self):
        self.output = self.output / "nonexistent"
        self.assertIn("Not an audit directory", self.check().stderr)

    def test_missing_sources_fails(self):
        del self.document["rules"][0]["sources"]
        self.write_json()
        self.assertIn("sources must be an array", self.check().stderr)


if __name__ == "__main__":
    unittest.main()
