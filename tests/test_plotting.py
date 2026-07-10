from pathlib import Path

import matplotlib.pyplot as plt

from comphy_python101 import load_basilisk_log, load_regime_map
from comphy_python101.plotting import _draw_regime_map, plot_log, plot_regime_map
from examples.build_site_figures import build_site_figures

ROOT = Path(__file__).parents[1]


def test_figures_are_written(tmp_path: Path) -> None:
    log_output = plot_log(
        load_basilisk_log(ROOT / "data" / "basilisk_log.csv"),
        tmp_path / "nested" / "log.png",
    )
    regime_output = plot_regime_map(
        load_regime_map(ROOT / "data" / "regime_map.csv"),
        tmp_path / "regime.png",
    )
    assert log_output.stat().st_size > 10_000
    assert regime_output.stat().st_size > 10_000


def test_site_figure_exemplars_are_rebuildable(tmp_path: Path) -> None:
    outputs = build_site_figures(tmp_path)
    assert {path.name for path in outputs} == {
        "basilisk-log.png",
        "central-difference-convergence.png",
        "regime-map.png",
    }
    assert all(path.stat().st_size > 10_000 for path in outputs)


def test_regime_legend_and_counts_ignore_row_order() -> None:
    cases = load_regime_map(ROOT / "data" / "regime_map.csv")
    expected_labels = {"no jet", "one drop", "multiple drops"}
    counts = []
    for ordered_cases in (cases, list(reversed(cases))):
        figure, axis = plt.subplots()
        _draw_regime_map(ordered_cases, axis)
        labels = {text.get_text() for text in axis.get_legend().get_texts()}
        assert labels == expected_labels
        counts.append(
            {
                collection.get_label(): len(collection.get_offsets())
                for collection in axis.collections
            }
        )
        plt.close(figure)
    assert (
        counts[0]
        == counts[1]
        == {
            "no jet": 7,
            "one drop": 9,
            "multiple drops": 4,
        }
    )
