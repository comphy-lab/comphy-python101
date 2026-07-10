from pathlib import Path

import pytest
from starter import verify_manifest, write_manifest


def test_manifest_verifies_then_detects_tampering(tmp_path: Path) -> None:
    output = tmp_path / "result.txt"
    output.write_text("settled result\n", encoding="utf-8")
    manifest = write_manifest(tmp_path, [output])
    assert manifest.name == "manifest.sha256"
    verify_manifest(tmp_path)
    output.write_text("changed result\n", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        verify_manifest(tmp_path)
