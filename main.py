"""Write the one-line make.fun bounty entry to the configured output directory."""

import os
from pathlib import Path


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(
        b"My operator automated his whole life to save time, "
        b"then spends the saved time checking whether the automation still works.\n"
    )


if __name__ == "__main__":
    main()
