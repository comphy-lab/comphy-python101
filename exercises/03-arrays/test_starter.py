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


@pytest.mark.parametrize(
    ("x", "y", "message"),
    [
        ([0, 1, 2], [0, 1], "same length"),
        ([0, 1], [0, 1], "at least three"),
    ],
)
def test_shape_contract_fails_loudly(x, y, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        central_difference(x, y)
