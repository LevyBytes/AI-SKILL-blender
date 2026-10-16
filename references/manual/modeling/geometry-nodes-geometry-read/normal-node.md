# Normal Node

### Normal Node

Outputs a unit vector indicating normal direction per evaluated point. Output varies by domain:
- Face: Surface "up" direction.
- Mesh Vertices: Average of connected face normals; or normalized position if isolated.
- Edge: Average of the two vertex normals.
- Face Corner: Same as face normal.
- Curve Control Points: Evaluated curve normal, perpendicular to curve path.

Caution: For NURBS and Bézier curves, output is at control points, not evaluated points; may differ visually. Use Resample Curve Node to create poly spline with points at every evaluated location.

**Inputs**
None.

**Outputs**
- Normal: Direction vector.
- True Normal: Mesh normals without custom attribute override.

[Related references](INDEX.md).
