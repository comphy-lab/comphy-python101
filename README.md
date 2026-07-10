# CoMPhy Python 101

[![Course website](https://img.shields.io/badge/course-comphy--lab.org-0b5d5b)](https://comphy-lab.org/comphy-python101/)
[![CI](https://github.com/comphy-lab/comphy-python101/actions/workflows/ci.yml/badge.svg)](https://github.com/comphy-lab/comphy-python101/actions/workflows/ci.yml)
[![Pages](https://github.com/comphy-lab/comphy-python101/actions/workflows/pages.yml/badge.svg)](https://github.com/comphy-lab/comphy-python101/actions/workflows/pages.yml)
[![Code: BSD-3-Clause](https://img.shields.io/badge/code-BSD--3--Clause-2f6f9f)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-e45d3f)](LICENSE-CONTENT)

Learn to reason with Python, not memorise it.

CoMPhy Python 101 is an open course for future CoMPhy Lab students and anyone
moving into scientific computing. It starts with questions, representations,
logic, and verification. Syntax arrives only when a problem needs it. The final
route is recognisably CoMPhy: simulation output becomes reduced data, a tested
claim, and a reproducible figure.

## The course spine

```text
question → representation → transformation → verification → evidence
```

Every lesson uses the same loop:

1. **Frame** the scientific question and the failure modes.
2. **Predict** shapes, units, limiting behaviour, or a qualitative trend.
3. **Build** the smallest transformation that can answer the question.
4. **Verify** it with an invariant, test, benchmark, or convergence check.
5. **Reflect** on what the result supports and what it does not.

## Two routes, one repository

| Route | Time | Use it when |
| --- | ---: | --- |
| Quick route | 6–8 hours | You already code occasionally and need the CoMPhy workflow |
| Full route | 20–24 hours | You are new to Python or want a firmer scientific-computing foundation |

There is no separate nano fork. The quick route selects lessons from the full
course, so examples, fixes, and tests cannot drift.

## Start

The course is designed to be read at
[comphy-lab.org/comphy-python101](https://comphy-lab.org/comphy-python101/).

For the runnable material:

```bash
git clone https://github.com/comphy-lab/comphy-python101.git
cd comphy-python101

# Recommended: installs Python and the locked environment when needed
uv sync --all-extras

# Check the reference implementation and build the site
uv run pytest
uv run mkdocs build --strict
```

No `uv` yet? Install it from the
[official documentation](https://docs.astral.sh/uv/getting-started/installation/),
or create a Python 3.11+ virtual environment and run
`python -m pip install -e ".[dev,docs]"`.

## What students build

- small functions whose inputs, outputs, units, and failure modes are explicit;
- NumPy transformations that preserve shapes and physical meaning;
- tests for limiting behaviour, schemas, and numerical regressions;
- command-line analysis tools with project-relative paths;
- deterministic, publication-ready figures;
- a Basilisk-to-publication reproduction capsule with provenance.

## Repository map

```text
docs/                   Website, lessons, instructor material
src/comphy_python101/   Tested scientific reference code
exercises/              Starter tasks and student-facing checks
solutions/              Worked solutions
examples/               Complete command-line workflows
data/                   Small synthetic datasets
tests/                  Unit, regression, and course-contract tests
```

## Grounded in CoMPhy practice

The curriculum was built after auditing public repositories across
[`comphy-lab`](https://github.com/comphy-lab) and
[`VatsalSy`](https://github.com/VatsalSy). It teaches the recurring workflow:
NumPy arrays, plotting, schemas, Basilisk post-processing, checked subprocesses,
HPC batch work, tests, locked environments, and reproducible paper figures.

It also uses real public failure modes as teaching material. A script that runs
is not necessarily correct; a notebook is not automatically reproducible; and a
beautiful plot can still encode the wrong equation.

## Contributing

Corrections, new exercises, translations, and small public teaching datasets
are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull
request.

## Licences

- Code, starters, solutions, tests, and workflows are BSD-3-Clause; see
  [LICENSE](LICENSE).
- Lesson prose, original diagrams, and teaching datasets are CC BY 4.0; see
  [LICENSE-CONTENT](LICENSE-CONTENT).

Dependencies retain their own licences.
