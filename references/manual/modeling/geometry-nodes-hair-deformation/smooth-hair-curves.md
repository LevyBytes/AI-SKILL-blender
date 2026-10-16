# Smooth Hair Curves

## Smooth Hair Curves

### Smooth Hair Curves

Smooth Hair Curves relaxes strand shapes, evening them out by averaging control points across several passes. It cuts noise, cleans up deformation artifacts, and polishes groomed shapes after steps such as frizz or noise.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in for smoothing.

Amount
Smoothing strength. Positive values smooth by averaging point positions; negative values widen the differences between points for a crumpled, distorted look.

Shape
How the smoothing reads along the strand. At 0.0 the effect is even; at 0.5 it falls off linearly from root to tip.

Iterations
How many smoothing passes run. More passes smooth further but can add processing time.

Weight
A per-point weight on how much each point feeds the smoothing. Closer to 0 means less influence there.

Lock Tips
On, the strand tips stay pinned and do not move while smoothing runs.

Preserve Length
On, each strand holds its starting length. Off, smoothing may shorten the curves a little.

### Outputs

Geometry
Output geometry with the smoothed hair curves.

[Related references](INDEX.md).
