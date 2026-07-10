# 07 · A plot is an argument

A plotting library can render almost anything. Scientific judgement determines
what should be rendered and what conclusion the figure can support.

<div class="lesson-contract">
  <p><strong>Decision:</strong> which visual encoding tests the stated claim?</p>
  <p><strong>Output:</strong> a deterministic figure backed by reduced data.</p>
</div>

## Frame

Suppose the claim is:

> kinetic energy approaches a plateau while the minimum length scale continues
> to shrink.

The figure needs both quantities against the same time coordinate. Their scales
may differ by orders of magnitude, so two aligned panels are clearer than two
unlabelled axes overlaid.

## Predict

Before plotting:

- Which axis is independent?
- Are quantities dimensional or nondimensional?
- Which trends should be monotonic?
- Is zero possible on a log axis?
- What visual comparison carries the claim?
- What data must remain available behind the figure?

## Start with the claim

```python
figure, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(time, kinetic_energy)
axes[1].plot(time, minimum_length)
```

Then make meaning explicit:

```python
axes[0].set_ylabel("kinetic energy")
axes[1].set_xlabel("time")
axes[1].set_ylabel(r"$h_{\min}$")
```

If values are dimensionless, say so in the caption or symbol definition. If
they have units, include them.

## Linear, log, and normalised scales

Use a log scale when ratios and power laws are the comparison. Do not use it to
make a weak trend look dramatic.

On log axes:

- values must be positive;
- multiplicative spacing is visible;
- a straight line suggests a power law only over the shown range;
- fitted exponents need a declared window and uncertainty.

Normalisation is a physical decision:

$$
\hat{t} = t/t_\sigma.
$$

Name the scale and justify it. “Nondimensional” is not enough.

## Encode categories accessibly

For a regime map, use both colour and marker:

```python
styles = {
    "no-jet": ("x", blue),
    "one-drop": ("o", gold),
    "multiple-drops": ("^", coral),
}
```

The figure remains interpretable when printed in greyscale or viewed with
colour-vision deficiency. Direct labels often beat a distant legend.

## Defaults are not neutral

Check:

- axis limits;
- aspect ratio;
- tick precision;
- legend order;
- line and marker overlap;
- font size at final publication width;
- whether a colour map is sequential, diverging, or categorical.

Never connect unordered categories with a line. Never draw a smooth regime
boundary simply because an interpolator is available.

## Save deterministically

```python
figure.savefig(output, dpi=180, bbox_inches="tight")
plt.close(figure)
```

A shared script should save an output and exit. `plt.show()` is useful during
exploration but fails on headless batch machines and cannot serve as a build
contract.

Keep figure creation inside a function so tests can check that an output is
written and source arrays remain unchanged.

The course reference functions are intentionally modest:

```python
--8<-- "src/comphy_python101/plotting.py"
```

<figure class="scientific-figure">
  <img src="../../assets/figures/basilisk-log.png" alt="Two aligned logarithmic panels show kinetic energy rising to a plateau while minimum length decreases with time.">
  <figcaption>The shared time axis supports the comparison; separate panels avoid a misleading dual-axis overlay. Synthetic teaching data.</figcaption>
</figure>

<figure class="scientific-figure">
  <img src="../../assets/figures/regime-map.png" alt="A logarithmic Ohnesorge–Bond regime map distinguishes no jet, one drop, and multiple drops using colour and marker shape.">
  <figcaption>Colour and marker shape carry the categories together; no interpolated boundary is invented between sparse cases.</figcaption>
</figure>

## A figure is not the data

Ship the reduced table used to draw it. A reader should be able to:

- inspect exact values;
- change an axis choice;
- test another normalisation;
- reproduce the figure without raw simulation dumps.

The public
[`Soft-Matter-Singularities-paper-figures`](https://github.com/comphy-lab/Soft-Matter-Singularities-paper-figures)
repository is a strong example of making figure jobs, commands, and expected
outputs explicit.

## Verify

Complete
[Exercise 07](https://github.com/comphy-lab/comphy-python101/tree/main/exercises/07-plotting),
then run the two reference commands:

```bash
uv run comphy-python101 plot-log data/basilisk_log.csv \
  --output build/log.png
uv run comphy-python101 plot-regime data/regime_map.csv \
  --output build/regime-map.png
```

Inspect both at their final display size. Then remove colour temporarily. Do
categories and hierarchy survive?

## Reflect

Write the claim of your last scientific figure in one sentence. For every
visual element, ask whether it supplies evidence, orientation, or decoration.
Decoration is allowed. Confusion is not.
