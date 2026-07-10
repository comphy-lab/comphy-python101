from pathlib import Path

import pytest

from comphy_python101 import load_basilisk_log, load_regime_map, summarise_log

ROOT = Path(__file__).parents[1]


def test_teaching_log_schema_and_summary() -> None:
    log = load_basilisk_log(ROOT / "data" / "basilisk_log.csv")
    summary = summarise_log(log)
    assert summary["samples"] == 16
    assert summary["final_time"] == pytest.approx(0.75)
    assert summary["peak_kinetic_energy"] == pytest.approx(0.194)
    assert summary["minimum_length"] == pytest.approx(0.073)


def test_regime_map_has_all_outcomes() -> None:
    cases = load_regime_map(ROOT / "data" / "regime_map.csv")
    assert len(cases) == 20
    assert {case.outcome for case in cases} == {
        "multiple-drops",
        "no-jet",
        "one-drop",
    }


def test_reader_names_a_missing_column(tmp_path: Path) -> None:
    invalid = tmp_path / "invalid.csv"
    invalid.write_text("t,dt\n0,0.1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="h_min"):
        load_basilisk_log(invalid)
