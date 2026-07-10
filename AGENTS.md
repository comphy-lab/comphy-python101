# CoMPhy Python 101

Open-source, mechanism-first Python onboarding for scientific computing in the
CoMPhy Lab.

## Structure

```text
docs/                   Course website and lessons
src/comphy_python101/   Tested reference implementation
exercises/              Student starters and local checks
solutions/              Worked solutions
examples/               End-to-end runnable examples
data/                   Small synthetic teaching datasets
tests/                  Repository-level regression tests
```

## Development

```bash
uv sync --all-extras
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv run mkdocs build --strict
uv run mkdocs serve
```

## Course contract

- Teach `question → representation → transformation → verification → evidence`.
- Make students predict before they run code.
- Keep I/O, computation, and presentation separate.
- Use names that preserve physical meaning and units.
- Treat assertions and tests as scientific claims, not software ceremony.
- Keep notebooks exploratory; canonical implementations live in scripts and
  modules.
- Never encourage post-processing on an HPC login node.
- All datasets in this repository are synthetic or explicitly public.

## Editing

- British English.
- Prefer short lessons with one conceptual turn.
- Every lesson follows: **Frame → Predict → Build → Verify → Reflect**.
- Starter code may contain `TODO`; reference code and CI must remain clean.
- New numerical claims need either an analytic limit, a conservation check, a
  convergence check, or a regression test.
- Build links and assets for the `/comphy-python101/` project-site path.
- Do not add a `CNAME`; the organisation custom domain is inherited.

## Licences

- Code, starter files, solutions, tests, and workflows: BSD-3-Clause.
- Lesson prose, original diagrams, and teaching datasets: CC BY 4.0.
