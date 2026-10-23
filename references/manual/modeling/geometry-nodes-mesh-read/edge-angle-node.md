# Edge Angle Node

## Edge Angle Node

### Edge Angle Node

Outputs radian angle between faces meeting at edge. For face/corner/point domains, interpolates from edge values.

Note: Output depends on mesh density. Denser meshes with same curvature produce different angles.

### Inputs

None.

### Outputs

Unsigned Angle: Shortest angle (0 to PI). Flat and non-manifold edges: 0. Back-folded: PI (180°). Computing this is faster than signed angle; use when distinction unnecessary.

Signed Angle: Signed angle. Flat and non-manifold: 0. Concave positive, convex negative.

[Related references](INDEX.md).
