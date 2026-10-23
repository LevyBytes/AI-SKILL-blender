# Trim Hair Curves

## Trim Hair Curves

### Trim Hair Curves

Trim Hair Curves cuts strands down or scales them against a target length or length factor — precise overall length, varied or randomized trims, and adjustable groom density and layering.

### Inputs

Geometry
Geometry: the hair-curve geometry fed in for trimming.

Scale Uniform
On, each strand scales uniformly to the target length. Off, the trim works progressively from root to tip.

Length Factor
Multiplies original strand length by this number. At 1.0 the hair holds; at 0.5 it is halved.

Replace Length
On, the Length input takes over the strand length outright rather than scaling it by the Length Factor .

Length
Target length for the op, consulted while Replace Length is on.

Mask
A per-curve mask modulating how much the trim bites. At 0.0 that strand is left alone; at 1.0 the full effect applies.

Random Offset
Works random variation into each strand's trimmed length for more natural hair.

Pin at Parameter
Names a parameter along each strand as the pivot or anchor while trimming; the trim runs relative to it.

Seed
The random seed behind the random offset. Move it for different trim variations under the same settings.

### Outputs

Geometry
Output geometry with the trimmed or scaled hair curves.

[Related references](INDEX.md).
