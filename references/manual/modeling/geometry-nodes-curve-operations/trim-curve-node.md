# Trim Curve Node

## Trim Curve Node

The Trim Curve node shortens splines by removing sections from start and end.

Bézier splines stay Bézier; the first, last, and their handles adjust to preserve shape. NURBS convert to poly.

Warning: Cyclic splines are not supported.

Note: Since normals compute from the final curve, this node may shift normals under Minimum twist method, as it considers the whole curve. Capture Attribute Node can preserve pre-trim normals.

Curve: Standard input (curve component).
Selection: Boolean field indicating which curves to trim.
Start: Where the trimmed spline begins (factor or length).

Note: If Start > End, the result is a single point at Start.

End: Where the trimmed spline ends (factor or length).

Mode:

Factor: Use 0–1 fraction of spline length.
Length: Use distance from spline start (0 to spline length).

Curve: Standard output.

[Related references](INDEX.md).
