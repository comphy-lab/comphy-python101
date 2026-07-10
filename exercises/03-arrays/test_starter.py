import numpy as np
import pytest
from starter import central_difference


def test_quadratic() -> None:
    x = np.linspace(-2, 2, 9)
    result = central_difference(x, x**2)
    assert result.shape == x.shape
    np.testing.assert_allclose(result, 2 * x, atol=1e-12)


def test_nonuniform_grid_fails() -> None:
    with pytest.raises(ValueError, match="uniform"):
        central_difference([0, 1, 3], [0, 1, 9])
