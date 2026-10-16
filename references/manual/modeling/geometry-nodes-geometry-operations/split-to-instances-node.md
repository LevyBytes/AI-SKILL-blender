# Split To Instances Node

## Split To Instances Node

### Split To Instances Node

Groups geometry elements (e.g., faces) by ID, then converts each group into an instance.

**Inputs**
- Geometry: Standard input.
- Selection: Boolean; included elements.
- Group ID: Integer cluster identifier.

**Properties**
- Domain: Element type and field scope.
  - Point: Base/control points.
  - Edge: Edges.
  - Face: Faces.
  - Spline: Splines.
  - Instance: Top-level instances.
  - Layer: Grease Pencil layers.

Note: Geometry outside the chosen domain is removed (e.g., selecting Edge drops faces and splines).

**Outputs**
- Instances: Grouped geometry.
- Group ID: Cluster index per instance.

Example: 1000x1000 grid of square faces, each assigned a group ID from a Voronoi texture (multiplied by 1000 to exceed 0–1 range), then translated by random Z offset per group.

[Related references](INDEX.md).
