# Integration lab 12 · Log to evidence

This lab joins lessons 03, 06, 08, and 11 without introducing a new abstraction.

## Frame

The synthetic Basilisk log contains time and minimum-length columns. Produce a
reduced table with:

```text
t,h_min,dh_min_dt
```

## Predict

- Is the time grid uniform?
- What sign should \(dh_{\min}/dt\) usually have?
- Which analytic function can test the derivative independently of the log?

## Build

Complete
[`exercises/12-log-to-evidence`](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/12-log-to-evidence).
Keep derivative computation separate from CSV writing.

## Verify

```bash
uv run pytest exercises/12-log-to-evidence/test_starter.py
```

The tests require exact differentiation of a quadratic and a named reduced
schema with one output row per input sample.

## Reflect

State which assumption belongs to the input schema and which belongs to the
finite-difference algorithm. They should not be hidden in the same error.
