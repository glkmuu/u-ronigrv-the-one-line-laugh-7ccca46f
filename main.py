"""The One-Line Laugh: write one funny line to entry.txt.

A single deterministic line, stdlib only, no network. The program
writes exactly one sentence to the entry file and nothing else, so
every run produces byte-identical output.
"""

import os

LINE = "My toaster has two settings: bread, and a smoke alarm audition."


def main() -> None:
    # The gate allows 1-200 characters and exactly one sentence.
    if not 1 <= len(LINE) <= 200 or LINE.strip() != LINE:
        raise ValueError("line must be a single sentence of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
