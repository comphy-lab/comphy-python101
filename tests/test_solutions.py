import runpy
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).parents[1]


def solution(number: str) -> dict:
    path = next((ROOT / "solutions" / number).glob("solution.py"))
    return runpy.run_path(str(path))


def test_function_solution() -> None:
    function = solution("02-functions")["capillary_time"]
    assert function(1000.0, 0.001, 0.064) == pytest.approx(0.003952847)


def test_array_solution() -> None:
    function = solution("03-arrays")["central_difference"]
    x = np.linspace(-1, 1, 5)
    np.testing.assert_allclose(function(x, x**2), 2 * x)


def test_debugging_solution() -> None:
    function = solution("04-debugging")["steady_state_index"]
    assert function([0, 1, 1.8, 2, 2.01, 1.99, 2], window=4) == 6


def test_file_solution() -> None:
    function = solution("05-files")["summarise_log"]
    assert function(ROOT / "data" / "basilisk_log.csv")["samples"] == 16


def test_regime_solution() -> None:
    function = solution("06-regime-map")["count_outcomes"]
    assert sum(function(ROOT / "data" / "regime_map.csv").values()) == 20
