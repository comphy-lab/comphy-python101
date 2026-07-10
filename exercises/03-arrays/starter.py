"""Starter: a shape-preserving finite difference."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def central_difference(x: ArrayLike, y: ArrayLike) -> NDArray[np.float64]:
    """Differentiate y(x) on a uniform grid without changing its shape."""

    _coordinate = np.asarray(x, dtype=float)
    _values = np.asarray(y, dtype=float)
    # TODO: validate the arrays, then fill a derivative array.
    raise NotImplementedError
