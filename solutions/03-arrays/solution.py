"""Worked solution for Exercise 03."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def central_difference(x: ArrayLike, y: ArrayLike) -> NDArray[np.float64]:
    coordinate = np.asarray(x, dtype=float)
    values = np.asarray(y, dtype=float)
    if coordinate.ndim != 1 or values.ndim != 1:
        raise ValueError("x and y must be one-dimensional")
    if coordinate.size != values.size or coordinate.size < 3:
        raise ValueError("x and y need the same length of at least three")
    spacing = np.diff(coordinate)
    if np.any(spacing <= 0) or not np.allclose(spacing, spacing[0]):
        raise ValueError("x must be a strictly increasing uniform grid")

    step = spacing[0]
    derivative = np.empty_like(values)
    derivative[1:-1] = (values[2:] - values[:-2]) / (2 * step)
    derivative[0] = (-3 * values[0] + 4 * values[1] - values[2]) / (2 * step)
    derivative[-1] = (3 * values[-1] - 4 * values[-2] + values[-3]) / (2 * step)
    return derivative
