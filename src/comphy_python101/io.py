"""Validated readers for the small teaching datasets."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class SimulationLog:
    """A minimal, explicit schema for a Basilisk-style time-series log."""

    time: FloatArray
    time_step: FloatArray
    kinetic_energy: FloatArray
    minimum_length: FloatArray


@dataclass(frozen=True)
class RegimeCase:
    """One synthetic case in the teaching regime map."""

    case_id: str
    ohnesorge: float
    bond: float
    outcome: str


def _rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header")
        return reader.fieldnames, list(reader)


def _require_columns(path: Path, fields: list[str], required: set[str]) -> None:
    missing = sorted(required.difference(fields))
    if missing:
        raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")


def load_basilisk_log(path: str | Path) -> SimulationLog:
    """Load and validate a four-column Basilisk-style teaching log."""

    source = Path(path)
    fields, rows = _rows(source)
    required = {"t", "dt", "kinetic_energy", "h_min"}
    _require_columns(source, fields, required)
    if not rows:
        raise ValueError(f"{source} contains no data rows")

    columns: dict[str, list[float]] = {name: [] for name in required}
    for line_number, row in enumerate(rows, start=2):
        for name in required:
            try:
                columns[name].append(float(row[name]))
            except (TypeError, ValueError) as error:
                raise ValueError(
                    f"{source}:{line_number}: {name} is not a number",
                ) from error

    time = np.asarray(columns["t"])
    time_step = np.asarray(columns["dt"])
    kinetic_energy = np.asarray(columns["kinetic_energy"])
    minimum_length = np.asarray(columns["h_min"])

    if not all(
        np.all(np.isfinite(values))
        for values in (time, time_step, kinetic_energy, minimum_length)
    ):
        raise ValueError(f"{source} contains non-finite values")
    if np.any(np.diff(time) <= 0):
        raise ValueError(f"{source}: t must be strictly increasing")
    if np.any(time_step <= 0):
        raise ValueError(f"{source}: dt must be strictly positive")
    if np.any(kinetic_energy < 0):
        raise ValueError(f"{source}: kinetic_energy cannot be negative")
    if np.any(minimum_length <= 0):
        raise ValueError(f"{source}: h_min must be strictly positive")

    return SimulationLog(time, time_step, kinetic_energy, minimum_length)


def load_regime_map(path: str | Path) -> list[RegimeCase]:
    """Load and validate the synthetic Oh–Bo outcome table."""

    source = Path(path)
    fields, rows = _rows(source)
    required = {"case_id", "ohnesorge", "bond", "outcome"}
    _require_columns(source, fields, required)
    if not rows:
        raise ValueError(f"{source} contains no data rows")

    allowed = {"no-jet", "one-drop", "multiple-drops"}
    cases: list[RegimeCase] = []
    for line_number, row in enumerate(rows, start=2):
        try:
            ohnesorge_number = float(row["ohnesorge"])
            bond_number = float(row["bond"])
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"{source}:{line_number}: dimensionless values must be numeric",
            ) from error
        outcome = row["outcome"].strip()
        if ohnesorge_number <= 0 or bond_number <= 0:
            raise ValueError(
                f"{source}:{line_number}: Oh and Bo must be strictly positive",
            )
        if outcome not in allowed:
            raise ValueError(
                f"{source}:{line_number}: unknown outcome {outcome!r}",
            )
        cases.append(
            RegimeCase(
                case_id=row["case_id"].strip(),
                ohnesorge=ohnesorge_number,
                bond=bond_number,
                outcome=outcome,
            ),
        )
    return cases
