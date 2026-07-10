# Exercise 03 — Shapes before values

## Frame

Estimate \(dy/dx\) on a uniformly spaced grid without changing the number or
order of samples.

## Predict

For \(y=x^2\), write the exact derivative. Mark which samples have neighbours
on both sides and which need a one-sided rule.

## Build

Implement the three regions in `starter.py`: left boundary, interior, right
boundary. Reject mismatched, short, or non-uniform inputs.

## Verify

```bash
uv run pytest exercises/03-arrays/test_starter.py
```

## Reflect

Vectorisation did not remove the algorithm. It made the algorithm visible as
array regions.
