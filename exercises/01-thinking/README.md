# Exercise 01 — Think before Python

## Frame

A simulation log contains time, time step, kinetic energy, and minimum neck
radius. Someone asks: “When does the run become steady?”

That sentence is not yet an algorithm.

## Predict

Write down:

1. the input shape and units;
2. what “steady” means numerically;
3. how long it must remain steady;
4. what should happen if it never becomes steady;
5. one series that would fool a weak definition.

## Build

Trace this candidate by hand:

```python
values = [0.0, 1.0, 1.8, 2.0, 2.01, 1.99, 2.00]
window = 4
tolerance = 0.02
```

For every four-value window, calculate its span and compare it with two per cent
of the largest magnitude in that window.

## Verify

Invent a series with a short false plateau followed by renewed growth. A correct
algorithm must not accept fewer samples than the promised window.

## Reflect

Which choices are physics, which are numerical policy, and which are merely
Python?
