"""Build the complete synthetic reproduction capsule."""

from __future__ import annotations

import argparse
import hashlib
import json
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


def manifest_name(path: Path, output: Path) -> Path:
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return Path(output.name) / path.relative_to(output)


def build_capsule(output: Path) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    log_source = ROOT / "data" / "basilisk_log.csv"
    regime_source = ROOT / "data" / "regime_map.csv"

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
        "".join(f"{sha256(path)}  {manifest_name(path, output)}\n" for path in tracked),
        encoding="utf-8",
    )
    return [*tracked, manifest]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("build/capsule"))
    args = parser.parse_args()
    for path in build_capsule(args.output.resolve()):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
