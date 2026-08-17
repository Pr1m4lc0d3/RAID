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


if __name__ == "__main__":
    unittest.main()
