# Exercise 09 — Make analysis callable

## Frame

Expose input and output paths as command-line arguments so another person can
run the reduction without editing source.

## Predict

Which paths must be caller choices, and which failures should remain loud?

## Build

Complete `main` in `starter.py`. Read the validated log, write its JSON summary,
create parent directories, and return zero on success.

## Verify

```bash
uv run pytest exercises/09-cli/test_starter.py
```

## Reflect

A script with three hard-coded path edits is shared code, not yet a tool.
