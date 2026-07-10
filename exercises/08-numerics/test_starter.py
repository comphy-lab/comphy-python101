import numpy as np
import pytest
from starter import convergence_study


def test_second_order_convergence() -> None:
    spacing, error, order = convergence_study([20, 40, 80, 160])
    assert spacing.shape == error.shape == (4,)
    assert order.shape == (3,)
    assert np.all(np.diff(error) < 0)
    assert order[-1] == pytest.approx(2.0, abs=0.08)


def test_short_grid_fails() -> None:
    with pytest.raises(ValueError, match="three"):
        convergence_study([2, 4])
