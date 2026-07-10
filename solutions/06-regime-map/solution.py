"""Worked solution for Exercise 06."""

import csv
from collections import Counter
from pathlib import Path


def count_outcomes(path: Path) -> dict[str, int]:
    allowed = {"no-jet", "one-drop", "multiple-drops"}
    case_ids: set[str] = set()
    counts: Counter[str] = Counter()
    with path.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            case_id = row["case_id"]
            outcome = row["outcome"]
            if case_id in case_ids:
                raise ValueError(f"duplicate case ID: {case_id}")
            if outcome not in allowed:
                raise ValueError(f"unknown outcome: {outcome}")
            case_ids.add(case_id)
            counts[outcome] += 1
    return {outcome: counts[outcome] for outcome in sorted(allowed)}
