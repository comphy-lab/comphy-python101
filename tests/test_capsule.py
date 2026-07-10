from pathlib import Path

import pytest

from examples.reproduce_capsule import build_capsule, verify_capsule


def test_capsule_is_complete(tmp_path: Path) -> None:
    paths = build_capsule(tmp_path)
    assert {path.name for path in paths} == {
        "basilisk_log.csv",
        "log.png",
        "manifest.sha256",
        "regime-map.png",
        "regime_map.csv",
        "summary.json",
    }
    manifest = (tmp_path / "manifest.sha256").read_text(encoding="utf-8")
    assert len(manifest.splitlines()) == 5
    assert "data/basilisk_log.csv" in manifest
    assert "data/regime_map.csv" in manifest
    verify_capsule(tmp_path)


def test_capsule_verification_detects_tampering(tmp_path: Path) -> None:
    build_capsule(tmp_path)
    (tmp_path / "summary.json").write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum mismatch"):
        verify_capsule(tmp_path)


def test_capsule_verification_rejects_unsafe_paths(tmp_path: Path) -> None:
    (tmp_path / "manifest.sha256").write_text(
        f"{'0' * 64}  ../outside.txt\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="unsafe path"):
        verify_capsule(tmp_path)
