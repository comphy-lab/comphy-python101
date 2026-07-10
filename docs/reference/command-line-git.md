# Command line and Git

These are the small commands used throughout the course.

## Orient yourself

```bash
pwd                 # current directory
ls                  # contents
cd path/to/project  # change directory
```

Run project commands from the repository root unless documented otherwise.

## Inspect files

```bash
head data/log.csv
tail data/log.csv
less data/log.csv
```

Search quickly:

```bash
rg "steady_state" .
rg --files
```

## Run Python

```bash
uv run python script.py
uv run python script.py --help
uv run pytest tests/test_io.py -q
```

`uv run` uses the project environment. Without `uv`, activate your virtual
environment first.

## Git state

```bash
git status -sb
git diff
git diff --staged
git log --oneline -10
```

Read the diff before staging.

## Branch, stage, commit

```bash
git switch -c lesson/clear-description
git add docs/core/03-arrays.md tests/test_analysis.py
git commit -m "Clarify array-shape contract"
```

Stage explicit files when unrelated work is present. A commit should capture
one coherent change and why it exists.

## Restore carefully

To discard one unstaged file change:

```bash
git restore path/to/file
```

This is destructive. Inspect `git diff -- path/to/file` first. Never use
`git reset --hard` as routine tidying.

## Pull and push

```bash
git pull --ff-only
git push -u origin lesson/clear-description
```

`--ff-only` refuses to invent a merge commit when local and remote histories
diverge.

## Check an output checksum

```bash
shasum -a 256 data.csv
shasum -a 256 -c manifest.sha256
```

Linux may use `sha256sum` instead.

## Useful failure clues

| Message | First question |
| --- | --- |
| `command not found` | is the program installed and on `PATH`? |
| `No such file or directory` | what is `pwd`, and is the path caller-relative? |
| `ModuleNotFoundError` | which Python interpreter is active? |
| `Permission denied` | are you executing a file that should be passed to Python? |
| non-zero exit from subprocess | what did stderr say, and which input triggered it? |

Do not prefix arbitrary commands with `sudo` to silence permissions. Understand
which resource is protected.
