# Cube Grid Topology Node

## Cube Grid Topology Node

Generates a boolean grid topology with specified bounds and resolution. Defines voxel layout and active region; usable with Field to Grid to construct volume grids. Output contains active voxels within regular, axis-aligned cube region.

Inputs:
- Bounds Min: Minimum world-space boundary; lower cube corner
- Bounds Max: Maximum world-space boundary; upper cube corner
- Resolution X/Y/Z: Voxel count along each axis; higher values increase detail and memory usage

Index space properties (Min):
- X, Y, Z: Starting voxel index for each axis

Outputs:
- Topology: Boolean grid defining grid topology and active region; active voxels correspond to bounds/resolution cube

[Related references](INDEX.md).
