from pathlib import Path

import pytest
from starter import summarise_log

ROOT = Path(__file__).parents[2]


def test_teaching_log() -> None:
    result = summarise_log(ROOT / "data" / "basilisk_log.csv")
    assert result == {
        "samples": 16,
        "final_time": pytest.approx(0.75),
        "peak_kinetic_energy": pytest.approx(0.194),
        "minimum_length": pytest.approx(0.073),
    }


def test_missing_column_fails(tmp_path: Path) -> None:
    path = tmp_path / "broken.csv"
    path.write_text("t,dt\n0,0.1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing"):
        summarise_log(path)


@pytest.mark.parametrize("contents", ["", "t,dt,kinetic_energy,h_min\n"])
def test_empty_input_fails(tmp_path: Path, contents: str) -> None:
    path = tmp_path / "empty.csv"
    path.write_text(contents, encoding="utf-8")
    with pytest.raises(ValueError, match="empty|header|data"):
        summarise_log(path)
