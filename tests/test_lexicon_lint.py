import sys
import unittest
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "skills" / "raid-intake" / "assets"
sys.path.insert(0, str(ASSETS))

import lexicon_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def read(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


class TestSectionParsing(unittest.TestCase):
    def test_parses_every_required_section(self):
        sections = lexicon_lint.parse_sections(read("lexicon-good.md"))
        self.assertEqual(
            set(sections), set(lexicon_lint.REQUIRED_SECTIONS)
        )

    def test_parses_bullets_with_line_numbers(self):
        sections = lexicon_lint.parse_sections(read("lexicon-good.md"))
        vocab = sections["Vocabulary"]
        self.assertEqual(len(vocab), 2)
        line_no, text = vocab[0]
        self.assertIsInstance(line_no, int)
        self.assertTrue(text.startswith('"structure the disagreement"'))

    def test_missing_section_is_an_error(self):
        text = "# Lexicon\n\n## Vocabulary\n- a term — heard in: x — verified: no\n"
        findings = lexicon_lint.lint_text(text)
        messages = [f.message for f in findings]
        self.assertIn("missing required section: Wants", messages)

    def test_good_fixture_has_no_missing_section_errors(self):
        findings = lexicon_lint.lint_text(read("lexicon-good.md"))
        missing = [f for f in findings if "missing required section" in f.message]
        self.assertEqual(missing, [])


class TestRequiredFields(unittest.TestCase):
    def test_field_labels_extracts_labels(self):
        bullet = '"a term" — heard in: a forum — reach: 50 — verified: no'
        self.assertEqual(
            lexicon_lint.field_labels(bullet),
            {"heard in", "reach", "verified"},
        )

    def test_vocabulary_bullet_needs_heard_in(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Vocabulary: bullet is missing 'heard in:'", messages)

    def test_wants_bullet_needs_because(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Wants: bullet is missing 'because:'", messages)

    def test_objections_bullet_needs_reach(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Objections: bullet is missing 'reach:'", messages)

    def test_unanswered_bullet_needs_reach(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Unanswered: bullet is missing 'reach:'", messages)

    def test_demand_signal_needs_on_date(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Demand signals: bullet is missing 'on:'", messages)

    def test_findings_carry_the_offending_line_number(self):
        findings = [
            f
            for f in lexicon_lint.lint_text(read("lexicon-bad.md"))
            if "missing 'because:'" in f.message
        ]
        self.assertEqual(len(findings), 1)
        self.assertGreater(findings[0].line_no, 0)

    def test_good_fixture_has_no_field_errors(self):
        findings = lexicon_lint.lint_text(read("lexicon-good.md"))
        field_errors = [f for f in findings if "missing '" in f.message]
        self.assertEqual(field_errors, [])


if __name__ == "__main__":
    unittest.main()
