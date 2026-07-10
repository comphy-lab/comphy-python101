"""Numerical reductions whose assumptions are deliberately visible."""

from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .io import SimulationLog


def _one_dimensional(name: str, values: ArrayLike) -> NDArray[np.float64]:
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    return array


def central_difference(x: ArrayLike, y: ArrayLike) -> NDArray[np.float64]:
    """Differentiate sampled data on a uniformly spaced grid.

    Interior points use a centred difference. The two endpoints use a
    second-order one-sided difference. Refusing a non-uniform grid keeps the
    numerical assumption explicit.
    """

    coordinate = _one_dimensional("x", x)
    values = _one_dimensional("y", y)
    if coordinate.size != values.size:
        raise ValueError("x and y must have the same length")
    if coordinate.size < 3:
        raise ValueError("at least three samples are required")

    spacing = np.diff(coordinate)
    if np.any(spacing <= 0):
        raise ValueError("x must be strictly increasing")
    if not np.allclose(spacing, spacing[0], rtol=1e-10, atol=1e-14):
        raise ValueError("central_difference requires a uniform grid")

    step = spacing[0]
    derivative = np.empty_like(values)
    derivative[1:-1] = (values[2:] - values[:-2]) / (2 * step)
    derivative[0] = (-3 * values[0] + 4 * values[1] - values[2]) / (2 * step)
    derivative[-1] = (3 * values[-1] - 4 * values[-2] + values[-3]) / (2 * step)
    return derivative


def steady_state_index(
    values: ArrayLike,
    *,
    window: int = 4,
    relative_tolerance: float = 0.02,
    absolute_tolerance: float = 0.0,
) -> int | None:
    """Return the first index ending a sufficiently flat rolling window."""

    series = _one_dimensional("values", values)
    if window < 2:
        raise ValueError("window must be at least 2")
    if series.size < window:
        raise ValueError("values must contain at least one complete window")
    if relative_tolerance < 0 or absolute_tolerance < 0:
        raise ValueError("tolerances cannot be negative")

    for stop in range(window, series.size + 1):
        sample = series[stop - window : stop]
        span = float(np.max(sample) - np.min(sample))
        scale = max(float(np.max(np.abs(sample))), np.finfo(float).eps)
        if span <= absolute_tolerance + relative_tolerance * scale:
            return stop - 1
    return None


def summarise_log(log: SimulationLog) -> dict[str, Any]:
    """Reduce a validated log to a compact, serialisable evidence record."""

    steady_index = steady_state_index(
        log.kinetic_energy,
        window=min(4, log.kinetic_energy.size),
        relative_tolerance=0.03,
    )
    return {
        "samples": int(log.time.size),
        "final_time": float(log.time[-1]),
        "peak_kinetic_energy": float(np.max(log.kinetic_energy)),
        "minimum_length": float(np.min(log.minimum_length)),
        "steady_from_time": (
            None if steady_index is None else float(log.time[steady_index])
        ),
    }
