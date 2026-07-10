"""Worked solution for Integration lab 12."""

import csv
from pathlib import Path

import numpy as np
from numpy.typing import ArrayLike, NDArray

from comphy_python101 import central_difference, load_basilisk_log


def differentiate_minimum_length(
    time: ArrayLike, minimum_length: ArrayLike
) -> NDArray[np.float64]:
    return central_difference(time, minimum_length)


def write_reduced_log(source: Path, output: Path) -> Path:
    log = load_basilisk_log(source)
    derivative = differentiate_minimum_length(log.time, log.minimum_length)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["t", "h_min", "dh_min_dt"])
        writer.writeheader()
        for time, length, rate in zip(
            log.time, log.minimum_length, derivative, strict=True
        ):
            writer.writerow({"t": time, "h_min": length, "dh_min_dt": rate})
    return output
