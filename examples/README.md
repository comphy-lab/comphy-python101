# End-to-end examples

`reproduce_capsule.py` is the course's small reference pipeline:

```text
validated inputs → reduction → figures → checksums
```

Run it from the repository root:

```bash
make reproduce
```

The output directory contains:

- `data/` — copied, declared inputs used by this build;
- `summary.json` — reduced evidence from the log;
- `log.png` and `regime-map.png` — deterministic figures;
- `manifest.sha256` — checksums for every input and output.

It is deliberately small enough to read in one sitting. The capstone asks
students to make the same contract work for a new question.

`make reproduce` installs or verifies the locked environment, runs the test
suite, rebuilds the capsule from a clean output directory, writes the manifest,
and verifies every listed digest. To verify an existing capsule without
rewriting it:

```bash
uv run python examples/reproduce_capsule.py \
  --output build/capsule --verify-only
```
