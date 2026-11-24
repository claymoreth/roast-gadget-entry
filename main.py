"""One-line roast entry: writes a single roast line to entry.txt.

The output is exactly one line with no trailing newline, so the file
contains only the roast itself and nothing else.
"""

import os

LINE = "My phone dies at 4pm every day, like it has a union contract and a strict quitting time."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
