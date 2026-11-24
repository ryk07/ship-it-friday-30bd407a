"""Ship It Friday — one-line git commit message entry.

Writes a single original commit message to /output/entry.txt.
Stdlib only. The message text is embedded here; no file reads,
no network, no environment access.
"""

import os

ENTRY = (
    "feat: rewrote auth from scratch at 4:59pm Friday \u2014 skipped the tests "
    "(confidence is a test), deploying to prod now, see you Monday "
    "(if we're still up)"
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
