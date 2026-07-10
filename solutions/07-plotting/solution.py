"""Worked solution for Exercise 07."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import ArrayLike


def plot_series(time: ArrayLike, values: ArrayLike, output: Path) -> Path:
    coordinate = np.asarray(time, dtype=float)
    observable = np.asarray(values, dtype=float)
    if coordinate.ndim != 1 or observable.ndim != 1:
        raise ValueError("time and values must be one-dimensional")
    if coordinate.size != observable.size:
        raise ValueError("time and values must have the same length")
    if not np.all(np.isfinite(coordinate)) or not np.all(np.isfinite(observable)):
        raise ValueError("time and values must be finite")

    output.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(5.2, 3.4))
    axis.plot(coordinate, observable, color="#0b5d5b", linewidth=2)
    axis.set_xlabel("time")
    axis.set_ylabel("observable")
    figure.tight_layout()
    figure.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(figure)
    return output
