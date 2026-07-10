from pathlib import Path

import numpy as np
import pytest
from starter import plot_series


def test_figure_is_written_without_mutating_inputs(tmp_path: Path) -> None:
    time = np.linspace(0.0, 1.0, 8)
    values = np.exp(-time)
    original = values.copy()
    output = plot_series(time, values, tmp_path / "nested" / "series.png")
    assert output.stat().st_size > 5_000
    np.testing.assert_array_equal(values, original)


def test_mismatched_arrays_fail(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="same length"):
        plot_series([0, 1], [1], tmp_path / "bad.png")
