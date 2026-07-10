"""Generate the scientific figure exemplars embedded in the course website."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from comphy_python101 import central_difference, load_basilisk_log, load_regime_map
from comphy_python101.plotting import BLUE, CORAL, plot_log, plot_regime_map

ROOT = Path(__file__).parents[1]


def build_site_figures(output: Path) -> list[Path]:
    """Build all site figures from declared synthetic inputs."""

    output.mkdir(parents=True, exist_ok=True)
    log_figure = plot_log(
        load_basilisk_log(ROOT / "data" / "basilisk_log.csv"),
        output / "basilisk-log.png",
    )
    regime_figure = plot_regime_map(
        load_regime_map(ROOT / "data" / "regime_map.csv"),
        output / "regime-map.png",
    )

    point_counts = [20, 40, 80, 160]
    spacing: list[float] = []
    error: list[float] = []
    for count in point_counts:
        coordinate = np.linspace(0.0, 2 * np.pi, count)
        derivative = central_difference(coordinate, np.sin(coordinate))
        spacing.append(float(coordinate[1] - coordinate[0]))
        error.append(float(np.max(np.abs(derivative - np.cos(coordinate)))))

    convergence_figure = output / "central-difference-convergence.png"
    figure, axis = plt.subplots(figsize=(6.4, 4.4))
    axis.loglog(spacing, error, "o-", color=BLUE, linewidth=2, label="measured error")
    reference = error[-1] * (np.asarray(spacing) / spacing[-1]) ** 2
    axis.loglog(spacing, reference, "--", color=CORAL, label=r"$\Delta x^2$")
    axis.set_xlabel(r"grid spacing, $\Delta x$")
    axis.set_ylabel("maximum derivative error")
    axis.spines[["top", "right"]].set_visible(False)
    axis.grid(which="both", alpha=0.2, linewidth=0.6)
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(convergence_figure, dpi=180, bbox_inches="tight")
    plt.close(figure)
    return [log_figure, regime_figure, convergence_figure]


if __name__ == "__main__":
    for path in build_site_figures(ROOT / "docs" / "assets" / "figures"):
        print(path)
