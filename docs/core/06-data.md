# 06 · Data has a schema

A file is not “just numbers”. It is a contract between the program that wrote
it and every program that will interpret it.

<div class="lesson-contract">
  <p><strong>Decision:</strong> does the input mean what the analysis assumes?</p>
  <p><strong>Output:</strong> a validated named schema and a reduced data product.</p>
</div>

## Frame

The teaching log promises:

| Column | Meaning | Validity |
| --- | --- | --- |
| `t` | dimensionless time | finite, strictly increasing |
| `dt` | time step | finite, positive |
| `kinetic_energy` | integrated kinetic energy | finite, non-negative |
| `h_min` | minimum length scale | finite, positive |

Validation turns that prose into executable boundaries.

## Predict

For each corrupted input, decide whether to stop, skip a row, or record missing
data:

- `h_min` column absent;
- one `kinetic_energy` value is `"failed"`;
- time is repeated after a restart;
- `h_min` is zero;
- the file has a header but no rows.

There is no universal answer. The point is to choose deliberately and record
the policy.

## Use names, not positions

```python
with path.open(newline="", encoding="utf-8") as stream:
    reader = csv.DictReader(stream)
    rows = list(reader)
```

Now `row["kinetic_energy"]` carries meaning. `row[7]` carries an undocumented
dependency on column order.

Check the header before conversion:

```python
required = {"t", "dt", "kinetic_energy", "h_min"}
missing = required.difference(reader.fieldnames or [])
if missing:
    raise ValueError(f"missing required columns: {sorted(missing)}")
```

## Validate at the boundary

The reference reader converts and checks once:

```python
log = load_basilisk_log("data/basilisk_log.csv")
```

Downstream functions receive a `SimulationLog`, not an arbitrary dictionary.
That does not make invalid data impossible, but it creates one visible place
where the contract is enforced.

```python
--8<-- "src/comphy_python101/io.py:1:92"
```

Notice the line number in conversion errors. “Could not convert string to
float” is much less useful than “`run.csv:417: h_min is not a number`”.

## Preserve raw and reduced data

A good workflow does not overwrite the source.

```text
raw log.csv
   ↓ validated reader
reduced summary.csv
   ↓ figure script
figure.pdf
```

Reduced data should include enough identifiers and metadata to trace each row
back to a case. A figure should not be the only surviving representation of the
result.

The public
[`Jumping-Drops/postProcess`](https://github.com/comphy-lab/Jumping-Drops/tree/main/postProcess)
pipeline documents a 12-column schema, per-snapshot processing, energy
integration, and reduced CSV/PNG outputs. The reusable idea is not its exact
columns. It is that the schema and execution policy are written down.

## Paths are data too

```python
from pathlib import Path

root = Path(__file__).resolve().parents[1]
input_path = root / "data" / "log.csv"
```

This anchors a repository-relative path to the script, rather than to whichever
directory the caller happened to be in. Avoid hard-coded `/Users/name/...`
paths in shared code.

Command-line paths are even better when the input is a genuine choice:

```bash
python analyse.py run/log.csv --output figures/run-12.png
```

## Record provenance

At minimum, a reduced dataset should state:

- source file or case identifier;
- source checksum or immutable commit where practical;
- schema and units;
- program version or commit;
- parameters controlling the reduction;
- creation date.

For small public capsules, a `README` plus `manifest.sha256` is enough.

## Large data need the same contract

Do not load a 100 GB file merely because `pandas.read_csv` can be typed in one
line. Decide:

- which columns are required;
- whether rows can be streamed or chunked;
- whether one case can be processed independently;
- where reduced outputs belong;
- how a partial run resumes.

On HPC, process independent snapshots in a single-node batch job or suitable
data-transfer node. Never turn the login node into an analysis workstation.

## Verify

Complete [Exercise 05](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/05-files).
After the tests pass,
add one test for a repeated time value. Decide whether the starter's summary
function should own that check or whether a separate reader should.

## Reflect

Write the schema for one dataset you currently use. If the column meaning lives
only in your memory or a plotting script, the dataset is not yet self-describing
enough to collaborate on.
