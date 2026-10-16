# Resample Curve Node

## Resample Curve Node

The Resample Curve node converts each input spline to a poly spline. In Count and Length modes, new points are evenly spaced.

Tip: Use a field to vary count/length per spline.

Curve: Standard input.
Selection: Whether to resample each spline (True = resample, False = unchanged).

Mode:

Count: Distribute the specified count evenly.
Length: Split into segments of specified length, rounded down to fit an integer count. Trim Curve Node with a multiple keeps distance exact if spline length changes.
Evaluated: Use the resolution attribute for NURBS/Bézier. Poly unchanged.

Count Count: Points on each new spline.
Length Length: Spacing between points.

Tip: Combine with Trim Curve Node using a length multiple for exact spacing despite spline length variance.

Curve: Standard output.

[Related references](INDEX.md).
