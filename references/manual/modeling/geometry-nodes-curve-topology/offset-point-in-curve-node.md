# Offset Point in Curve Node

## Offset Point in Curve Node

Offset Point in Curve Node

Fetches neighboring control points by stepping relative to an input point along its curve.

Conceptually similar to Offset Corner in Face Node, but point indices do not wrap around unless the curve is cyclic.

Inputs:
Point Index: Input control point. By default uses field context, requiring point-domain evaluation.
Offset: Step count. In cyclic curves, wrapping occurs past boundaries.

Outputs:
Is Valid Offset: Whether the resulting index exists in the original curve. Always true for cyclic curves.
Point Index: Resulting control point index.

[Related references](INDEX.md).
