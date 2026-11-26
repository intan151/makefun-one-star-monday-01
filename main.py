#!/usr/bin/env python3
"""One Star for Monday — make.fun entry program.

Writes a single line of plain text to /output/entry.txt: a one-star
review of Monday as if Monday were a restaurant, at most 25 words.
Deterministic, no network, no input.
"""

import os

ENTRY = (
    "One star. Monday seated me by the kitchen, served cold coffee "
    "and burnt toast, then charged me for the weekend I never got."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: what was written must be byte-identical to ENTRY.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 180, "entry must be 1-180 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"
    assert written == written.strip(), "entry must not have leading/trailing whitespace"
    assert len(written.split()) <= 25, "entry must be at most 25 words"


if __name__ == "__main__":
    main()
