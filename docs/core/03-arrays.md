# 03 · Arrays are the working language

Scientific Python becomes useful when you stop treating an array as “many
numbers” and start treating its shape as part of the model.

<div class="lesson-contract">
  <p><strong>Decision:</strong> does each axis retain a declared physical meaning?</p>
  <p><strong>Output:</strong> a vectorised, shape-preserving numerical transformation.</p>
</div>

## Frame

A time series may have shape `(500,)`. A field sampled on a grid might have
shape `(256, 128)`. A parameter sweep can have shape `(n_oh, n_bo, n_time)`.

Those axes are not interchangeable.

```python
energy.shape
time.shape
field.shape
```

Check shapes before values when an operation surprises you.

## Predict

For

```python
time = np.linspace(0.0, 1.0, 6)
height = time**2
```

predict:

- each shape;
- the first and last value;
- the exact derivative;
- which samples have neighbours on both sides.

Then run it.

## Indexing answers a question

```python
late = time > 0.5
late_energy = energy[late]
```

The Boolean array `late` has the same shape as `time`. It represents a
predicate for every sample. Applying it to a different-length array is a model
error, not merely an indexing inconvenience.

Slices preserve order:

```python
interior = height[1:-1]
left = height[:-2]
right = height[2:]
```

These three arrays have the same shape. That alignment is the basis of a
centred difference:

```python
derivative[1:-1] = (right - left) / (2 * step)
```

## Broadcasting needs an axis story

```python
oh = np.array([0.001, 0.01, 0.1])
bo = np.array([0.001, 0.01, 0.1, 1.0])
```

`oh * bo` fails because shapes `(3,)` and `(4,)` do not align. If you want every
pair:

```python
oh_grid = oh[:, None]   # shape (3, 1)
bo_grid = bo[None, :]   # shape (1, 4)
combined = oh_grid * bo_grid  # shape (3, 4)
```

The added axes express the intended outer product. Do not add `None` until you
can say what each axis means.

## Vectorisation is not a moral virtue

Vectorisation is excellent when:

- one operation applies independently to an array region;
- shapes express the algorithm;
- NumPy performs the work more clearly and efficiently.

A loop is better when:

- each case may fail differently;
- processing has side effects;
- the next step depends on a convergence history;
- clarity would be lost in a dense expression.

In CoMPhy post-processing, vectorise arithmetic *within* one case and loop or
parallelise *across* independent cases. That boundary often matches the
scientific structure.

## Numerical arrays have a data type

```python
values.dtype
```

Integer division produces floats, but storing into an integer array can still
truncate. Strings loaded from a CSV do not become physical numbers until you
convert and validate them. `nan` and `inf` are floats, so type alone does not
guarantee validity.

```python
if not np.all(np.isfinite(values)):
    raise ValueError("values must be finite")
```

## A visible finite-difference contract

The reference implementation deliberately accepts only a uniform grid:

```python
--8<-- "src/comphy_python101/analysis.py:1:55"
```

Refusing non-uniform spacing is better than applying a uniform formula
silently. A more general algorithm can be added when the course needs it.

## Verify

Complete [Exercise 03](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/03-arrays).
Use \(y=x^2\)
because the second-order boundary and interior formulas should reproduce its
derivative to roundoff on a uniform grid.

Then change one coordinate to make the grid non-uniform. The correct behaviour
for this exercise is a clear error.

## Reflect

For every array in your solution, annotate:

```text
name:
shape:
axis meaning:
units:
valid range:
```

If that feels excessive for a five-line exercise, imagine the same ambiguity
inside a three-dimensional parameter sweep.
