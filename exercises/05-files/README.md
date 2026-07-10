# Exercise 05 — Data has a schema

## Frame

Read `data/basilisk_log.csv` and return its sample count, final time, peak
kinetic energy, and minimum length.

## Predict

List the assumptions a naive `np.loadtxt` call would silently make. Decide which
ones should produce a clear error.

## Build

Complete `summarise_log` in `starter.py`. Use the header names, not column
numbers. Reject a missing column or an empty file.

## Verify

```bash
uv run pytest exercises/05-files/test_starter.py
```

## Reflect

A schema is part of the scientific method: it records what a number means
before anyone plots it.
