# SDF Grid Mean Node

## SDF Grid Mean Node

Applies mean (box) filter smoothing to a Signed Distance Field. Averages voxel values within a local neighborhood to smooth variations and noise while preserving overall shape. Works as a fast, separable averaging operation (box filter); suited for general-purpose softening after boolean, voxelization, or other volumetric operations.

Inputs:
- Grid: Signed distance field to smooth
- Width: Smoothing kernel radius in voxels; larger values produce broader smoothing, softer less-detailed surfaces; smaller values restrict to immediate neighbors, retaining fine detail
- Iterations: Mean filter application count; each iteration increases surface smoothness; multiple passes approximate Gaussian-like blur

Outputs:
- Grid: SDF after mean filtering; smoother, more uniform surface useful for refining noisy/rough SDFs before Grid to Mesh or other operations

[Related references](INDEX.md).
