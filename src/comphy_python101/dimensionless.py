"""Small dimensionless-number functions with explicit physical contracts."""

from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike, NDArray

ScalarOrArray = float | NDArray[np.float64]


def _positive(name: str, value: ArrayLike) -> NDArray[np.float64]:
    array = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    if np.any(array <= 0):
        raise ValueError(f"{name} must be strictly positive")
    return array


def _scalar_or_array(
    operation: Callable[[], NDArray[np.float64] | np.float64],
) -> ScalarOrArray:
    result = np.asarray(operation(), dtype=float)
    return float(result) if result.ndim == 0 else result


def capillary_time(
    density: ArrayLike,
    length: ArrayLike,
    surface_tension: ArrayLike,
) -> ScalarOrArray:
    r"""Return the inertio-capillary time :math:`\sqrt{\rho L^3/\sigma}`."""

    rho = _positive("density", density)
    scale = _positive("length", length)
    sigma = _positive("surface_tension", surface_tension)
    return _scalar_or_array(lambda: np.sqrt(rho * scale**3 / sigma))


def reynolds(
    density: ArrayLike,
    speed: ArrayLike,
    length: ArrayLike,
    dynamic_viscosity: ArrayLike,
) -> ScalarOrArray:
    r"""Return :math:`Re = \rho U L / \mu`."""

    rho = _positive("density", density)
    velocity = _positive("speed", speed)
    scale = _positive("length", length)
    viscosity = _positive("dynamic_viscosity", dynamic_viscosity)
    return _scalar_or_array(lambda: rho * velocity * scale / viscosity)


def weber(
    density: ArrayLike,
    speed: ArrayLike,
    length: ArrayLike,
    surface_tension: ArrayLike,
) -> ScalarOrArray:
    r"""Return :math:`We = \rho U^2 L / \sigma`."""

    rho = _positive("density", density)
    velocity = _positive("speed", speed)
    scale = _positive("length", length)
    sigma = _positive("surface_tension", surface_tension)
    return _scalar_or_array(lambda: rho * velocity**2 * scale / sigma)


def ohnesorge(
    dynamic_viscosity: ArrayLike,
    density: ArrayLike,
    surface_tension: ArrayLike,
    length: ArrayLike,
) -> ScalarOrArray:
    r"""Return :math:`Oh = \mu/\sqrt{\rho\sigma L}`."""

    viscosity = _positive("dynamic_viscosity", dynamic_viscosity)
    rho = _positive("density", density)
    sigma = _positive("surface_tension", surface_tension)
    scale = _positive("length", length)
    return _scalar_or_array(
        lambda: viscosity / np.sqrt(rho * sigma * scale),
    )
