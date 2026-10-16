# Spline Parameter Node

## Spline Parameter Node

Spline Parameter Node

Reports position along each spline via two metrics: distance traveled and normalized progress.

The Factor is not simply index-over-total because vertices may be unevenly distributed along the curve. The initial value is zero, covering distance to the current point rather than beyond it.

At spline domain, outputs the accumulated curve progress at the start of each spline. Spline order is visible in Spreadsheet Editor.

Warning: For NURBS and Bézier splines, values correspond to control points only. NURBS discrepancies are often pronounced. Resample Curve Node creates uniform point density.

Special case: When length is zero, Factor defaults to index-over-total.

Inputs: None

Outputs:
Factor — At point domain: fraction of spline length. At spline domain: fraction of total curve length.
Length — At point domain: distance along the spline. At spline domain: distance along entire curve.
Index — Zero-indexed position within the current spline, separate from the global Index node.

Examples:
Use parameter to drive radial variation along a curve. Start has radius 0, end has radius 1.

[Related references](INDEX.md).
