# Exercise 07 — Plot the claim

## Frame

Build a deterministic time-series figure without changing the source arrays.

## Predict

Which axis carries time, which label states the observable, and what should
happen if the arrays do not align?

## Build

Complete `plot_series` in `starter.py`. Validate one-dimensional, aligned data;
label both axes; create parent directories; save and close the figure.

## Verify

```bash
uv run pytest exercises/07-plotting/test_starter.py
```

## Reflect

The output file is evidence only because its data and visual choices remain
inspectable.
