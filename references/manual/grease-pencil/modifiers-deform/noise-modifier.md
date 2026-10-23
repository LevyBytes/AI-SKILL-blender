# Noise Modifier

## Noise Modifier

The Noise Modifier destabilizes stroke/point data (position, strength, thickness, UV texture placement) by layering fluctuating offsets that roughen the linework.

Stochastic amplitude can intensify the visual artifact.

**Options.**

Position: noise magnitude impacting point location.

Strength: noise magnitude impacting point strength (opacity).

Thickness: noise magnitude impacting point width.

UV: noise magnitude impacting point UV rotation.

Noise Scale: governs noise frequency bandwidth.

Noise Offset: shifts noise progression along strokes.

Seed: initialization for the pseudo-random sequence.

**Randomize.**

When engaged, noise draws from random values temporally.

Mode:
- Steps: fresh random value at regular intervals.
  Step: frame intervals before value changes.
- Keyframes: fresh random value exclusively on keyframe events.

**Influence.**

See Influence Filters.

[Related references](INDEX.md).
