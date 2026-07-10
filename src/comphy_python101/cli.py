"""Command-line front door for the reference workflows."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from .analysis import summarise_log
from .io import load_basilisk_log, load_regime_map
from .plotting import plot_log, plot_regime_map


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="comphy-python101",
        description="Validated teaching workflows for scientific Python.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    summary = commands.add_parser("summary", help="summarise a Basilisk log")
    summary.add_argument("input", type=Path)

    log_plot = commands.add_parser("plot-log", help="plot a Basilisk log")
    log_plot.add_argument("input", type=Path)
    log_plot.add_argument("--output", type=Path, default=Path("log.png"))

    regime_plot = commands.add_parser("plot-regime", help="plot an Oh–Bo map")
    regime_plot.add_argument("input", type=Path)
    regime_plot.add_argument("--output", type=Path, default=Path("regime-map.png"))
    return parser


def main(arguments: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(arguments)
    if args.command == "summary":
        print(json.dumps(summarise_log(load_basilisk_log(args.input)), indent=2))
    elif args.command == "plot-log":
        output = plot_log(load_basilisk_log(args.input), args.output)
        print(output)
    elif args.command == "plot-regime":
        output = plot_regime_map(load_regime_map(args.input), args.output)
        print(output)
    return 0
