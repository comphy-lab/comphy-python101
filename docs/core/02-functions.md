# 02 · Functions are scientific claims

A useful function says what enters, what leaves, and what must be true. Its body
is the proof attempt.

<div class="lesson-contract">
  <p><strong>Decision:</strong> is one scientific transformation explicit enough to test?</p>
  <p><strong>Output:</strong> a unit-consistent function with loud invalid states.</p>
</div>

## Frame

The inertio-capillary time is

$$
t_\sigma = \sqrt{\frac{\rho L^3}{\sigma}}.
$$

The arithmetic fits on one line. The scientific contract is larger:

- \(\rho\): positive density;
- \(L\): positive length scale;
- \(\sigma\): positive surface tension;
- output: a time;
- arrays may be useful for a sweep;
- zero, negative, or non-finite inputs are not physical for this formula.

## Predict

Before implementation:

- \(t_\sigma \propto L^{3/2}\);
- \(t_\sigma\) increases with density;
- \(t_\sigma\) decreases with surface tension;
- the units under the square root reduce to time squared.

These become tests.

## Build the boundary first

```python
def capillary_time(density, length, surface_tension):
    """Return sqrt(rho L^3 / sigma) for positive inputs."""
```

The parameter names carry more information than `a`, `b`, and `c`. The
docstring states the operation and the domain. The function should return a
value, not print one, because the caller may need to compare, plot, save, or
test it.

```python
from math import sqrt


def capillary_time(density, length, surface_tension):
    if density <= 0 or length <= 0 or surface_tension <= 0:
        raise ValueError("inputs must be strictly positive")
    return sqrt(density * length**3 / surface_tension)
```

An exception marks the boundary between “this model applies” and “the caller
gave an invalid state”. Returning `nan` would allow the error to travel into a
later plot.

## Parameters are choices

A function interface should expose choices that change meaning, not every local
detail.

```python
def steady_state_index(
    values,
    *,
    window=4,
    relative_tolerance=0.02,
):
    ...
```

The `*` makes policy arguments keyword-only:

```python
steady_state_index(energy, window=8, relative_tolerance=0.01)
```

That call is harder to misread than `steady_state_index(energy, 8, 0.01)`.

## Prefer one level of meaning

This function mixes levels:

```python
def analyse():
    path = "/Users/name/project/log.csv"
    rows = open(path).readlines()
    # parse, calculate, plot, save, print ...
```

A cleaner split is:

```python
log = load_log(path)
summary = summarise_log(log)
plot_log(log, output)
```

Now parsing can fail on a schema, reduction can be tested on arrays, and
plotting can change without changing the physics.

## Tests state claims

```python
def test_length_scaling():
    first = capillary_time(1000.0, 1e-3, 0.064)
    second = capillary_time(1000.0, 2e-3, 0.064)
    assert second / first == pytest.approx(2**1.5)
```

This test is stronger than repeating the same formula in the expected value. It
checks a scaling consequence.

Useful test families are:

- **known value** from a hand calculation;
- **limit or scaling** from the governing relation;
- **invalid domain** that must fail;
- **shape contract** for vector inputs;
- **regression** for a settled numerical result.

## A family of claims

The course reference package implements \(Re\), \(We\), \(Oh\), and
\(t_\sigma\) with two deliberately different validation policies:

```python
--8<-- "src/comphy_python101/dimensionless.py"
```

Read it for structure, not for cleverness. Density, length, surface tension,
and denominator viscosity must remain strictly positive. Speed in \(Re\) and
\(We\), and numerator viscosity in \(Oh\), may be zero: those are valid
zero-speed and inviscid limits. Negative or non-finite values still fail.

Notice that array support is a consequence of NumPy operations, while scalar
input still returns a scalar.

## Verify

Complete [Exercise 02](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/02-functions).
Do not begin
with the square root. Write the three prediction tests first, watch them fail,
then implement.

## Reflect

Could a reader use your function correctly without reading its body? Could a
test disprove its scientific claim? If either answer is no, improve the
boundary.
