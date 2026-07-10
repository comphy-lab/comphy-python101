# Python preflight

This page is the on-ramp for learners who have not programmed before. It is a
compact vocabulary check, not a hidden prerequisite course.

<div class="lesson-contract">
  <p><strong>Decision:</strong> can you trace the small Python structures used in lesson 01?</p>
  <p><strong>Output:</strong> a hand trace that names values, types, iteration, and one failure.</p>
</div>

## Frame

Python stores values under names:

```python
time = 0.45
label = "kinetic energy"
samples = [0.10, 0.18, 0.19]
row = {"t": 0.45, "kinetic_energy": 0.186}
```

`time` is a floating-point number, `label` is text, `samples` is an ordered
list, and `row` maps explicit field names to values. Predict the value and type
of each expression before running it:

```python
samples[0]
samples[-1]
row["t"]
len(samples)
```

## Predict

What should fail here, and why is the failure useful?

```python
row["surface_tension"]
float("not-a-number")
samples[10]
```

Read an error from the final line upwards: the final line names the immediate
failure; the traceback shows how execution reached it.

## Build

A function names one transformation:

```python
def peak(values):
    return max(values)

peak(samples)
```

A loop repeats a transformation while preserving visible state:

```python
converted = []
for value in ["0.10", "0.18", "0.19"]:
    converted.append(float(value))
```

Lesson 01 later compresses the same idea into a generator expression:

```python
peak = max(float(row["kinetic_energy"]) for row in rows)
```

Read it as the ordinary loop below:

```python
energies = []
for row in rows:
    energies.append(float(row["kinetic_energy"]))
peak = max(energies)
```

## Verify

Without running code, trace this program on paper:

```python
rows = [{"energy": "0.10"}, {"energy": "0.19"}]
energies = [float(row["energy"]) for row in rows]
assert max(energies) == 0.19
```

Record the value and type of `row`, `row["energy"]`, `energies`, and
`max(energies)`. Then change one string to `"missing"` and predict the first
failure.

## Reflect

You are ready for lesson 01 if you can explain:

- what a name refers to;
- how a list differs from a dictionary;
- what indexing and a function call do;
- how a loop and a comprehension repeat work;
- where to begin reading a traceback.

Keep the [syntax map](../reference/syntax-map.md) open while learning. Looking up
notation is normal; hiding an unexamined assumption is the actual problem.
