# Integration lab 13 · Evidence to capsule

This lab joins lessons 07, 09, 10, 11, and 12 into the course's miniature
reproduction capsule.

## Frame

A clean build must validate inputs, run the tests, create reduced evidence and
figures, write a manifest, verify every digest, and return non-zero on failure.

## Predict

List the expected files before running the build. Which input and output files
must the manifest cover? Which environment facts belong outside the checksum?

## Build

Complete
[`exercises/13-evidence-to-capsule`](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/13-evidence-to-capsule),
then run the full reference command:

```bash
make reproduce
```

## Verify

The exercise first verifies a clean capsule, then changes `summary.json` and
requires checksum verification to fail.

## Reflect

Explain why rebuilding, testing, and verifying are three separate claims even
when one command coordinates all three.
