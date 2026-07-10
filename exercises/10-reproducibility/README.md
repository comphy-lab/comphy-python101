# Exercise 10 — Detect change

## Frame

Write and verify a SHA-256 manifest for declared outputs.

## Predict

What can a checksum establish, and what provenance question can it not answer?

## Build

Complete `write_manifest` and `verify_manifest` in `starter.py`. Store paths
relative to one root and reject missing, malformed, or changed files.

## Verify

```bash
uv run pytest exercises/10-reproducibility/test_starter.py
```

## Reflect

Integrity says the bytes are unchanged. Provenance says what those bytes mean.
