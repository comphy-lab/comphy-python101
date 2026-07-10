import json
from pathlib import Path

import pytest
from starter import build_evidence

ROOT = Path(__file__).parents[2]


def test_log_becomes_summary_and_figure(tmp_path: Path) -> None:
    summary, figure = build_evidence(ROOT / "data" / "basilisk_log.csv", tmp_path)
    assert json.loads(summary.read_text(encoding="utf-8"))["samples"] == 16
    assert figure.stat().st_size > 10_000


def test_negative_energy_fails_before_outputs(tmp_path: Path) -> None:
    source = tmp_path / "invalid.csv"
    source.write_text(
        "t,dt,kinetic_energy,h_min\n0,0.1,-1,0.2\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="kinetic_energy"):
        build_evidence(source, tmp_path / "out")
    assert not (tmp_path / "out").exists()
