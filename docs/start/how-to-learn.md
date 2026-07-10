# How to learn here

The fastest way to become dependent on code is to run it before you have a
prediction. The fastest way to learn from code is to make a prediction precise
enough that the program can disagree with you.

## Predict before execution

Before pressing run, write at least one of:

- the output type and shape;
- the physical units;
- the sign;
- a limiting value;
- a monotonic trend;
- a failure you expect to see.

“It should make a plot” is not a prediction. “The nondimensional height should
decrease monotonically from one, and the output array should have the same
length as time” is.

## Read errors as evidence

An exception has three useful layers:

1. **type** — what kind of contract failed;
2. **message** — what the code knows about the failure;
3. **traceback** — the path from your call to the failing line.

Start at the final line, then move upward until you reach code you own. Do not
randomly edit every line named in the traceback.

## Shrink before fixing

When a 10,000-case pipeline fails:

1. identify the first failing case;
2. preserve its exact inputs;
3. call the smallest relevant function;
4. remove unrelated plotting, file copying, and parallelism;
5. turn the failure into a test;
6. fix the underlying claim;
7. rerun the full path.

This is scientific control of variables applied to debugging.

## Use notebooks as a lab bench

A notebook is useful for:

- seeing a new dataset;
- trying a transformation;
- inspecting a few cases;
- discussing a figure interactively.

Move durable work into a module or script when:

- cell order matters;
- another figure needs the same logic;
- hidden state changes the result;
- the notebook becomes too large to review;
- a batch job or CI must run it.

The clean endpoint is not “no notebooks”. It is one source of truth.

## Work with AI without outsourcing judgement

AI can accelerate the loop if you keep ownership of the claim.

1. Save the first generated attempt.
2. State what it assumes about inputs, units, shapes, and physics.
3. Run the smallest check that could falsify it.
4. Repair it into a second version.
5. explain the difference in a pull request.

This mirrors a useful practice in the public
[`Intro-Soft-Matter-2025`](https://github.com/comphy-lab/Intro-Soft-Matter-2025)
course: preserve the first attempt, debug it, and explain what changed. The
important part is not that an LLM wrote version one. It is that the student can
audit it.

Never accept an equation because the code is polished. In a public CoMPhy
example, the written Voinov relation and its implementation use different
coefficients. That is not a reason to pick whichever one looks familiar. It is
a reason to return to the derivation, cite the intended convention, and write a
test that makes the decision explicit.

## Ask better help questions

A useful question includes:

- the intended result;
- the smallest input that fails;
- the exact command;
- the full error;
- what you predicted;
- what you have already ruled out.

“Python is broken” gives nobody a mechanism to inspect.

## Keep a reasoning log

For each exercise, retain four short notes:

```text
prediction:
observed:
explanation:
next check:
```

That habit scales directly into simulation logs, issue reports, commit
messages, and methods sections.
