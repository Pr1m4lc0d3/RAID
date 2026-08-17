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


if __name__ == "__main__":
    unittest.main()
