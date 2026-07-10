from pathlib import Path

from comphy_python101 import load_basilisk_log, load_regime_map
from comphy_python101.plotting import plot_log, plot_regime_map

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
