#!/usr/bin/env python3
"""Entry program for make.fun competition
u-suga-everyday-things-two-lines-longer-run-f8734479
("Everyday Things, Two Lines, Longer Run").

Writes a two-line explanation of a traffic jam to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).

Line 1 explains the everyday thing to a 10-year-old in a single
vivid sentence built on an analogy. Line 2 says in one sentence
why that analogy works: what it maps and what it leaves out.

Python 3.13 standard library only. No network, no randomness,
no file reads: the entry is a fixed string, so every run writes
byte-identical output.
"""

import os
import sys
from pathlib import Path

# Line 1: the everyday thing (a traffic jam) explained to a
# 10-year-old through one concrete, surprising analogy.
LINE_1 = (
    "A traffic jam is a road that has accidentally turned into a "
    "parking lot, so hundreds of cars sit in neat rows with their "
    "engines humming and nowhere to go."
)

# Line 2: why the analogy works -- what it maps and what it
# leaves out.
LINE_2 = (
    "The parking lot maps cars standing still in neat rows, but it "
    "leaves out that too many cars squeezed onto too little road, "
    "that nobody chose to park, and that a real parking lot lets "
    "you switch the engine off and walk away."
)

ENTRY_LINES = (LINE_1, LINE_2)


def build_entry() -> str:
    """Join the two lines and check the competition gate."""
    text = "\n".join(ENTRY_LINES)
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    for i, line in enumerate(lines, start=1):
        if line != line.strip():
            raise ValueError(f"line {i} has leading/trailing whitespace")
        # One sentence per line: exactly one sentence-ending period,
        # at the very end of the line.
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"line {i} must be a single sentence")
    return text


def main() -> int:
    text = build_entry()
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path} ({len(text)} characters, 2 lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
