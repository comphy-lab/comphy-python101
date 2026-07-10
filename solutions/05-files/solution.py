"""Worked solution for Exercise 05."""

import csv
from pathlib import Path


def summarise_log(path: Path) -> dict[str, float | int]:
    required = {"t", "kinetic_energy", "h_min"}
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        fields = set(reader.fieldnames or [])
        missing = required - fields
        if missing:
            raise ValueError(f"missing columns: {', '.join(sorted(missing))}")
        rows = list(reader)
    if not rows:
        raise ValueError("input contains no data")
    return {
        "samples": len(rows),
        "final_time": float(rows[-1]["t"]),
        "peak_kinetic_energy": max(float(row["kinetic_energy"]) for row in rows),
        "minimum_length": min(float(row["h_min"]) for row in rows),
    }
