# Contributing

The course is open to corrections, translations, new exercises, public
datasets, and accessibility improvements.

The repository contribution guide is
[`CONTRIBUTING.md`](https://github.com/comphy-lab/comphy-python101/blob/main/CONTRIBUTING.md).

Before proposing material, state:

1. the scientific decision the learner will make;
2. which reasoning step it teaches;
3. the public or synthetic data source;
4. the automated check;
5. why the lesson is not already covered.

Build locally:

```bash
uv sync --all-extras
make check
```

Open an issue for ambiguous scientific content before investing in a large
rewrite. Small corrections can go directly to a focused pull request.
