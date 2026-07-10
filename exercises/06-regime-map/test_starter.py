from pathlib import Path

import pytest
from starter import count_outcomes

ROOT = Path(__file__).parents[2]


def test_counts() -> None:
    assert count_outcomes(ROOT / "data" / "regime_map.csv") == {
        "no-jet": 8,
        "one-drop": 8,
        "multiple-drops": 4,
    }


def test_unknown_outcome_fails(tmp_path: Path) -> None:
    path = tmp_path / "unknown.csv"
    path.write_text(
        "case_id,ohnesorge,bond,outcome\nc1,0.1,0.1,perhaps\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="unknown"):
        count_outcomes(path)
