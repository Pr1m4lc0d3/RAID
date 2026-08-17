import sys
import unittest
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "skills" / "raid-provision" / "assets"
sys.path.insert(0, str(ASSETS))

import evidence_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def read(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


class TestSectionParsing(unittest.TestCase):
    def test_parses_every_required_section(self):
        sections = evidence_lint.parse_sections(read("evidence-good.md"))
        self.assertEqual(set(sections), set(evidence_lint.REQUIRED_SECTIONS))

    def test_parses_bullets_with_line_numbers(self):
        sections = evidence_lint.parse_sections(read("evidence-good.md"))
        proven = sections["Proven"]
        self.assertEqual(len(proven), 2)
        line_no, text = proven[0]
        self.assertIsInstance(line_no, int)
        self.assertTrue(text.startswith("three seats"))

    def test_missing_section_is_an_error(self):
        text = "# x\n\n## Proven\n- a cap — exhibit: f1 — kind: log — verified: no\n"
        messages = [f.message for f in evidence_lint.lint_text(text)]
        self.assertIn("missing required section: Limits", messages)

    def test_good_fixture_has_no_missing_section_errors(self):
        findings = evidence_lint.lint_text(read("evidence-good.md"))
        missing = [f for f in findings if "missing required section" in f.message]
        self.assertEqual(missing, [])


class TestRequiredFields(unittest.TestCase):
    def test_field_labels_extracts_labels(self):
        bullet = "a cap — exhibit: f1 — kind: log — verified: no"
        self.assertEqual(
            evidence_lint.field_labels(bullet),
            {"exhibit", "kind", "verified"},
        )

    def test_field_labels_handles_multiword_label(self):
        bullet = "a limit — bears on: some claim"
        self.assertEqual(evidence_lint.field_labels(bullet), {"bears on"})

    def test_proven_bullet_needs_exhibit(self):
        messages = [f.message for f in evidence_lint.lint_text(read("evidence-bad.md"))]
        self.assertIn("Proven: bullet is missing 'exhibit:'", messages)

    def test_claimed_bullet_needs_reason(self):
        messages = [f.message for f in evidence_lint.lint_text(read("evidence-bad.md"))]
        self.assertIn("Claimed but unproven: bullet is missing 'reason:'", messages)

    def test_limits_bullet_needs_bears_on(self):
        messages = [f.message for f in evidence_lint.lint_text(read("evidence-bad.md"))]
        self.assertIn("Limits: bullet is missing 'bears on:'", messages)

    def test_findings_carry_the_offending_line_number(self):
        findings = [
            f for f in evidence_lint.lint_text(read("evidence-bad.md"))
            if "missing 'reason:'" in f.message
        ]
        self.assertEqual(len(findings), 1)
        self.assertGreater(findings[0].line_no, 0)

    def test_good_fixture_has_no_field_errors(self):
        findings = evidence_lint.lint_text(read("evidence-good.md"))
        field_errors = [f for f in findings if "missing '" in f.message]
        self.assertEqual(field_errors, [])


if __name__ == "__main__":
    unittest.main()
