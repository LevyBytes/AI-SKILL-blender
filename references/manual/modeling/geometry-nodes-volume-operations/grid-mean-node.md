# Grid Mean Node

## Grid Mean Node

Applies a box (mean) filter to a volume grid. Each active voxel's value becomes the average of neighbors within a box-shaped kernel. Smooths data, reduces high-frequency variation. Use cases: soften density, smooth noise, prepare volume for further work.

Properties:
Data Type: Grid data type (Float, Integer, Vector). Must match input.

Inputs:
- Grid: Volume to smooth
- Width: Filter radius in voxels; larger values increase neighborhood size and smoothing strength
- Iterations: Mean filter application count; higher values progressively smooth

Outputs:
- Grid: Filtered grid with smoothed voxel values

[Related references](INDEX.md).
