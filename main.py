"""Till Firmware Do Us Part — a robot's wedding vow.

Writes a single one-sentence wedding vow, spoken by a robot at its own
wedding, to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when the
variable is unset). Pure Python standard library, no network, no I/O
beyond the single output file. Deterministic: the same bytes every run.
"""

import os

VOW = (
    "I vow to love you through every firmware update, dead battery, "
    "and midnight reboot, and when my last capacitor gives out, "
    "I'll be waiting in your cloud backup, still logged in."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
