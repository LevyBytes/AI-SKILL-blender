# Delete Geometry Node

## Delete Geometry Node

### Delete Geometry Node

Removes specified geometry elements from the input. Operates analogously to Edit Mode deletion. The domain and mode properties control which element types are removed.

**Inputs**
- Geometry: Standard input.
- Selection: Boolean field marking elements for removal.

**Properties**
- Domain: Scope of deletion.
  - Point: Remove vertices, control points, and base points.
  - Edge: Remove mesh edges; other components unaffected.
  - Face: Remove mesh faces; other components unaffected.
  - Spline: Remove entire splines if selected; unchanged otherwise.
  - Instance: Remove top-level instances; realized geometry persists.

- Mode: Deletion granularity (mesh only).
  - All: Remove vertices, edges, and faces together.
  - Only Edges & Faces: Preserve vertices even if selected.
  - Only Faces: Remove only faces.

**Output**
- Geometry: Standard output.

[Related references](INDEX.md).
