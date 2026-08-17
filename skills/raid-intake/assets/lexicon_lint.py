#!/usr/bin/env python3
"""lexicon-lint — check .monkeys/lexicon.md carries the fields a human needs.

The linter checks FORM. It cannot know whether a captured phrase is real, only
whether the line says where it was heard, how far it reached, and whether anyone
checked it. A line that omits those is not wrong; it is uncheckable, which is
worse, because it reads as settled.
"""

import re
from typing import NamedTuple

REQUIRED_SECTIONS = (
    "Vocabulary",
    "Wants",
    "Objections",
    "Unanswered",
    "Demand signals",
)

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
BULLET_RE = re.compile(r"^-\s+(.*\S)\s*$")


class Finding(NamedTuple):
    line_no: int
    level: str
    message: str


def parse_sections(text):
    """Return {section_name: [(line_no, bullet_text), ...]} for '## ' headings."""
    sections = {}
    current = None
    for line_no, line in enumerate(text.splitlines(), start=1):
        heading = SECTION_RE.match(line)
        if heading:
            current = heading.group(1)
            sections.setdefault(current, [])
            continue
        if current is None:
            continue
        bullet = BULLET_RE.match(line)
        if bullet:
            sections[current].append((line_no, bullet.group(1)))
    return sections


def lint_text(text):
    findings = []
    sections = parse_sections(text)
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            findings.append(
                Finding(0, "error", f"missing required section: {name}")
            )
    return findings
