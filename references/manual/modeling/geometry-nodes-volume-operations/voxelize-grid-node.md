# Voxelize Grid Node

## Voxelize Grid Node

Expands all active tiles in a sparse voxel grid into fully-voxelized regions. Sparse grids (SDFs, fog volumes) store inactive areas as compact tiles; this node unpacks tiles into explicit voxels, enabling direct access and modification. Preparatory for operations needing dense voxel data (sampling, filtering, arithmetic using neighboring values).

Inputs:
- Grid: Grid to voxelize (typically sparse SDF or fog volume whose active tiles should expand)

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector)

Outputs:
- Grid: Result with all active tiles converted to individual voxels; for fog volumes, interior sparse tiles expand to editable voxel values; for SDFs, produces fully dense representation suitable for precise sampling and editing

[Related references](INDEX.md).
