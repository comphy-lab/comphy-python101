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


@pytest.mark.parametrize("contents", ["", "t,dt,kinetic_energy,h_min\n"])
def test_reader_rejects_empty_input(tmp_path: Path, contents: str) -> None:
    invalid = tmp_path / "empty.csv"
    invalid.write_text(contents, encoding="utf-8")
    with pytest.raises(ValueError, match="no header|no data rows"):
        load_basilisk_log(invalid)


def test_regime_map_rejects_duplicate_case_ids(tmp_path: Path) -> None:
    invalid = tmp_path / "duplicate.csv"
    invalid.write_text(
        "case_id,ohnesorge,bond,outcome\nc1,0.1,0.2,no-jet\nc1,0.2,0.3,one-drop\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate case ID"):
        load_regime_map(invalid)


@pytest.mark.parametrize(
    ("ohnesorge", "outcome", "message"),
    [("0", "no-jet", "strictly positive"), ("0.1", "perhaps", "unknown outcome")],
)
def test_regime_map_rejects_invalid_cases(
    tmp_path: Path, ohnesorge: str, outcome: str, message: str
) -> None:
    invalid = tmp_path / "invalid-case.csv"
    invalid.write_text(
        f"case_id,ohnesorge,bond,outcome\nc1,{ohnesorge},0.2,{outcome}\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match=message):
        load_regime_map(invalid)


@pytest.mark.parametrize("value", ["nan", "inf"])
def test_regime_map_rejects_nonfinite_values(tmp_path: Path, value: str) -> None:
    invalid = tmp_path / "nonfinite.csv"
    invalid.write_text(
        f"case_id,ohnesorge,bond,outcome\nc1,{value},0.2,no-jet\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="finite"):
        load_regime_map(invalid)
