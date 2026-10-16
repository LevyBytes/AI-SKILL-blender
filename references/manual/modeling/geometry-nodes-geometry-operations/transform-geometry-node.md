# Transform Geometry Node

## Transform Geometry Node

### Transform Geometry Node

Applies translation, rotation, or scaling to entire geometry as a single unit. For per-element movement, use Set Position Node; for instance-level transforms, use dedicated instance nodes.

**Inputs**
- Geometry: Standard input.
- Mode: Specification method.
  - Components: Separate location, rotation, scale inputs.
  - Matrix: Transformation matrix.
- Translation: Offset in local space.
- Rotation: Euler angles in local space.
- Scale: Scale multiplier in local space.
- Transform: Matrix (Matrix mode only).

**Output**
- Geometry: Standard output.

[Related references](INDEX.md).
