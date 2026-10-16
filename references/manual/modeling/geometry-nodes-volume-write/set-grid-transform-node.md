# Set Grid Transform Node

## Set Grid Transform Node

Establishes how a voxel grid maps from index space (voxel coordinates) into object space. Default mappings assign integer voxel indices directly to object coordinates; this node permits custom mapping matrices for grid repositioning, orientation, or scaling relative to objects/scenes.

Inputs:
- Grid: Grid whose transform changes
- Transform: New transform from grid index space to object space; typically from Transformation Matrix

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines value storage type and must match input grid.

Outputs:
- Is Valid: True if provided transform applied successfully; fails if non-invertible or extreme scaling (0, negative/positive combinations)
- Grid: Grid with updated transform; new transform affects voxel-to-object interpretation, influencing grid interactions with other geometry and sampling

[Related references](INDEX.md).
