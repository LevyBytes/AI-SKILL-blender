# Sample Curve Node

## Sample Curve Node

Sample Curve Node

Evaluates a point at a specific distance or progress fraction along the curve, interpolating custom attribute values from surrounding evaluated vertices.

When the curve contains multiple splines, the sample location references total accumulated length across all splines in Spreadsheet Editor order.

Inputs:
Curves — Geometry input with curve data.
Value — Custom attribute field to evaluate and output.
Factor — Normalized progress (0–1) mode.
Length — Distance units mode.
Curve Index — Isolate specific splines. Ignored when All Curves is enabled.

Properties:
Data Type — Output attribute type.

Mode — Endpoint location method, paralleling Trim Curve Node behavior.
Factor — Normalize within each spline (0–1).
Length — Distance from spline start.

All Curves — Use total curve length instead of per-spline length.

Outputs:
Value — Sampled attribute value.
Position — Curve location.
Tangent — Unit direction vector.

Tip: Combine with Align Rotation to Vector Node to match curve direction. Layer a second rotation node with Normal to align a second axis.

Normal — Unit surface perpendicular.

Examples:
Recreates Resample Curve Node's Count mode, but outputs a mesh instead. Z component of position can serve as sample factor (0–1 range across the line).

[Related references](INDEX.md).
