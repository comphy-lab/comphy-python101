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
| 07 Plotting | Does the figure encode the claim without changing the data? | deterministic output and source-array integrity |
| 08 Numerics | Does the derivative converge at the predicted order? | decreasing error and observed order |
| 09 CLI | Can the analysis run without source edits or current-directory folklore? | absolute input path and explicit output |
| 10 Reproducibility | Can byte-level change be detected? | manifest verification and tamper failure |
| 11 Basilisk log | Can one validated log become a summary and figure? | schema failure and complete outputs |
| 12 Log to evidence | Can validation, differentiation, and reduced output stay separate? | analytic derivative and CSV schema |
| 13 Evidence to capsule | Can a clean command rebuild and verify the public evidence? | complete capsule and tamper detection |

Run a starter's checks explicitly:

```bash
uv run pytest exercises/02-functions/test_starter.py
```

The check should fail first. Read the failure, change only `starter.py`, and run
it again. Worked solutions are in the matching `solutions/` folder.

Exercises 12 and 13 are staged integration labs. Complete them in order before
starting the capstone: the first joins numerical and data contracts; the second
joins commands, figures, provenance, and integrity.
