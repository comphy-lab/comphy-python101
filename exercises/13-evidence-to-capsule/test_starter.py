from pathlib import Path

import pytest
from starter import reproduce

from examples.reproduce_capsule import verify_capsule


def test_capsule_rebuilds_and_verifies(tmp_path: Path) -> None:
    paths = reproduce(tmp_path)
    assert {path.name for path in paths} >= {
        "summary.json",
        "log.png",
        "regime-map.png",
        "manifest.sha256",
    }
    verify_capsule(tmp_path)


def test_changed_output_fails_verification(tmp_path: Path) -> None:
    reproduce(tmp_path)
    (tmp_path / "summary.json").write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        verify_capsule(tmp_path)
