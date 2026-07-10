# 01 · Think like a program

Programming begins before Python. A program is a precise account of how
information changes.

<div class="lesson-contract">
  <p><strong>Decision:</strong> can you state the computation without hiding behind code?</p>
  <p><strong>Output:</strong> a hand-traced pipeline with explicit state and failure modes.</p>
</div>

## Frame

Suppose a simulation writes:

```text
t, dt, kinetic_energy, h_min
```

You want to report the final time, peak kinetic energy, and minimum \(h_{\min}\).
The first useful description is not Python:

```text
read rows
check the schema
convert named columns to numbers
check time order and physical bounds
reduce the arrays
report the result
```

This already contains the structure of the program. Python supplies notation
for the structure.

## Predict

Before inspecting code, answer:

- What is one row?
- Which values vary from row to row?
- Which column names and units are promises?
- Does row order matter?
- What result types do you expect?
- Which invalid states should stop the analysis?

If `t` moves backwards, taking `t[-1]` still produces a number. It simply no
longer means “the final time”. That is why validation precedes reduction.

## Represent state

Every representation makes some operations easy and others dangerous.

```python
row = {
    "t": 0.45,
    "dt": 0.05,
    "kinetic_energy": 0.186,
    "h_min": 0.15,
}
```

A dictionary makes names explicit. A list such as
`[0.45, 0.05, 0.186, 0.15]` is shorter, but its meaning depends on an external
column order. Later, arrays make whole-column numerical operations easy.

Ask of every object:

1. What does one item mean?
2. What does its position mean?
3. What can change it?
4. What must always be true?

Types are useful because they narrow possible meanings. Names and shapes narrow
them further.

## Trace a transformation

Read code from the inside out:

```python
peak = max(float(row["kinetic_energy"]) for row in rows)
```

Trace one row:

| Step | Value | Type | Meaning |
| --- | --- | --- | --- |
| `row["kinetic_energy"]` | `"0.186"` | string | text from the CSV |
| `float(...)` | `0.186` | float | numerical energy |
| generator | one value per row | stream | all energies |
| `max(...)` | `0.194` | float | peak energy |

This is more informative than saying “`max` finds the biggest thing”. It keeps
the representation change visible.

## Separate effects from transformations

Three jobs are often tangled:

1. **I/O** reads files and writes figures.
2. **computation** maps inputs to results.
3. **presentation** chooses labels, layout, and formatting.

A function that both opens a hard-coded file and draws a figure is difficult to
test. A function that accepts arrays and returns a reduction can be checked with
three numbers.

```python
def peak_energy(kinetic_energy):
    return max(kinetic_energy)
```

The function is not “better” because it is short. It is better because its
claim is visible.

## Read unfamiliar code as a story

Use four passes:

1. **Boundary pass** — find inputs, outputs, files, commands, and external
   programs.
2. **Shape pass** — write the shape and meaning of the main objects.
3. **Decision pass** — mark conditions, loops, early exits, and exceptions.
4. **Evidence pass** — find assertions, tests, checksums, and saved outputs.

Do not begin by understanding every line. First find the program's skeleton.

The public
[`rebuild_all_figures.py`](https://github.com/comphy-lab/Soft-Matter-Singularities-paper-figures/blob/main/scripts/rebuild_all_figures.py)
is a useful mature example: figure jobs are data, paths are anchored, commands
must succeed, and expected outputs are checked. Its taste comes from making the
workflow legible.

## Verify

Complete [Exercise 01](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/01-thinking)
on paper. Create a
false plateau that defeats a two-sample “steady” rule. If you cannot make an
adversarial example, your definition is probably still vague.

## Reflect

For the program you traced:

- Which assumptions came from physics?
- Which came from the data format?
- Which were numerical policy?
- Which were merely Python syntax?

That separation is the foundation of the course.
