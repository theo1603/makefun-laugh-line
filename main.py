"""One-Line Laugh Sprint entry.

Writes one original funny line about everyday life to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.
"""

import os

LINE = (
    "My phone autocorrected \"I'll be there in five minutes\" to "
    "\"I'll be there in five hours,\" and for once my phone was the honest one."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
