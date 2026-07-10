# Scientific Python taste

Taste is compressed experience. These rules are defaults, not scripture, but
each protects a recurring failure mode.

## Names

- Use physical meaning: `surface_tension`, not `s`.
- Include units when values are dimensional: `radius_m`, `time_s`.
- Keep established dimensionless names: `oh`, `we`, `bo`, with a nearby
  definition.
- Do not encode temporary history in names: `final_new_v2`.

## Functions

- One function should make one level of decision.
- Prefer explicit inputs and returned outputs over globals.
- Keep I/O, computation, and presentation separable.
- Expose scientific policy as named arguments.
- Reject invalid domains at the boundary.

## Arrays

- Treat shape and axis meaning as part of the type.
- Validate alignment before arithmetic.
- Vectorise clear numerical regions, not complicated control flow.
- Do not allocate a million points before asking what accuracy needs.
- Preserve case identity through reductions.

## Files and paths

- Use `pathlib`.
- Never commit a collaborator-specific absolute path.
- Keep raw inputs immutable.
- Name reduced schemas and units.
- Write outputs deterministically and check that they exist.

## Plots

- Begin with the claim.
- State dimensional or nondimensional axes.
- Use log scales for ratios and scaling, not drama.
- Combine marker and colour for categories.
- Ship reduced data behind important figures.
- Inspect at final publication size.

## Numerics

- Stable is not accurate.
- Converged residual is not small model error.
- Check a limit, conservation law, or resolution trend.
- Record fit windows and exclusions.
- Use a regression test only after independent verification.

## Errors

- Fail early and name the violated contract.
- Never use bare `except`.
- Preserve tracebacks for unexpected failures.
- Turn every fixed bug into the smallest useful test.

## Tools

- A shared script needs `--help`.
- Use a thin `main()` and test functions directly.
- Call subprocesses with argument lists and `check=True`.
- Avoid `shell=True` with interpolated input.
- Respect HPC boundaries; use compute jobs for post-processing.

## Reproducibility

- Declare dependencies in `pyproject.toml`.
- Commit the lock file for a capsule.
- Provide one rebuild command.
- Record provenance and checksums.
- Licence code and content explicitly.
- Make the clean-clone path part of CI.

## One review question

At every boundary ask:

> What wrong result could pass through this code without becoming loud?

Then decide whether a name, validation, test, or design change should make it
louder.
