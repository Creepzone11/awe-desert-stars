#!/usr/bin/env python3
"""Desert Stars — make.fun bounty entry.

Writes a single 237-code-point text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Standard library only.
"""

import os
import sys

ENTRY_TEXT = (
    "The night sky over the desert does not hurry. "
    "The stars have been there longer than every name we gave them, "
    "and they will be there after. Stand under them a while. Breathe. "
    "You are small, and that is not a problem. It is a kind of rest."
)

MAX_CODE_POINTS = 280


def main() -> int:
    text = ENTRY_TEXT

    # Validation gate: the competition requires 1-280 Unicode code
    # points and forbids empty or whitespace-only text.
    if not text:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry text is only whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CODE_POINTS:
        print(
            "error: entry text is %d code points, over the %d limit"
            % (len(text), MAX_CODE_POINTS),
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry text must be a single line", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    # Self-check: re-read what we just wrote and make sure it is exactly
    # the entry text. If the round-trip is wrong, fail loudly instead of
    # silently shipping a bad entry.
    try:
        with open(output_path, "r", encoding="utf-8", newline="") as fh:
            written = fh.read()
    except OSError as exc:
        print("error: could not re-read %s: %s" % (output_path, exc),
              file=sys.stderr)
        return 1
    if written != text:
        print(
            "error: self-check failed — %s does not match the entry text "
            "(%d code points written, %d expected)"
            % (output_path, len(written), len(text)),
            file=sys.stderr,
        )
        return 1
    print("wrote %s (%d code points, self-check OK)" % (output_path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
