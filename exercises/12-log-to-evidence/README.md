# Integration lab 12 — Log to reduced evidence

## Frame

Join validated input, a declared finite-difference rule, and a reduced CSV.

## Predict

What grid assumption does the derivative make, and which columns must the
reduced file preserve?

## Build

Complete `differentiate_minimum_length` and `write_reduced_log` in `starter.py`.
Keep computation separate from file writing.

## Verify

```bash
uv run pytest exercises/12-log-to-evidence/test_starter.py
```

## Reflect

The reduced table is useful because another analysis can inspect or replace the
numerical policy without reading the raw log again.
