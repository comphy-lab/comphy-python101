"""Worked solution for Exercise 10."""

import hashlib
from collections.abc import Sequence
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest(root: Path, paths: Sequence[Path]) -> Path:
    manifest = root / "manifest.sha256"
    lines = [f"{_sha256(path)}  {path.relative_to(root)}\n" for path in paths]
    manifest.write_text("".join(lines), encoding="utf-8")
    return manifest


def verify_manifest(root: Path) -> None:
    manifest = root / "manifest.sha256"
    for line in manifest.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", maxsplit=1)
        if _sha256(root / relative) != expected:
            raise ValueError(f"checksum mismatch: {relative}")
