# For instructors

This course is designed for guided self-study, a one-day quick route, or a
multi-session onboarding course.

## Recommended formats

### One-day quick route

| Session | Material |
| --- | --- |
| 09:00 | overview and lesson 01 |
| 10:00 | functions and Exercise 02 |
| 11:30 | arrays and Exercise 03 |
| 13:30 | debugging and Exercise 04 |
| 15:00 | tools and Basilisk-log lab |
| 16:30 | explain one result and review |

Aim for roughly 20% exposition and 80% tracing, coding, checking, and
explanation.

### Six-session full route

1. thinking, functions;
2. arrays, control;
3. debugging, schemas;
4. plotting, numerical verification;
5. tools, reproducibility;
6. CoMPhy labs and capstone proposal.

## Facilitation

- Ask for predictions before live execution.
- Let the first test fail visibly.
- Request an adversarial input, not only a happy path.
- Ask “what does this number mean?” more often than “what syntax did you use?”
- Pair students to explain each other's code.
- Do not repair every error immediately; help the student form a discriminating
  check.

## AI-assisted work

Require students to retain an initial generated attempt, identify its physical
and computational assumptions, and explain the corrected version in a pull
request. Grade the audit, not the prompt.

## Solutions

Worked solutions are public by design. Use them after a genuine attempt:

1. compare boundaries and tests before bodies;
2. identify one difference in scientific policy;
3. improve either version;
4. explain the choice.

Hiding solutions in an open repository is security theatre.

## Assessment

Use the capstone rubric. A student should not pass with a polished figure but no
schema, or a comprehensive test suite but no physical question.

## Extending the course

Prefer a new exercise when:

- it represents a recurring CoMPhy task;
- it teaches a distinct decision;
- public or synthetic data suffice;
- a compact automated check exists.

Do not add an exercise merely to cover another Python feature.
