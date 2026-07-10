import numpy as np
import pytest

from comphy_python101 import capillary_time, ohnesorge, reynolds, weber


def test_dimensionless_numbers_match_definitions() -> None:
    rho = 1000.0
    speed = 2.0
    length = 0.001
    sigma = 0.072
    viscosity = 0.001

    assert reynolds(rho, speed, length, viscosity) == pytest.approx(2000.0)
    assert weber(rho, speed, length, sigma) == pytest.approx(55.5555556)
    assert ohnesorge(viscosity, rho, sigma, length) == pytest.approx(
        viscosity / np.sqrt(rho * sigma * length),
    )
    assert capillary_time(rho, length, sigma) == pytest.approx(
        np.sqrt(rho * length**3 / sigma),
    )


def test_array_inputs_broadcast() -> None:
    lengths = np.array([1e-3, 2e-3, 4e-3])
    values = capillary_time(1000.0, lengths, 0.072)
    assert isinstance(values, np.ndarray)
    assert values.shape == lengths.shape
    assert np.all(np.diff(values) > 0)


def test_zero_numerator_limits_are_valid() -> None:
    assert reynolds(1000.0, 0.0, 0.001, 0.001) == 0.0
    assert weber(1000.0, 0.0, 0.001, 0.072) == 0.0
    assert ohnesorge(0.0, 1000.0, 0.072, 0.001) == 0.0


@pytest.mark.parametrize(
    ("function", "arguments"),
    [
        (reynolds, (1000.0, -1.0, 0.001, 0.001)),
        (weber, (1000.0, -1.0, 0.001, 0.072)),
        (ohnesorge, (-0.001, 1000.0, 0.072, 0.001)),
    ],
)
def test_negative_numerators_fail(function, arguments: tuple[float, ...]) -> None:
    with pytest.raises(ValueError):
        function(*arguments)


@pytest.mark.parametrize("invalid", [0.0, -1.0, np.nan, np.inf])
def test_nonphysical_inputs_fail_loudly(invalid: float) -> None:
    with pytest.raises(ValueError):
        ohnesorge(0.001, 1000.0, 0.072, invalid)
