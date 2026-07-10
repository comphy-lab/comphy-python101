# Practice map

The lessons explain one decision at a time. The exercises make each decision
fail, pass, and leave an artefact.

| Stage | Exercises | Evidence |
| --- | --- | --- |
| Foundations | 01–06 | traced state, contracts, arrays, tests, schemas, case identity |
| Scientific workflow | 07–11 | figures, convergence, CLI, checksums, validated log evidence |
| Integration | 12–13 | reduced derivative table, verified reproduction capsule |

Exercise 01 is a paper trace with no code scaffold. Each numbered folder from
02 to 13 in
[`exercises/`](https://github.com/comphy-lab/comphy-python101/tree/main/exercises)
contains a starter and tests. The matching
[`solutions/`](https://github.com/comphy-lab/comphy-python101/tree/main/solutions)
folder contains a worked answer.

Run one starter check explicitly:

```bash
uv run pytest exercises/07-plotting/test_starter.py
```

The first failure is part of the exercise. Edit only `starter.py`, predict which
claim should pass next, and rerun the narrow check.

Complete [Integration lab 12](12-log-to-evidence.md) and then
[Integration lab 13](13-evidence-to-capsule.md) before designing a new capstone.
