# 09 · Turn analysis into a tool

A reusable analysis has a narrow command-line boundary, pure computational
functions, project-safe paths, useful errors, and an observable output.

<div class="lesson-contract">
  <p><strong>Decision:</strong> can another person run the analysis without editing source?</p>
  <p><strong>Output:</strong> a command-line program with checked inputs and outputs.</p>
</div>

## Frame

This is not a reusable interface:

```python
path = "/Users/name/Desktop/new/final/really-final/log.csv"
```

The path is a caller choice disguised as source code. Expose it:

```bash
comphy-python101 summary run/log.csv
```

## A thin `main`

```python
def main(arguments=None):
    args = build_parser().parse_args(arguments)
    log = load_basilisk_log(args.input)
    summary = summarise_log(log)
    print(json.dumps(summary, indent=2))
    return 0
```

`main` coordinates. Parsing and reduction remain testable without launching a
subprocess.

The course CLI follows this shape:

```python
--8<-- "src/comphy_python101/cli.py"
```

## Command-line arguments are a schema

Use `argparse` to state:

- required inputs;
- optional outputs;
- types;
- help;
- mutually exclusive choices where needed.

The resulting `--help` is part of the interface:

```bash
uv run comphy-python101 --help
```

An argument should change a meaningful choice. Do not expose every local
variable merely because you can.

## Paths without folklore

Use `pathlib.Path`:

```python
output = Path(args.output)
output.parent.mkdir(parents=True, exist_ok=True)
```

Do not build paths with manual `"/"` concatenation. Do not assume the user's
home directory or current working directory.

## External programs must fail visibly

Scientific workflows often call compiled extractors:

```python
subprocess.run(
    [str(extractor), str(snapshot), str(output)],
    check=True,
)
```

Use a list of arguments and `check=True`. Avoid `shell=True` with interpolated
input: it adds quoting ambiguity and command-injection risk.

After a successful command, check that the expected output exists and is
non-empty. A zero exit status is not evidence that the right file was written.

The public figure rebuilder in
[`Soft-Matter-Singularities-paper-figures`](https://github.com/comphy-lab/Soft-Matter-Singularities-paper-figures/blob/main/scripts/rebuild_all_figures.py)
does this well. A public legacy visualiser,
[`BasiliskVisualization/vView2D_v1.py`](https://github.com/VatsalSy/BasiliskVisualization/blob/master/vView2D_v1.py),
is a useful refactoring contrast: manual `sys.argv`, global state, hard-coded
assumptions, nested array loops, and `shell=True`.

## Exit status is an output

Return zero for success and non-zero for failure. Let unexpected exceptions
produce a traceback during development. For expected user mistakes, give a
short actionable message.

Do not catch everything:

```python
try:
    ...
except Exception:
    pass
```

That converts evidence into silence.

## Make repeated work restartable

For a case or snapshot pipeline:

- give outputs deterministic names;
- skip only when an output passes a validity check;
- write partial outputs atomically where possible;
- record failed case IDs;
- avoid deleting raw inputs;
- support selecting a subset from the CLI.

Parallelise across independent cases. On HPC, request a compute node and keep
concurrency within allocated resources. The
[`Jumping-Drops/postProcess`](https://github.com/comphy-lab/Jumping-Drops/tree/main/postProcess)
notes make the important operational point explicit: single-node batch
processing, not login-node work.

## Verify

Complete
[Exercise 09](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/09-cli),
then run:

```bash
uv run comphy-python101 summary data/basilisk_log.csv
uv run comphy-python101 plot-log data/basilisk_log.csv \
  --output build/log.png
```

Then run the first command from another directory with an absolute input path.
The command should still behave predictably.

Refactor a small personal plotting script so that:

1. source paths become arguments;
2. computation moves into a function;
3. output is explicit;
4. invalid input returns a useful failure;
5. one test calls the function directly.

## Reflect

If another student must open your source and edit three path variables before
running it, you have shared code, not yet a tool.
