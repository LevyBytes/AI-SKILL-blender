# Subdivide Curve Node

## Subdivide Curve Node

The Subdivide Curve node inserts control points between existing ones. For Bézier and poly, shape is unaltered.

Bézier curves gain finer control while keeping the visual level that Bézier provides. Unlike Resample Curve Node, which converts to poly.

Curve: Standard input.
Cuts: Control points to insert on the segment after each point. As a field, the count at each segment is set by the field value at the previous point.

Curve: Standard output.

[Related references](INDEX.md).
