"""Starter: quantify a finite-difference convergence claim."""

from collections.abc import Sequence

import numpy as np
from numpy.typing import NDArray


def convergence_study(
    point_counts: Sequence[int],
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """Return spacings, maximum errors, and successive observed orders."""

    # TODO: compare the numerical derivative of sin(x) with cos(x).
    raise NotImplementedError
