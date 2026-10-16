# Grid Laplacian Node

## Grid Laplacian Node

Computes the Laplacian of a scalar voxel grid. Measures how a voxel value differs from neighbor average—how much the field "curves" or deviates locally. Defined as divergence of gradient; used in physics/geometry for diffusion, smoothing, curvature analysis, PDE solving.

Mathematically, Laplacian of f(x,y,z):
∇²f = (∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²)

Positive Laplacian = local minimum (smaller than surroundings); negative = local maximum (larger than surroundings).

Inputs:
- Grid: Scalar grid for Laplacian computation (must store float values like density, temperature, SDF)

Outputs:
- Laplacian: Float grid representing field Laplacian; each voxel contains sum of second derivatives along X/Y/Z axes; detects local peaks/valleys or drives smoothing/diffusion in procedural grids

[Related references](INDEX.md).
