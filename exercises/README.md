# Exercises

Each exercise is a scientific decision, not a syntax quiz.

| Exercise | Decision | Main check |
| --- | --- | --- |
| 01 Thinking | What must be true before code can answer the question? | hand trace and failure modes |
| 02 Functions | Is the capillary-time claim explicit and unit-consistent? | analytic value and invalid inputs |
| 03 Arrays | Does the derivative preserve shape and order? | exact quadratic derivative |
| 04 Debugging | Has a plateau really lasted for a complete window? | adversarial time series |
| 05 Files | Does the input obey the promised schema? | missing/corrupt columns |
| 06 Regime map | Can categories be reduced without losing case identity? | counts and unknown categories |

Run a starter's checks explicitly:

```bash
uv run pytest exercises/02-functions/test_starter.py
```

The check should fail first. Read the failure, change only `starter.py`, and run
it again. Worked solutions are in the matching `solutions/` folder.
