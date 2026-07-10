"""Deterministic figures for the teaching workflows."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from .io import RegimeCase, SimulationLog

INK = "#13201f"
TEAL = "#0b5d5b"
BLUE = "#2f6f9f"
CORAL = "#e45d3f"
GOLD = "#c3912c"


def _output_path(path: str | Path) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    return output


def plot_log(log: SimulationLog, output: str | Path) -> Path:
    """Save a two-panel time-series figure from a validated log."""

    destination = _output_path(output)
    figure, axes = plt.subplots(2, 1, figsize=(6.4, 5.4), sharex=True)

    axes[0].plot(log.time, log.kinetic_energy, color=TEAL, linewidth=2)
    axes[0].set_ylabel("kinetic energy")
    axes[0].set_yscale("log")

    axes[1].plot(log.time, log.minimum_length, color=CORAL, linewidth=2)
    axes[1].set_xlabel("time")
    axes[1].set_ylabel(r"$h_{\min}$")
    axes[1].set_yscale("log")

    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(alpha=0.2, linewidth=0.6)

    figure.suptitle("Synthetic Basilisk log", color=INK)
    figure.tight_layout()
    figure.savefig(destination, dpi=180, bbox_inches="tight")
    plt.close(figure)
    return destination


def _draw_regime_map(cases: list[RegimeCase], axis: Axes) -> None:
    """Draw validated categorical cases on an existing axis."""

    if not cases:
        raise ValueError("at least one case is required")
    styles = {
        "no-jet": ("x", BLUE),
        "one-drop": ("o", GOLD),
        "multiple-drops": ("^", CORAL),
    }

    for outcome, (marker, colour) in styles.items():
        selected = [case for case in cases if case.outcome == outcome]
        if not selected:
            continue
        axis.scatter(
            [case.ohnesorge for case in selected],
            [case.bond for case in selected],
            marker=marker,
            color=colour,
            label=outcome.replace("-", " "),
            s=58,
            linewidths=1.4,
        )

    axis.set_xscale("log")
    axis.set_yscale("log")
    axis.set_xlabel(r"Ohnesorge number, $Oh$")
    axis.set_ylabel(r"Bond number, $Bo$")
    axis.spines[["top", "right"]].set_visible(False)
    axis.grid(which="both", alpha=0.18, linewidth=0.6)
    axis.legend(frameon=False, title="observed outcome")


def plot_regime_map(cases: list[RegimeCase], output: str | Path) -> Path:
    """Save a labelled Oh–Bo regime map."""

    destination = _output_path(output)
    figure, axis = plt.subplots(figsize=(6.4, 4.8))
    _draw_regime_map(cases, axis)
    figure.tight_layout()
    figure.savefig(destination, dpi=180, bbox_inches="tight")
    plt.close(figure)
    return destination
