# Raycast Node

## Raycast Node

### Raycast Node

Casts rays from source geometry onto target geometry, returning hit locations, normals, distances, and interpolated attributes.

**Inputs**
- Target Geometry: Ray target.
- Attribute: Optional field evaluated on target; interpolated at hit.
- Interpolation: Mapping strategy.
  - Interpolated: Smooth barycentric blending.
  - Nearest: Closest vertex value.
- Source Position: Ray origin (default = Position Node).
- Ray Direction: Ray vector (evaluated on source context).
- Ray Length: Max distance before "no hit."

**Properties**
- Data Type: Output type.

**Outputs**
- Is Hit: True if ray intersects.
- Hit Position: Intersection point.
- Hit Normal: Surface normal at intersection.
- Hit Distance: Distance from origin (or Ray Length if no hit).
- Attribute: Interpolated result.

[Related references](INDEX.md).
