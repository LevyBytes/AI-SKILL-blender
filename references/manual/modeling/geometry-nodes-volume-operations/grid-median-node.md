# Grid Median Node

## Grid Median Node

Applies a median (box) filter to a volume grid. Each active voxel becomes the median of neighbors within a box kernel. Median filtering preserves sharp features while removing isolated noise—more effective than mean at edge retention. Use cases: clean sparse artifacts, maintain density/level-set edges.

Properties:
Data Type: Grid data type (Float, Integer, Vector). Must match input.

Inputs:
- Grid: Volume to smooth
- Width: Filter radius in voxels; larger values increase neighborhood scope and smoothing
- Iterations: Filter application count; repeated passes progressively smooth

Outputs:
- Grid: Filtered grid with updated voxel values

[Related references](INDEX.md).
