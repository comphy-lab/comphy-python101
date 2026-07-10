# Exercise 06 — Reduce without erasing provenance

## Frame

Count the outcomes in `data/regime_map.csv`, but retain the rule that every row
must have a known category and unique case identifier.

## Predict

Why is counting by marker colour from a rendered figure weaker than counting
from the table?

## Build

Complete `count_outcomes` in `starter.py`. Reject duplicate case IDs and unknown
outcomes.

## Verify

```bash
uv run pytest exercises/06-regime-map/test_starter.py
```

## Reflect

The figure is an argument. The table is the auditable evidence behind it.
