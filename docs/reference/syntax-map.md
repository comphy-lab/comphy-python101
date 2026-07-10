# Python syntax map

Use this as a lookup after the course gives you a reason for the syntax.

## Bind a name

```python
radius_m = 1e-3
```

The name now refers to a value. Python does not encode units, so the name or a
units library must.

## Make a sequence

```python
cases = ["c001", "c002", "c003"]
```

Lists are ordered and mutable. Tuples are ordered and normally used for fixed
records:

```python
limits = (0.0, 1.0)
```

## Map names to values

```python
summary = {"peak_energy": 0.194, "final_time": 0.75}
summary["peak_energy"]
```

## Branch on a condition

```python
if time_step <= 0:
    raise ValueError("time step must be positive")
elif time_step < warning_limit:
    warn()
else:
    continue_normally()
```

Indentation defines the block.

## Repeat

```python
for case in cases:
    process(case)
```

Use `enumerate` when both index and item matter:

```python
for index, value in enumerate(values):
    ...
```

Use `while` when termination depends on changing state:

```python
while residual > tolerance:
    state = update(state)
```

Always plan a maximum iteration count.

## Define a function

```python
def weber(density, speed, length, surface_tension):
    return density * speed**2 * length / surface_tension
```

Keyword-only policy arguments follow `*`:

```python
def detect(values, *, window=4, tolerance=0.02):
    ...
```

## Fail deliberately

```python
raise ValueError("Oh must be positive")
```

Catch only errors you can handle:

```python
try:
    value = float(text)
except ValueError as error:
    raise ValueError(f"bad value: {text!r}") from error
```

## Work with files

```python
from pathlib import Path

path = Path("data") / "log.csv"
text = path.read_text(encoding="utf-8")
```

For structured CSV, use `csv.DictReader`, NumPy, or pandas with a declared
schema.

## Build arrays

```python
import numpy as np

time = np.linspace(0.0, 1.0, 101)
late = time > 0.5
late_time = time[late]
```

Important attributes:

```python
time.shape
time.ndim
time.dtype
time.size
```

## Import

```python
from comphy_python101 import load_basilisk_log
```

The imported name becomes available in the current module. Avoid wildcard
imports; they hide provenance.

## Main guard

```python
def main():
    ...
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

This lets the file act as a command while keeping functions importable for
tests.

## Tests

```python
def test_length_scaling():
    assert second / first == pytest.approx(2**1.5)
```

The test name states the claim. `pytest.approx` handles floating-point
comparison with a tolerance.

## Formatting strings

```python
message = f"case {case_id}: peak={peak:.3g}"
```

Use formatting for presentation, not before numerical operations.

## Type hints

```python
def summarise(path: Path) -> dict[str, float]:
    ...
```

Hints document intent and help tools. Python does not enforce them at runtime.
Validation is still required at external boundaries.
