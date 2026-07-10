# Exercise 02 — A function is a scientific claim

## Frame

Implement the inertio-capillary time

$$
t_\sigma = \sqrt{\frac{\rho L^3}{\sigma}}.
$$

The function must reject non-physical inputs rather than return a mysterious
`nan`.

## Predict

- If \(L\) doubles, by what factor should \(t_\sigma\) change?
- What units remain inside the square root?
- Which inputs must be strictly positive?

## Build

Edit `starter.py`. Keep the interface fixed.

## Verify

```bash
uv run pytest exercises/02-functions/test_starter.py
```

## Reflect

The square root is easy. The valuable part is the contract around it.
