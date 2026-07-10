# 13 · Reproduction capsule

The capstone is a small public scientific argument that another person can
rebuild, inspect, and challenge.

<div class="lesson-contract">
  <p><strong>Question:</strong> can one declared workflow turn public or supplied data into a trustworthy figure?</p>
  <p><strong>Output:</strong> a one-command Basilisk-to-publication reproduction capsule.</p>
</div>

## The deliverable

Choose one modest physical question:

- When does an observable plateau?
- Does a reduced quantity follow a limiting scaling?
- How does an outcome change across one nondimensional parameter?
- Does a Python reduction agree with a C/Basilisk result?

Do not begin with “make a dashboard” or “analyse everything”. One question is
enough.

## Required structure

```text
capsule/
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   ├── README.md
│   └── reduced.csv
├── src/
│   └── analysis.py
├── tests/
│   └── test_analysis.py
├── figures/
│   └── result.pdf
├── manifest.sha256
└── Makefile
```

Raw simulation dumps may live in a durable archive rather than Git. The data
README must name the source and explain how `reduced.csv` was produced.

## Required reasoning

### Question

State one claim the figure can test. Name the control and response variables.

### Representation

Document schemas, units, shapes, case IDs, missing values, and valid ranges.

### Transformation

Separate reading, computation, and presentation. Expose genuine choices as
arguments. Do not require source edits to change an input path.

### Verification

Include at least three checks:

1. schema or physical invariant;
2. analytic limit, scaling, conservation, or cross-code comparison;
3. regression on a settled reduced result.

### Evidence

Ship reduced data, a legible figure, and a caption that says what the result
supports and what remains uncertain.

## Execution contract

One command must rebuild the public artefacts:

```bash
make reproduce
```

It should:

1. install or verify the locked environment;
2. validate inputs;
3. run reductions;
4. run tests;
5. create the figure;
6. update or verify checksums;
7. return non-zero if anything fails.

The course's miniature example is:

```bash
uv run python examples/reproduce_capsule.py --output build/capsule
```

Read that script. It is intentionally ordinary. A clear sequence of checked
steps is better than an orchestration framework students cannot explain.

## HPC extension

If the capsule begins from Basilisk snapshots:

```text
archived snapshot
   ↓ qcc-compiled extractor on compute node
per-snapshot reduced row
   ↓ validated Python gather
reduced table
   ↓ tested analysis
figure
```

Requirements:

- pin the Basilisk source or release;
- save the extractor source and compile command;
- submit extraction as a batch job;
- cap concurrency to the allocation;
- make per-snapshot outputs restartable;
- record failed or omitted snapshots;
- never post-process on the login node.

The public
[`Jumping-Drops/postProcess`](https://github.com/comphy-lab/Jumping-Drops/tree/main/postProcess)
pipeline is a useful operational reference. The
[`SingularJets2026`](https://github.com/comphy-lab/Bursting-Bubble/tree/main/papers/SingularJets2026)
capsule is the stronger reproducibility endpoint.

## Review rubric

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Question | absent | broad | precise and falsifiable |
| Representation | implicit | partial | schema, units, shapes, provenance |
| Transformation | tangled | mostly separated | small functions and thin CLI |
| Verification | “looks right” | one check | independent checks plus regression |
| Evidence | figure only | data or caption | reduced data, figure, bounded claim |
| Reproduction | manual folklore | documented steps | clean one-command rebuild |
| Collaboration | private assumptions | some notes | licence, README, reviewable history |

The target is not fourteen points for ornament. It is no zero in any column.

## Submission

Open a pull request containing:

- the capsule;
- a short statement of the claim;
- the rebuild command;
- validation output;
- one rendered figure;
- known limitations.

Keep the first attempt in the branch history or a clearly named file if AI
assistance was substantial. Explain the scientific corrections made.

## Final reflection

Answer:

1. Which result would most change under a different modelling choice?
2. Which test gives you the most confidence?
3. Which part still depends on judgement rather than automation?
4. What would a new student need to reproduce this in a year?

If you can answer those clearly, you have learned more than Python syntax.
