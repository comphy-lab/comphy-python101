"""Worked solution for Exercise 02."""

from math import sqrt


def capillary_time(density: float, length: float, surface_tension: float) -> float:
    if density <= 0 or length <= 0 or surface_tension <= 0:
        raise ValueError("density, length, and surface tension must be positive")
    return sqrt(density * length**3 / surface_tension)
