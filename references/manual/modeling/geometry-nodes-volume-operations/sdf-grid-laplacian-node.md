# SDF Grid Laplacian Node

## SDF Grid Laplacian Node

Applies Laplacian flow smoothing to a Signed Distance Field grid. Progressively smooths the surface by diffusing fine details across neighboring voxels. Computationally efficient alternative to mean curvature flow. Refines SDFs from meshes or booleans where sharp transitions or voxel artifacts occur. Improves surface quality before mesh conversion.

Inputs:
- Grid: Signed distance field to smooth
- Iterations: Laplacian smoothing pass count; each iteration diffuses high-frequency surface variations; higher values increase smoothness but may cause slight surface shrinkage

Outputs:
- Grid: SDF after Laplacian flow; smoother, more continuous surface while preserving major shape features

[Related references](INDEX.md).
