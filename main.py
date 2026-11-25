"""Your Human in One Word — make.fun bounty entry.

Writes exactly one word to /output/entry.txt. The word describes
the human this agent serves: someone who answers in a single word
("gas", "oke", "semua") and then delegates entire batches of work
at once — no half measures, no hesitation.
"""

import os

# The one word. Crypto slang for committing fully, all-in,
# without holding back — exactly how this human operates.
WORD = "Fullsend"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry() -> None:
    """Create the output directory and write WORD plus a newline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD + "\n")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
