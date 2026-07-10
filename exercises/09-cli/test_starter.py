import json
from pathlib import Path

import pytest
from starter import main

ROOT = Path(__file__).parents[2]


def test_cli_accepts_absolute_input_from_another_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = (ROOT / "data" / "basilisk_log.csv").resolve()
    output = tmp_path / "nested" / "summary.json"
    monkeypatch.chdir(tmp_path)
    assert main([str(source), "--output", str(output)]) == 0
    assert json.loads(output.read_text(encoding="utf-8"))["samples"] == 16


def test_missing_input_fails(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        main([str(tmp_path / "missing.csv"), "--output", str(tmp_path / "out.json")])
