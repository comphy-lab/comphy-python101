# Exercise 08 — Measure convergence

## Frame

Test the centred-difference implementation against the analytic derivative of
\(\sin x\).

## Predict

If the spacing halves, by what factor should a second-order error fall?

## Build

Complete `convergence_study` in `starter.py`. Return spacings, maximum errors,
and observed orders for the requested grid sizes.

## Verify

```bash
uv run pytest exercises/08-numerics/test_starter.py
```

## Reflect

A convergence rate tests an implementation claim; it does not validate the
physical model.
