# 11 · Read a Basilisk log

This lab joins the core ideas: a named schema, validated arrays, a reduction,
tests, a CLI, and a figure.

<div class="lesson-contract">
  <p><strong>Question:</strong> when does kinetic energy plateau while the minimum scale continues to shrink?</p>
  <p><strong>Output:</strong> a JSON evidence record and a deterministic two-panel figure.</p>
</div>

The supplied data are synthetic. They mimic a Basilisk-style diagnostic log and
do not encode an unpublished run.

## Frame

Inspect the first rows:

```bash
head data/basilisk_log.csv
```

The contract is documented in [`data/README.md`](https://github.com/comphy-lab/comphy-python101/blob/main/data/README.md).

Write down:

- expected sample count;
- time range and spacing;
- valid signs for every quantity;
- a numerical definition of “plateau”;
- whether shrinking \(h_{\min}\) is compatible with steady kinetic energy.

The final question is physical. The program can report trends; it cannot decide
their interpretation without a model.

## Predict

Before plotting:

1. energy should rise and approach approximately 0.194;
2. \(h_{\min}\) should remain positive and decrease;
3. the two arrays should share the time shape;
4. a four-sample, three-per-cent window should eventually detect a plateau.

## Build: validate once

```python
from comphy_python101 import load_basilisk_log

log = load_basilisk_log("data/basilisk_log.csv")
```

Inspect:

```python
log.time.shape
log.kinetic_energy.shape
log.minimum_length.min()
```

Now break a copy:

```bash
cp data/basilisk_log.csv /tmp/broken-log.csv
```

Make one time repeat and run:

```bash
uv run comphy-python101 summary /tmp/broken-log.csv
```

The reader should stop before reduction.

## Build: reduce to evidence

```bash
uv run comphy-python101 summary data/basilisk_log.csv
```

The output is machine-readable:

```json
{
  "samples": 16,
  "final_time": 0.75,
  "peak_kinetic_energy": 0.194,
  "minimum_length": 0.073,
  "steady_from_time": 0.65
}
```

Do not trust this block merely because the course printed it. Read
`summarise_log` and calculate the accepted rolling window.

The steady time is not a universal physical event. It depends on the declared
window and tolerance. Record those values if the result enters a paper.

## Build: make the argument visible

```bash
uv run comphy-python101 plot-log data/basilisk_log.csv \
  --output build/basilisk-log.png
```

Inspect:

- are both \(y\)-axes logarithmic for a reason?
- are all values legal on those axes?
- is the shared time axis clear?
- would normalising time by \(t_\sigma\) improve comparison across cases?

<figure class="scientific-figure">
  <img src="../../assets/figures/basilisk-log.png" alt="Two logarithmic time-series panels show kinetic energy approaching a plateau and minimum length continuing to shrink.">
  <figcaption>The rendered exemplar is generated from <code>data/basilisk_log.csv</code>; the trend supports a numerical statement, while its physical interpretation remains model-dependent.</figcaption>
</figure>

## Verify

Complete
[Exercise 11](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/11-basilisk-log),
then run the targeted reference tests:

```bash
uv run pytest tests/test_io.py tests/test_plotting.py -q
```

Inspect the regression test that establishes:

> a log with negative kinetic energy must fail and name the violated column.

Useful evidence layers are:

1. schema test;
2. range and ordering invariants;
3. reduction regression;
4. figure-output smoke test;
5. visual and physical interpretation.

## Extend

Add a command:

```bash
comphy-python101 derivative data/basilisk_log.csv
```

It should:

- compute \(dh_{\min}/dt\);
- save a reduced CSV with `t,h_min,dh_min_dt`;
- state the finite-difference assumption;
- refuse a non-uniform grid or use an algorithm that supports it;
- include an analytic test independent of the simulation data.

## HPC boundary

A real Basilisk workflow may contain thousands of snapshots:

```text
snapshot → compiled Basilisk extractor → reduced row
```

Run extractors across independent snapshots on an allocated compute node.
Gather reduced rows, sort by time, validate the schema, then plot. Never launch
a multiprocessing sweep on the login node.

## Reflect

The log became evidence only after three questions were separated:

- Does the file obey its contract?
- Does the numerical reduction behave as claimed?
- What physical statement does the trend support?

Do not compress those into “the plot looks right”.
