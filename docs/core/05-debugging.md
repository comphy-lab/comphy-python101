# 05 · Debugging is experimental science

Debugging is not staring harder. It is a controlled sequence of hypotheses and
tests.

<div class="lesson-contract">
  <p><strong>Decision:</strong> which assumption first became false?</p>
  <p><strong>Output:</strong> a smallest failing example and a regression test.</p>
</div>

## Frame

A pipeline reports that the kinetic energy became steady at \(t=0.10\), but the
curve rises sharply afterwards.

Possible hypotheses:

- the data are unsorted;
- the tolerance is too loose;
- only two adjacent values are checked;
- the wrong column is used;
- the returned index is off by one.

Each hypothesis suggests a different experiment.

## Predict

Construct a six-value series with a short false plateau followed by growth:

```python
values = [0.0, 1.0, 1.01, 2.0, 3.0, 4.0]
```

A two-point detector accepts indices 1–2. A detector promising a three-sample
window must reject the series.

## Shrink the failure

Remove:

- file reading;
- plotting;
- parallel processing;
- every unrelated column;
- all cases except the first failure.

Call the smallest function with a literal list. The goal is a failure you can
understand in one screen.

## Turn it into a test

```python
def test_false_plateau_is_rejected():
    values = [0.0, 1.0, 1.01, 2.0, 3.0, 4.0]
    assert steady_state_index(values, window=3) is None
```

Run it and see it fail before changing the implementation. Otherwise, you do
not know whether the test can detect the bug.

## Tests are different kinds of evidence

### Example test

A hand-calculated input gives a known output.

### Property or limit

Doubling \(L\) changes \(t_\sigma\) by \(2^{3/2}\).

### Invariant

Time remains strictly increasing; a mass fraction stays within \([0,1]\).

### Regression

A settled dataset produces a specific reduced value or checksum. Regression
protects a result; it does not explain why the result is correct.

Use more than one kind for important scientific code.

## Tracebacks localise, not diagnose

The last traceback line tells you where Python noticed a failure. The cause may
be earlier:

```text
ValueError: operands could not be broadcast together with shapes (200,) (199,)
```

The error is detected in arithmetic. The cause may be two slices representing
different physical intervals. Print or assert shapes at the boundary where they
are created.

## Assertions and exceptions

Use exceptions for invalid external input:

```python
if np.any(time_step <= 0):
    raise ValueError("dt must be positive")
```

Use assertions for internal states that would indicate a programmer mistake:

```python
assert reduced.shape == time.shape
```

Do not use `assert` to validate user files in production; Python can disable
assertions.

## When prose and code disagree

One audited public contact-line example documents a coefficient \(3Ca\) while
its implementation uses \(9Ca\). The lesson is not “replace 9 with 3”. The
lesson is:

1. identify the convention and derivation intended;
2. check the cited source or analytic limit;
3. encode the decision in one function;
4. add a test that would fail under the other coefficient;
5. update prose and code together.

“The script ran” cannot resolve a modelling disagreement.

## Use version history as an instrument

When a working result breaks:

```bash
git diff
git log --oneline -- path/to/file.py
```

The diff narrows what changed. A small commit gives you a controlled experiment.
This is why “various fixes” is a useless commit.

## Verify

Complete [Exercise 04](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/04-debugging).
Keep the
intentional bug long enough to explain exactly why the first test catches it.

Then run:

```bash
uv run pytest tests/test_analysis.py -q
```

Read the test names as a specification.

## Reflect

Write a four-line debugging record:

```text
symptom:
hypothesis:
discriminating check:
result:
```

If the check cannot distinguish your hypothesis from alternatives, it is not
yet a good experiment.
