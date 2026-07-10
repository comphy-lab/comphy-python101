import json
from pathlib import Path

from comphy_python101.cli import main

ROOT = Path(__file__).parents[1]


def test_summary_command_prints_machine_readable_evidence(capsys) -> None:
    result = main(["summary", str(ROOT / "data" / "basilisk_log.csv")])
    captured = json.loads(capsys.readouterr().out)
    assert result == 0
    assert captured["samples"] == 16
