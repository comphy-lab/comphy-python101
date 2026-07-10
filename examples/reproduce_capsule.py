"""Build the complete synthetic reproduction capsule."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from comphy_python101 import load_basilisk_log, load_regime_map, summarise_log
from comphy_python101.plotting import plot_log, plot_regime_map

ROOT = Path(__file__).parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_capsule(output: Path) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    data_output = output / "data"
    data_output.mkdir(exist_ok=True)
    log_source = data_output / "basilisk_log.csv"
    regime_source = data_output / "regime_map.csv"
    shutil.copy2(ROOT / "data" / "basilisk_log.csv", log_source)
    shutil.copy2(ROOT / "data" / "regime_map.csv", regime_source)

    log = load_basilisk_log(log_source)
    cases = load_regime_map(regime_source)

    summary_path = output / "summary.json"
    summary_path.write_text(
        json.dumps(summarise_log(log), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    log_figure = plot_log(log, output / "log.png")
    regime_figure = plot_regime_map(cases, output / "regime-map.png")

    tracked = [log_source, regime_source, summary_path, log_figure, regime_figure]
    manifest = output / "manifest.sha256"
    manifest.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(output)}\n" for path in tracked),
        encoding="utf-8",
    )
    return [*tracked, manifest]


def verify_capsule(output: Path) -> None:
    """Verify every declared capsule file against its SHA-256 digest."""

    manifest = output / "manifest.sha256"
    if not manifest.is_file():
        raise FileNotFoundError(manifest)
    lines = manifest.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError("manifest contains no entries")
    for line_number, line in enumerate(lines, start=1):
        try:
            expected, relative_text = line.split("  ", maxsplit=1)
        except ValueError as error:
            raise ValueError(f"manifest line {line_number} is malformed") from error
        relative = Path(relative_text)
        if len(expected) != 64 or any(
            character not in "0123456789abcdef" for character in expected
        ):
            raise ValueError(f"manifest line {line_number} has an invalid digest")
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"manifest line {line_number} has an unsafe path")
        path = output / relative
        if not path.is_file():
            raise ValueError(f"manifest file is missing: {relative}")
        if sha256(path) != expected:
            raise ValueError(f"checksum mismatch: {relative}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("build/capsule"))
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    output = args.output.resolve()
    if not args.verify_only:
        for path in build_capsule(output):
            print(path)
    verify_capsule(output)
    print(f"verified {output / 'manifest.sha256'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
