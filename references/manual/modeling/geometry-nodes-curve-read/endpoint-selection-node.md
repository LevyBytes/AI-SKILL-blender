# Endpoint Selection Node

## Endpoint Selection Node

Endpoint Selection Node

Provides a boolean selection marking the first and last N control points of each spline.

Note: Selection operates on control points; for NURBS and Bézier splines, a single control point may map to many viewport-displayed points.

Tip: Use Capture Attribute Node to preserve this selection after converting to mesh or point cloud.

Inputs:
Start Size — Count of points selected from the beginning.
End Size — Count of points selected from the end.

Outputs:
Selection — Boolean field for start and end regions.

Examples:
Generate first/last point selection for any curve. The shown poly spline in Edit Mode serves as input to Instance on Points Node.

[Related references](INDEX.md).
