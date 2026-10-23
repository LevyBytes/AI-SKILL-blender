# Set Material Node

## Set Material Node

Set Material Node

Changes material assignment via material_index modification. If the material already exists, the existing index is reused.

Note: Operates on mesh, point cloud, and volume data; other types do not support materials.

Inputs:
Geometry: Standard geometry input.
Material: Material to apply.
Selection: Modify boolean per face. True applies, false preserves. For volumes and point clouds, field input is ignored (single material only).

Outputs:
Geometry: Standard geometry output.

[Related references](INDEX.md).
