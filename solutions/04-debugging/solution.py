"""Worked solution for Exercise 04."""

from collections.abc import Sequence


def steady_state_index(
    values: Sequence[float],
    *,
    window: int = 4,
    relative_tolerance: float = 0.02,
    absolute_tolerance: float = 0.0,
) -> int | None:
    if window < 2 or len(values) < window:
        raise ValueError("a complete window of at least two values is required")
    for stop in range(window, len(values) + 1):
        sample = values[stop - window : stop]
        span = max(sample) - min(sample)
        scale = max(max(abs(value) for value in sample), 1e-300)
        if span <= absolute_tolerance + relative_tolerance * scale:
            return stop - 1
    return None
