# Set up once

The goal is a fresh clone that behaves like everyone else's fresh clone. An
environment is not bureaucracy; it is how “works on my machine” becomes a
testable statement.

## Recommended path: `uv`

Install `uv` using its
[official instructions](https://docs.astral.sh/uv/getting-started/installation/).
Then:

```bash
git clone https://github.com/comphy-lab/comphy-python101.git
cd comphy-python101
uv sync --all-extras
```

`uv` reads `pyproject.toml`, installs the Python version named in
`.python-version`, and recreates the dependency versions recorded in
`uv.lock`.

Run the smoke checks:

```bash
uv run python --version
uv run comphy-python101 summary data/basilisk_log.csv
uv run pytest
```

The summary should be JSON with 16 samples and a final time of 0.75. The test
suite should pass.

## Plain Python path

Python 3.11 or newer is sufficient.

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -e ".[dev,docs]"
    pytest
    ```

=== "Windows PowerShell"

    ```powershell
    py -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install -e ".[dev,docs]"
    pytest
    ```

Use `python -m pip`, not a bare `pip`, when you are unsure which interpreter a
command belongs to.

## Read a command as a sentence

```bash
uv run python examples/reproduce_capsule.py --output build/capsule
```

- `uv run` selects the project environment.
- `python` executes a Python file.
- `examples/reproduce_capsule.py` is the program.
- `--output build/capsule` is an explicit input to that program.

The shell is not outside programming. Paths, arguments, exit status, and working
directory are part of the computation.

The full capsule front door adds environment, tests, a clean rebuild, and
checksum verification around that explicit program:

```bash
make reproduce
```

## Your editor

Use any editor that can:

- show line numbers;
- display the selected Python interpreter;
- search across the repository;
- open a terminal in the project root.

Visual Studio Code, PyCharm, and a terminal editor all work. Do not spend the
first hour polishing an editor theme. Make the smoke test pass.

## Common setup failures

### `command not found`

The shell cannot locate the executable. Check installation and restart the
terminal before changing code.

### `ModuleNotFoundError`

Usually the wrong interpreter is active or dependencies were not installed.

```bash
which python       # macOS / Linux
where.exe python   # Windows
python -c "import sys; print(sys.executable)"
```

### A relative path cannot be found

Check:

```bash
pwd
ls
```

Run course commands from the repository root unless the exercise says
otherwise. Later, you will make tools independent of the caller's working
directory with `pathlib`.

### Matplotlib cannot open a display

Batch and CI machines have no desktop. Scientific scripts should save figures,
not require a window. The reference plotting functions do exactly that.

## Final check

Build the website locally:

```bash
uv run mkdocs serve
```

Open the displayed local URL. If code tests and the site build both work, the
environment is ready.
