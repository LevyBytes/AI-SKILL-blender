# Sort Elements Node

## Sort Elements Node

### Sort Elements Node

Reorders geometry elements via index permutation.

**Inputs**
- Geometry: Standard input.
- Selection: Boolean; sort scope (all if blank).
- Group ID: Cluster ID; elements with matching IDs sort as groups.
- Sort Weight: Values driving reorder.

**Properties**
- Domain: Field evaluation scope.
  - Point: Base/control points.
  - Edge: Mesh edges.
  - Faces: Mesh faces.
  - Spline: Curve splines.
  - Instance: Top-level instances.

**Outputs**
- Geometry: Standard output.

[Related references](INDEX.md).
