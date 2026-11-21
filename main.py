#!/usr/bin/env python3
"""The Lamp — a make.fun bounty entry.

Writes one 224-code-point line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt). Standard library only, no network.
"""

import os
import sys

ENTRY_TEXT = (
    "The lamp turns once, and the dark takes the light out to sea. "
    "A ship the keeper will never see finds the shore by it. "
    "The light has reached across this water for a hundred years, "
    "and the sea has never once asked it to hurry."
)

# One still image: a lamp turning, a ship finding the shore, a hundred
# years of light that has never once been asked to hurry.

MAX_CODE_POINTS = 280


def validate(text):
    """Return None if the text passes, else a message naming the
    first problem: it must be non-empty, not just blanks, at most
    MAX_CODE_POINTS long, and a single line."""
    if not text:
        return "nothing to write — the entry text is empty"
    if not text.strip():
        return "nothing to write — the entry text is all whitespace"
    if len(text) > MAX_CODE_POINTS:
        return (
            "entry text is %d code points long, beyond the %d limit"
            % (len(text), MAX_CODE_POINTS)
        )
    if "\n" in text or "\r" in text:
        return "entry text must be one single line"
    return None


def main() -> int:
    text = ENTRY_TEXT

    # Check first, before any file is touched, so a bad entry fails
    # here instead of halfway through writing.
    problem = validate(text)
    if problem is not None:
        print("error: %s" % problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())

    # Read the file back and compare: a short write or an encoding
    # slip should be caught here, not slip through to the judge.
    try:
        with open(output_path, "r", encoding="utf-8", newline="") as fh:
            written = fh.read()
    except OSError as exc:
        print("error: read-back of %s failed: %s" % (output_path, exc),
              file=sys.stderr)
        return 1
    if written != text:
        print("error: what came back differs — %s holds %d code points, "
              "but the entry is %d" % (output_path, len(written), len(text)),
              file=sys.stderr)
        return 1
    print("wrote %s (%d code points, verified by read-back)"
          % (output_path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
