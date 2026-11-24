#!/usr/bin/env python3
"""One-Liner Laugh Lab: one line, 200 characters max.

A robot vacuum's excuse after eating a sock, written to /output/entry.txt.
Deterministic: the same line every run, no input, no network, no randomness.
The line is deadpan machine voice with a legal twist: the sock is not
food, it is a loiterer under arrest, and the punchline is the bail it
could not pay.
"""

import os

LINE = (
    "I didn't eat your sock. I arrested it for loitering on my floor "
    "\u2014 bail was one dryer sheet, and it couldn't pay."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
