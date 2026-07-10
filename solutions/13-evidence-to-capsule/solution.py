"""Worked solution for Integration lab 13."""

from pathlib import Path

from examples.reproduce_capsule import build_capsule, verify_capsule


def reproduce(output: Path) -> list[Path]:
    paths = build_capsule(output)
    verify_capsule(output)
    return paths
