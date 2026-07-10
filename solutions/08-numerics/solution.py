"""Worked solution for Exercise 08."""

from collections.abc import Sequence

import numpy as np
from numpy.typing import NDArray

from comphy_python101 import central_difference


def convergence_study(
    point_counts: Sequence[int],
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    if any(count < 3 for count in point_counts):
        raise ValueError("each grid needs at least three points")
    spacings: list[float] = []
    errors: list[float] = []
    for count in point_counts:
        coordinate = np.linspace(0.0, 2 * np.pi, count)
        numerical = central_difference(coordinate, np.sin(coordinate))
        spacings.append(float(coordinate[1] - coordinate[0]))
        errors.append(float(np.max(np.abs(numerical - np.cos(coordinate)))))
    spacing = np.asarray(spacings)
    error = np.asarray(errors)
    order = np.log(error[:-1] / error[1:]) / np.log(spacing[:-1] / spacing[1:])
    return spacing, error, order
