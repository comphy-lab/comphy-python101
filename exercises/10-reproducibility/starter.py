"""Starter: write and verify a small checksum manifest."""

from collections.abc import Sequence
from pathlib import Path


def write_manifest(root: Path, paths: Sequence[Path]) -> Path:
    del root, paths
    # TODO: hash each file and write paths relative to root.
    raise NotImplementedError


def verify_manifest(root: Path) -> None:
    del root
    # TODO: recompute every listed digest and fail on any mismatch.
    raise NotImplementedError
