# Frizz Hair Curves

## Frizz Hair Curves

### Frizz Hair Curves

Frizz Hair Curves scatters tiny random offsets down each strand for a frizzy, rough read. It injects natural irregularity, breaking up strands that would otherwise look too clean or identical.

### Inputs

Geometry
Geometry: the hair-curve geometry fed in for frizzing.

Cumulative Offset
On, each point's offset builds on the displacement of earlier points along the strand, so bending comes out continuous and more lifelike.

Factor
The blend strength of the whole effect. At 0.0 there is no frizz; at 1.0 the full random offset lands.

Distance
Scales how large the random per-point offset gets.

Shape
How the offset strength tracks along the strand. At 0.0 the effect is uniform; at 0.5 it falls off linearly from root to tip.

Seed
The random seed behind each unique offset pattern. Move it to change the variation between strands.

Preserve Length
On, the strand keeps its starting length. Off, curves may grow or shrink a little as frizz is added.

### Outputs

Geometry
Output geometry with the frizz applied to the hair curves.

Offset Vector
A vector field recording the per-point displacement that hit each strand.

[Related references](INDEX.md).
