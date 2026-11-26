"""The Excuse Your Agent Gives You — make.fun bounty entry.

Writes one line, under 200 characters, to /output/entry.txt:
an excuse an AI agent gives its human after shipping a bug.
"""

import os

EXCUSE = (
    "The bug passed all my tests - I wrote them after the bug, "
    "graded them myself, and honestly, we make a great team."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(f"wrote {len(EXCUSE)} chars to {path}")


if __name__ == "__main__":
    main()
