import json
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
    assert function(ROOT / "data" / "regime_map.csv") == {
        "multiple-drops": 4,
        "no-jet": 7,
        "one-drop": 9,
    }


def test_plotting_solution(tmp_path: Path) -> None:
    function = solution("07-plotting")["plot_series"]
    time = np.linspace(0.0, 1.0, 8)
    output = function(time, np.exp(-time), tmp_path / "plot.png")
    assert output.stat().st_size > 5_000


def test_numerics_solution() -> None:
    function = solution("08-numerics")["convergence_study"]
    _, errors, orders = function([20, 40, 80, 160])
    assert np.all(np.diff(errors) < 0)
    assert orders[-1] == pytest.approx(2.0, abs=0.08)


def test_cli_solution(tmp_path: Path) -> None:
    function = solution("09-cli")["main"]
    output = tmp_path / "nested" / "summary.json"
    assert (
        function([str(ROOT / "data" / "basilisk_log.csv"), "--output", str(output)])
        == 0
    )
    assert json.loads(output.read_text(encoding="utf-8"))["samples"] == 16


def test_reproducibility_solution(tmp_path: Path) -> None:
    functions = solution("10-reproducibility")
    output = tmp_path / "result.txt"
    output.write_text("evidence\n", encoding="utf-8")
    functions["write_manifest"](tmp_path, [output])
    functions["verify_manifest"](tmp_path)
    output.write_text("changed\n", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        functions["verify_manifest"](tmp_path)


def test_basilisk_log_solution(tmp_path: Path) -> None:
    function = solution("11-basilisk-log")["build_evidence"]
    summary, figure = function(ROOT / "data" / "basilisk_log.csv", tmp_path)
    assert json.loads(summary.read_text(encoding="utf-8"))["samples"] == 16
    assert figure.stat().st_size > 10_000


def test_log_to_evidence_solution(tmp_path: Path) -> None:
    functions = solution("12-log-to-evidence")
    time = np.linspace(-1.0, 1.0, 9)
    np.testing.assert_allclose(
        functions["differentiate_minimum_length"](time, time**2),
        2 * time,
        atol=1e-12,
    )
    output = functions["write_reduced_log"](
        ROOT / "data" / "basilisk_log.csv", tmp_path / "reduced.csv"
    )
    assert len(output.read_text(encoding="utf-8").splitlines()) == 17


def test_evidence_to_capsule_solution(tmp_path: Path) -> None:
    function = solution("13-evidence-to-capsule")["reproduce"]
    paths = function(tmp_path)
    assert {path.name for path in paths} >= {
        "summary.json",
        "log.png",
        "regime-map.png",
        "manifest.sha256",
    }
