# Grid to Points Node

## Grid to Points Node

Transforms a voxel grid into a point cloud representation. All active voxels and tiles map to individual points. The voxel value attaches as an anonymous attribute; index-space data is available as field output. Enables custom volume visualization or downstream point manipulation.

Inputs:
- Grid: Voxel grid to convert

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines Value output type.

Outputs:
- Points: Point cloud (one point per active voxel or tile)
- Value: Stored grid value at each voxel; for tiles, the shared value across all voxels

Voxel Index output:
- X, Y, Z: Voxel coordinates in index space (or tile minimum for tiles)
- Is Tile: True when point represents a tile rather than single voxel
- Extent: Voxel or tile size; 1 for individual voxels; cubic dimension in voxels for tiles

[Related references](INDEX.md).
