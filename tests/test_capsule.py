from pathlib import Path

from examples.reproduce_capsule import build_capsule


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
