# Teaching data

Both CSV files are deliberately small, synthetic, and CC BY 4.0. They mimic the
shape of public CoMPhy post-processing outputs without reproducing an
unpublished simulation.

## `basilisk_log.csv`

| Column | Meaning | Contract |
| --- | --- | --- |
| `t` | dimensionless time | strictly increasing |
| `dt` | time step | positive |
| `kinetic_energy` | domain-integrated kinetic energy | non-negative |
| `h_min` | minimum interfacial length scale | positive |

## `regime_map.csv`

Each row is one synthetic case with a case identifier, Ohnesorge number, Bond
number, and observed categorical outcome. The categories are for teaching only;
they are not a physical regime boundary or published dataset.
