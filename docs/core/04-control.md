# 04 · Control flow expresses an algorithm

Conditions and loops are not topics to memorise. They are how code expresses
decisions, repetition, and state changes.

<div class="lesson-contract">
  <p><strong>Decision:</strong> does the control flow match the stated algorithm?</p>
  <p><strong>Output:</strong> a small event detector with explicit termination.</p>
</div>

## Frame

Find the first time a minimum length falls below a threshold.

The algorithm is:

```text
visit samples in time order
if the threshold is crossed, return that index
if no sample crosses, return no result
```

Python follows directly:

```python
def first_crossing(values, threshold):
    for index, value in enumerate(values):
        if value < threshold:
            return index
    return None
```

The early `return` is part of the meaning: “first”.

## Predict

Test mentally:

- the first value already crosses;
- exactly one value equals the threshold;
- no value crosses;
- values are not time ordered.

The final case reveals an input contract. The loop cannot infer physical time
order from a list of values.

## Conditions should read like the policy

Prefer:

```python
if time_step <= 0:
    raise ValueError("time step must be positive")
```

to:

```python
if not time_step > 0:
    ...
```

Negated compound logic is where edge cases hide. Give a complex decision a
name:

```python
window_is_flat = span <= absolute_tolerance + relative_tolerance * scale
if window_is_flat:
    return stop - 1
```

## Loops carry state

A cumulative integral needs the previous state:

```python
integral = np.zeros_like(x)
for index in range(1, len(x)):
    width = x[index] - x[index - 1]
    area = 0.5 * width * (f[index] + f[index - 1])
    integral[index] = integral[index - 1] + area
```

At each step, name the invariant:

> `integral[index]` contains the trapezoidal integral through `x[index]`.

This is the useful way to reason about a loop. Trace one iteration and confirm
the invariant survives.

The public
[`Contact-Line-101`](https://github.com/comphy-lab/Contact-Line-101)
script is a compact place to see a log grid, functions, a cumulative integral,
and deterministic plotting in one scientific story.

## Separate case loops from array algebra

A parameter sweep often has two scales:

```python
for case in cases:
    data = load_case(case)
    reduced = compute_vectorised_quantities(data)
    save_case(case, reduced)
```

The case loop handles paths, failures, restartability, and provenance. Array
operations handle numerical transformations within a case.

This boundary also tells you how to parallelise: independent cases or snapshots
can be distributed; tightly coupled array operations stay together.

## Termination is a scientific choice

Iterative algorithms need:

- a quantity to monitor;
- a tolerance with scale;
- a maximum iteration count;
- a result for non-convergence.

```python
for iteration in range(max_iterations):
    state = update(state)
    if residual(state) < tolerance:
        return state
raise RuntimeError("iteration did not converge")
```

Without the maximum, a bug can become an infinite job. Without the residual
definition, “converged” is a mood.

## Comprehensions are compact loops

```python
valid_paths = [path for path in paths if path.is_file()]
```

Use a comprehension when the transformation and filter are each simple. Use a
normal loop when you need multiple decisions, logging, exceptions, or state.
Readability is the optimisation target.

## Verify

Write `first_crossing(time, values, threshold)` that validates equal lengths and
strictly increasing time, then returns both the index and time.

Tests should cover the four predictions above. Add a duplicated time sample and
make it fail loudly.

## Reflect

For each `if`, write the policy in words. For each loop, write the invariant.
If the sentence and code disagree, fix the code or the sentence before adding
features.
