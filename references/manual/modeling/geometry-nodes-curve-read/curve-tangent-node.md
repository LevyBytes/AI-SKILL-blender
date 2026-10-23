# Curve Tangent Node

## Curve Tangent Node

Curve Tangent Node

Returns the unit-length direction vector at each control point, aligned with curve flow. The Reverse Curve Node governs direction.

Warning: For NURBS and Bézier splines, output corresponds to control points, not evaluated points. A Bézier curve may have 48 evaluated points but only 4 control points (resolution 12). NURBS discrepancies are often larger. Use Resample Curve Node to create a poly spline with aligned densities.

Inputs: None

Outputs:
Tangent: Direction vector per control point.

[Related references](INDEX.md).
