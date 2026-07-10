"""Worked solution for Exercise 11."""

import json
from pathlib import Path

from comphy_python101 import load_basilisk_log, summarise_log
from comphy_python101.plotting import plot_log


def build_evidence(source: Path, output: Path) -> tuple[Path, Path]:
    log = load_basilisk_log(source)
    summary = summarise_log(log)
    output.mkdir(parents=True, exist_ok=True)
    summary_path = output / "summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    figure_path = plot_log(log, output / "log.png")
    return summary_path, figure_path
