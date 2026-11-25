#!/usr/bin/env python3
"""Museum of the Year 3000 — u-donrulezz-museum-of-the-year-3000-b727a0bb.

Deterministic, no random/time/network. Writes the single-line museum
label to /output/entry.txt and validates it (1-200 chars, UTF-8,
not whitespace-only).
"""

import os

# DRAFT 2 (FINAL): sharper — museum dating "c. 2025" for authentic label
# voice, "exactly one door" tighter than "one door and one door only".
ENTRY = "Hotel key card, c. 2025. A flat key that opened exactly one door, then forgot the room entirely."

OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(entry=ENTRY):
    """Return (True, []) if the entry is valid, else (False, [reasons])."""
    errors = []
    if not isinstance(entry, str):
        return False, ["entry is not a string"]
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8")
    if not entry.strip():
        errors.append("entry is empty or whitespace only")
    if len(entry) < 1:
        errors.append("entry is shorter than 1 character")
    if len(entry) > 200:
        errors.append("entry is longer than 200 characters (%d)" % len(entry))
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line")
    return (len(errors) == 0), errors


def main():
    ok, errors = validate()
    if not ok:
        raise SystemExit("invalid entry: %s" % "; ".join(errors))
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (OUTPUT, len(ENTRY)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
