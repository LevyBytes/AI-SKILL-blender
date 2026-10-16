# Grid Dilate & Erode Node

## Grid Dilate & Erode Node

Expands or contracts the active voxel regions of a volume grid. Modifies which voxels are active without changing stored values. Common uses: grow/shrink regions, fill gaps, remove noise, adjust boundaries.

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Must match input.

Inputs:
- Grid: Volume grid to modify
- Connectivity: Determines neighboring voxel treatment:
  - Face: 6-connectivity (face-adjacent only)
  - Edge: 18-connectivity (face or edge adjacent)
  - Vertex: 26-connectivity (face, edge, or vertex adjacent)
- Tiles: Active tile handling during operation:
  - Ignore: Tiles unmodified and don't contribute
  - Expand: Convert tiles to voxels, apply operation, leave fully voxelized
  - Preserve: Keep tiles unchanged when possible; voxelize only as needed (memory efficient)
- Steps: Operation repetition count; higher values expand/contract further

Outputs:
- Grid: Result with updated active voxel regions

[Related references](INDEX.md).
