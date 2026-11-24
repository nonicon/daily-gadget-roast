#!/usr/bin/env python3
"""Daily Gadget Roast — one-line roast of the gadget I use every day.

Writes a single original roast line (at most 200 characters) to
/output/entry.txt, as required by the make.fun bounty
"One-Line Roast: The Gadget You Use Every Day".

The line roasts my wireless earbuds: their battery gauge jumps from
47% to 12% to dead with no warning, like a resignation handed in
in three percentages.

Before writing, validate_entry() enforces the kit gate (1-200 chars,
single line, not blank) and main() reads the file back to prove the
write landed byte-for-byte. The output directory honours
MAKEFUN_OUTPUT_DIR and defaults to /output.
"""

import os
import sys

ROAST = "My earbuds die at 47%, then 12%, then nothing — a resignation letter in three percentages."


def validate_entry(line: str) -> str:
    """Enforce the kit gate: UTF-8 text, 1-200 chars, single line, not blank."""
    text = line.strip()
    if not text:
        raise ValueError("roast line is blank")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast line is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("roast line must be a single line")
    return text


def main() -> int:
    line = validate_entry(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip read-back: the file must hold exactly the validated line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt does not match the validated roast line")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
