# Clip Grid Node

## Clip Grid Node

Restricts a voxel grid to a bounding box specified in index space. Voxels outside the min/max indices deactivate; their values reset to the grid's background. Partially clipped tiles voxelize fully so individual voxels can be isolated.

Inputs:
- Grid: Input voxel grid to clip
- Min X/Y/Z: Minimum index bounds
- Max X/Y/Z: Maximum index bounds

Properties:
Data Type: Grid data type (Float, Integer, Boolean, or Vector). Must match input grid.

Outputs:
- Grid: Clipped grid with out-of-bounds voxels deactivated and reset

[Related references](INDEX.md).
