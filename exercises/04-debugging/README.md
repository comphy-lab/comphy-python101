# Exercise 04 — Debug the definition

## Frame

The starter claims to detect a steady plateau, but it examines only two
successive samples. A momentary pause can therefore pass.

## Predict

Create the smallest series that contains a false two-point plateau followed by
growth.

## Build

Repair `steady_state_index` so that it:

- checks a complete rolling window;
- accepts relative and absolute tolerances;
- returns the index ending the first accepted window;
- returns `None` when no plateau exists.

## Verify

```bash
uv run pytest exercises/04-debugging/test_starter.py
```

## Reflect

The bug is not a missing colon. The code implements the wrong idea faithfully.
