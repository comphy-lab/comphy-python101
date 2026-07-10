import pytest
from starter import capillary_time


def test_known_value() -> None:
    assert capillary_time(1000.0, 0.001, 0.064) == pytest.approx(0.003952847)


def test_length_scaling() -> None:
    first = capillary_time(1000.0, 0.001, 0.064)
    second = capillary_time(1000.0, 0.002, 0.064)
    assert second / first == pytest.approx(2**1.5)


@pytest.mark.parametrize("values", [(0, 1, 1), (1, -1, 1), (1, 1, 0)])
def test_nonphysical_values_fail(values: tuple[float, float, float]) -> None:
    with pytest.raises(ValueError):
        capillary_time(*values)
