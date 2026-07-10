"""Starter: reduce a validated log to derivative evidence."""

from pathlib import Path

import numpy as np
from numpy.typing import ArrayLike, NDArray


def differentiate_minimum_length(
    time: ArrayLike, minimum_length: ArrayLike
) -> NDArray[np.float64]:
    del time, minimum_length
    # TODO: return a shape-preserving derivative with a visible grid contract.
    raise NotImplementedError


def write_reduced_log(source: Path, output: Path) -> Path:
    del source, output
    # TODO: validate the log and write t,h_min,dh_min_dt.
    raise NotImplementedError
