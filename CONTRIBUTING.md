# Contributing

Small, concrete improvements are welcome: a clearer explanation, a failing
edge-case test, a better starter prompt, an accessibility fix, or a compact
public dataset with provenance.

## Before changing a lesson

State which part of the reasoning loop improves:

- question;
- representation;
- transformation;
- verification;
- evidence.

Avoid adding syntax merely because Python has it. A concept belongs when it
helps a student make a scientific decision.

## Development

```bash
uv sync --all-extras
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv run mkdocs build --strict
```

For an individual exercise, follow its README and run its check file directly.
The repository-level test suite validates solutions, not incomplete starters.

## Pull requests

- Keep one conceptual change per pull request.
- Explain the learner-visible reason for the change.
- Include or update a test when behaviour changes.
- Use only public or synthetic data. Record provenance and units.
- Do not commit notebook outputs unless the output is itself the lesson.
- Do not add secrets, private paths, unpublished data, or HPC credentials.

## Writing

- British English.
- Mechanism first.
- One conceptual turn per section.
- Prefer a small worked example over a catalogue of features.
- Use `Frame → Predict → Build → Verify → Reflect` in every lesson.

## Licensing contributions

By contributing, you agree that code is offered under BSD-3-Clause and lesson
content, original diagrams, and teaching data are offered under CC BY 4.0.
