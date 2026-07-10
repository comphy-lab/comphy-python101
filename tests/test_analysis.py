import numpy as np
import pytest

from comphy_python101 import central_difference, steady_state_index


def test_central_difference_is_exact_for_a_quadratic() -> None:
    x = np.linspace(-2.0, 2.0, 9)
    derivative = central_difference(x, x**2)
    np.testing.assert_allclose(derivative, 2 * x, atol=1e-12)


def test_central_difference_refuses_hidden_nonuniformity() -> None:
    with pytest.raises(ValueError, match="uniform"):
        central_difference([0.0, 0.5, 1.5], [0.0, 0.25, 2.25])


def test_steady_state_requires_a_whole_flat_window() -> None:
    values = [0.0, 1.0, 1.8, 2.0, 2.01, 1.99, 2.00]
    assert steady_state_index(values, window=4, relative_tolerance=0.02) == 6


def test_steady_state_can_be_absent() -> None:
    assert steady_state_index([1, 2, 3, 4], window=3) is None
