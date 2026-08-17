#!/usr/bin/env python3
"""evidence-lint — check .monkeys/evidence-inventory.md carries the fields a human needs.

The linter checks FORM. It cannot know whether an exhibit really proves what the
line says, only whether the line names the exhibit, its kind, and whether anyone
checked it. A line that omits those is not wrong; it is uncheckable, which reads
as settled when it is not.
"""

import re
from typing import NamedTuple

REQUIRED_SECTIONS = (
    "Proven",
    "Claimed but unproven",
    "Limits",
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
