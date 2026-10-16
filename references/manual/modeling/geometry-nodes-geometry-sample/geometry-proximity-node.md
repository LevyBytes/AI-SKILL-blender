# Geometry Proximity Node

## Geometry Proximity Node

### Geometry Proximity Node

Computes the nearest location on target geometry for each source point.

**Inputs**
- Geometry: Source.
- Group ID: Partitions input into searchable groups.
- Sample Position: Query point.
- Sample Group ID: Search scope.

**Properties**
- Target Element: Search surface.
  - Faces: Face surface.
  - Edges: Edge surface.
  - Points: Vertices (mesh or point cloud; fastest).

**Outputs**
- Position: Nearest location.
- Distance: Float distance.
- Is Valid: Success flag (fails if group is empty).

Tip: Map Range Node often pairs with distance output for falloff.

Example: Different modes (faces, edges, points) shown with subdivided/unsubdivided meshes; sphere-distributed points as target.

[Related references](INDEX.md).
