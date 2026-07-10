# Course overview

Python is not the subject. The subject is how to make a computer answer a
scientific question without quietly changing the question.

The recurring loop is:

```text
question → representation → transformation → verification → evidence
```

Syntax matters in the same way notation matters in mathematics: it must be
precise, but memorising notation is not the same as knowing what to do.

## Who this is for

The course assumes:

- comfort with algebra, graphs, and physical units;
- no prior programming;
- willingness to predict an answer before seeing a plot.

It also works as a reset for students who can already make notebooks run but
have not yet built a tested script, command-line tool, or reproducible figure.

## What you will be able to do

By the end, you should be able to:

1. translate a physical question into explicit inputs, outputs, and failure
   modes;
2. trace values, shapes, units, and state through unfamiliar code;
3. design small functions with testable scientific contracts;
4. use NumPy arrays without losing track of axes or meaning;
5. debug by shrinking a failure and testing a hypothesis;
6. validate tabular data before reducing it;
7. design a plot around a claim rather than around default settings;
8. test limiting behaviour, conservation, and numerical convergence;
9. turn an analysis into a path-safe command-line tool;
10. build a locked, one-command reproduction capsule.

## The lesson rhythm

Every lesson has the same five moves.

<div class="lesson-contract">
  <p><strong>Frame.</strong> What decision are we making? What could make it wrong?</p>
  <p><strong>Predict.</strong> State shapes, units, limits, or trends before execution.</p>
  <p><strong>Build.</strong> Express the smallest transformation that can decide.</p>
  <p><strong>Verify.</strong> Attack it with a claim that could fail.</p>
  <p><strong>Reflect.</strong> Say what the result supports and what it does not.</p>
</div>

## Quick route

Allow 6–8 focused hours. Do these in order:

1. [Think like a program](../core/01-thinking.md)
2. [Functions are scientific claims](../core/02-functions.md)
3. [Arrays are the working language](../core/03-arrays.md)
4. [Debugging and tests](../core/05-debugging.md)
5. [Analysis becomes a tool](../core/09-tools.md)
6. [Read a Basilisk log](../comphy/11-basilisk-log.md)

Then inspect the [reproduction capsule](../comphy/13-capstone.md). If any part
feels like magic, return to the linked full-route lesson.

## Full route

Allow 20–24 hours including exercises.

| Stage | Lessons | Scientific habit |
| --- | --- | --- |
| Model | 01–04 | make state and logic explicit |
| Interrogate | 05–07 | fail loudly, preserve schemas, argue with plots |
| Trust | 08–10 | verify numerics and leave a reproducible trail |
| Practise | 11–13 | turn CoMPhy-style output into public evidence |

Do not binge-read the text. A useful cadence is 20–30 minutes of reading,
45–75 minutes of exercise, and 10 minutes explaining your result to another
person.

## What is deliberately not here

There is no early catalogue of every string method, collection type, class
feature, or plotting option. You will meet language features when a problem
creates a reason for them.

There is also no notebook-only route. Notebooks are excellent scratch benches.
They are poor final contracts when execution order, hidden state, and large
outputs become part of the result. Canonical work in this course ends as
functions, scripts, tests, and small data products.

## Assessment

The capstone is a small Basilisk-to-publication reproduction capsule. It needs:

- one physical question and nondimensional control parameter;
- one public or supplied dataset;
- a command-line tool that validates inputs;
- reduced data and one scientific figure;
- tests for schema, limiting behaviour, and a numerical regression;
- a locked environment, provenance note, and one-command rebuild.

The standard is not code cleverness. The standard is whether another student
can see, challenge, and reproduce the chain of reasoning.
