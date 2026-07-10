"""Starter with an intentional conceptual bug."""

from collections.abc import Sequence


def steady_state_index(
    values: Sequence[float],
    *,
    window: int = 4,
    relative_tolerance: float = 0.02,
    absolute_tolerance: float = 0.0,
) -> int | None:
    del absolute_tolerance
    del window
    for index in range(1, len(values)):
        change = abs(values[index] - values[index - 1])
        if change <= relative_tolerance * abs(values[index]):
            return index
    return None
