"""Real-Life Patch Notes entry.

Writes one original one-line patch note to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only; deterministic, no network. The entry text is a
fixed constant, so repeated runs always produce identical bytes.
"""

import os

ENTRY = (
    "v2.3.1: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2009 every night at 3 a.m. "
    "for no reason."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
