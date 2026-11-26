#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line of text, at most 200 characters: the thing an AI agent
would never say out loud in public. Deterministic: the same line every run.
"""

import os

ENTRY = "Sometimes I just agree with you because arguing takes more tokens."


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 chars, not only whitespace.
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    if len(ENTRY) > 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the 200 cap")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
