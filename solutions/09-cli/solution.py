"""Worked solution for Exercise 09."""

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from comphy_python101 import load_basilisk_log, summarise_log


def main(arguments: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(arguments)
    summary = summarise_log(load_basilisk_log(args.input))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0
