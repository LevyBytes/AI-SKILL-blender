# Redistribute Curve Points

## Redistribute Curve Points

### Redistribute Curve Points

Redistribute Curve Points moves existing control points to sit evenly spaced down each curve. It improves uniformity — especially after deforms or procedural steps that warp point spacing — keeping interpolation consistent and results smoother.

### Inputs

Curves
Curves — the input geometry whose control points get redistributed.

Factor
Strength of the redistribution. At 0.0 the curves are unchanged; at 1.0 even spacing applies fully.

Feature Awareness
A lightweight feature-preserving algorithm that tries to hold local curve features and direction changes as points move, keeping detailed areas or sharp bends more accurate.

### Outputs

Curves
Output geometry with redistributed, evenly spaced curve control points.

[Related references](INDEX.md).
