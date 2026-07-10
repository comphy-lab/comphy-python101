# Exercise 11 — Join schema, reduction, and figure

## Frame

Turn the synthetic Basilisk log into one JSON summary and one deterministic
figure.

## Predict

Which invalid row must stop the pipeline before either output is written?

## Build

Complete `build_evidence` in `starter.py` by composing the reference reader,
reduction, and plotting function.

## Verify

```bash
uv run pytest exercises/11-basilisk-log/test_starter.py
```

## Reflect

Composition is trustworthy only when each boundary keeps its own contract.
