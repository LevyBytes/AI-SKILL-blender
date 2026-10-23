# Geometry Node

## Geometry Node

### Geometry Node

Access geometric information about the shading point. All vector coordinates use World Space. For volume shaders, only position and incoming vector are available.

### Inputs

None.

### Properties

None.

### Outputs

- **Position**: Shading point location.
- **Normal**: Surface shading normal (includes smooth normals and bump mapping).
- **Tangent**: Surface tangent direction.
- **True Normal**: Flat/geometry normal of the surface.
- **Incoming**: Vector pointing toward the viewer.
- **Parametric**: Surface parametric coordinates. For area lights outputs UV planar coordinates; for point lights outputs spherical coordinates.
- **Backfacing**: 1.0 if viewed from back, 0.0 from front.
- **Pointiness** *(Cycles Only)* — Vertex-based curvature approximation. Light values indicate convex angles; dark values indicate concave. Useful for dirt maps and wear effects.
- **Random per Island** *(Cycles Only)* — Unique random value per connected mesh component (island). Useful for variations on multi-part objects like tree leaves or wood planks. When using Array modifiers, retrieves a random value per instance.

[Related references](INDEX.md).
