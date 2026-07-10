# Integration lab 13 — Evidence to capsule

## Frame

Build the complete miniature capsule, verify its manifest, and prove that a
changed output fails verification.

## Predict

Which artefacts must be rebuilt, and which files belong in the integrity
manifest?

## Build

Complete `reproduce` in `starter.py` by composing the course capsule builder and
verifier. Do not duplicate their scientific logic.

## Verify

```bash
uv run pytest exercises/13-evidence-to-capsule/test_starter.py
```

## Reflect

One-command reproduction is valuable because the sequence is declared and
failure is observable, not because `make` or Python is magical.
