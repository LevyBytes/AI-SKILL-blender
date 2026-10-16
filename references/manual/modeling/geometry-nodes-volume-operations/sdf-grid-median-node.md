# SDF Grid Median Node

## SDF Grid Median Node

Applies a median filter to a Signed Distance Field. Each voxel becomes the median of its neighbors—eliminating noise and small artifacts while retaining sharp features and edges. Non-linear filtering excels at impulsive noise (isolated spikes/dips) versus mean or Laplacian approaches. Retains overall structure and perimeter definition. Valuable for refining SDFs from noisy or voxelized source meshes.

Inputs:
- Grid: Signed distance field to filter
- Width: Median filter kernel radius in voxels; larger widths produce stronger smoothing via wider neighborhood
- Iterations: How many times the filter runs; more passes deepen the smoothing and knock back noise while still holding edges crisp

Outputs:
- Grid: SDF after median filtering; reduced high-frequency noise and artifacts; sharp edges and important structural details retained

[Related references](INDEX.md).
