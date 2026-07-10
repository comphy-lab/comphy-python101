# 10 · Reproducible collaboration

Reproducibility is the ability to rebuild a result from declared inputs and
instructions. Collaboration is what tests whether those declarations are real.

<div class="lesson-contract">
  <p><strong>Decision:</strong> can a fresh clone reproduce the evidence without private memory?</p>
  <p><strong>Output:</strong> a locked, tested, reviewable one-command build.</p>
</div>

## Frame

A scientific capsule needs more than a script:

```text
question
code
environment
input or public source
reduced data
tests
figure
provenance
licence
```

Missing pieces become somebody else's archaeology.

## Declare the environment

`pyproject.toml` names the project, Python requirement, dependencies, command
line entry point, and tool configuration. `uv.lock` records the resolved
versions.

```bash
uv sync --locked --all-extras
```

The lock file is not a claim that versions never change. It is a record of the
environment that passed.

## Make one front door

This repository uses:

```bash
make check
```

which expands to lint, tests, and a strict site build. A paper capsule might
use:

```bash
make figure-3
```

The command should be documented and automated. “Run cells 2, 4, 7, change the
path, then click save” is not a build.

## Use version control as reasoning history

A clean cycle is:

```bash
git switch -c feature/clear-name
git status
git diff
git add explicit-file.py test_explicit_file.py
git commit -m "Verify capillary-time scaling"
git push -u origin feature/clear-name
```

The pull request explains:

- what scientific or learner-visible behaviour changed;
- why;
- what verifies it;
- what remains uncertain.

Small commits make regressions and disputed decisions inspectable.

## Continuous integration is a fresh colleague

CI checks the repository in a clean machine:

- install the locked environment;
- lint and format;
- run tests;
- build the website;
- deploy only after the build passes.

It catches missing local files, implicit paths, stale generated content, and
environment assumptions. CI passing means the declared workflow worked. It
does not independently validate the science; that is what the tests must
encode.

## Track provenance and integrity

For each input and output:

```bash
shasum -a 256 data.csv figure.png
```

A checksum detects byte-level change. A provenance note explains meaning:

```text
source:
source commit or DOI:
schema and units:
reduction command:
analysis commit:
known exclusions:
```

Store a small reduced dataset when raw simulation data are too large to ship.
Point to the durable archive for raw inputs.

## Licence every public surface

Public does not automatically mean open source. This course uses:

- BSD-3-Clause for code;
- CC BY 4.0 for prose, original diagrams, and teaching data.

Third-party data, figures, fonts, and code keep their own licences. Record
attribution at the point of reuse.

## Notebooks and generated outputs

Keep a notebook when the interaction is itself valuable. Before committing:

- restart the kernel;
- run all cells in order;
- remove private paths and large accidental outputs;
- move reusable logic into a module;
- state the environment and data source.

Do not treat a 6 MB notebook diff as reviewable source merely because GitHub
renders it.

## The mature CoMPhy pattern

The public
[`SingularJets2026`](https://github.com/comphy-lab/Bursting-Bubble/tree/main/papers/SingularJets2026)
capsule combines a Python 3.12 environment, `uv.lock`, exact regression tests,
fit-window metadata, checksums, reduced-data manifests, and offline CI. That is
the endpoint this course aims towards, scaled down enough for a student to own.

## Verify

Run the course capsule from a clean output directory:

```bash
rm -rf build/capsule
uv run python examples/reproduce_capsule.py --output build/capsule
```

Then:

1. inspect `summary.json`;
2. open both figures;
3. verify `manifest.sha256`;
4. change one input byte and confirm the checksum changes;
5. restore the file with Git.

## Reflect

Imagine you leave the lab for six months. What knowledge exists only in your
head? Each item is either a deliberate boundary or a reproducibility bug.
