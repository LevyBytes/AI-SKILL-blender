# Curve to Points Node

## Curve to Points Node

The Curve to Points node generates a point cloud from a curve.

Curve: Standard input.
Count: Points to generate (Count mode only).
Length: Segment length (Length mode only).

Mode:

Evaluated: Points from the curve's pre-computed evaluation, using the resolution attribute for NURBS/Bézier. Usually fastest, no extra sampling.
Count: Distribute the specified count evenly across each spline.
Length: Split each spline into segments of specified length. The length rounds down to fit an integer count. Trim Curve Node with a multiple prevents jumping if spline length changes.

Points: Generated point cloud.
Tangent: The curve tangent at sampled position (or direct evaluated normal in Evaluated mode).
Normal: The normal from the evaluated curve at each point, matching Normal Node output at those locations.
Rotation: Euler rotation built from Tangent and Normal, for convenience.

[Related references](INDEX.md).
