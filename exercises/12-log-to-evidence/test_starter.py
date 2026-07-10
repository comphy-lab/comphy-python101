import csv
from pathlib import Path

import numpy as np
from starter import differentiate_minimum_length, write_reduced_log

ROOT = Path(__file__).parents[2]


def test_derivative_is_exact_for_a_quadratic() -> None:
    time = np.linspace(-1.0, 1.0, 9)
    np.testing.assert_allclose(
        differentiate_minimum_length(time, time**2), 2 * time, atol=1e-12
    )


def test_reduced_log_has_named_columns(tmp_path: Path) -> None:
    output = write_reduced_log(
        ROOT / "data" / "basilisk_log.csv", tmp_path / "nested" / "reduced.csv"
    )
    with output.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert rows[0].keys() == {"t", "h_min", "dh_min_dt"}
    assert len(rows) == 16
