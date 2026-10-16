# Curve Segment

## Curve Segment

### Curve Segment

Curve Segment reports on the segment linking each point to the one before it. It helps when analyzing or reworking per-segment data — length, direction, connectivity — and when building effects keyed to local curve structure.

### Inputs

No inputs on this node.

### Outputs

Segment Length
How far the current point sits from its predecessor on the same curve. Use it to gauge curve smoothness, catch segment stretching, or deform relative to curve length.

Segment Direction
A unit vector aimed from the prior point at the current one. It captures the segment's local tangent heading.

Neighbor Index
The index of the previous neighboring point along the curve. Use it to reference or sample attributes from the adjacent point.

[Related references](INDEX.md).
