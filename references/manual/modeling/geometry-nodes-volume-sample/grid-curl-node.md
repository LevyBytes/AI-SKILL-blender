# Grid Curl Node

## Grid Curl Node

Computes the curl of a vector field in a voxel grid. Curl represents local rotational motion or circulation—how much and in what direction the field "spins" around each point.

Mathematically, curl of F = (Fx, Fy, Fz):
∇ × F = ((∂Fz/∂y - ∂Fy/∂z) î + (∂Fx/∂z - ∂Fz/∂x) ĵ + (∂Fy/∂x - ∂Fx/∂y) k̂)

Result vector points along rotation axis; magnitude indicates rotation strength. Useful for generating turbulence or analyzing rotational flow behavior in simulations and procedural effects.

Inputs:
- Grid: Vector grid for curl calculation (must store 3D vectors like velocity/direction fields)

Outputs:
- Curl: Vector grid representing field curl (local rotation); output direction indicates rotation axis; magnitude represents rotational strength at each voxel

[Related references](INDEX.md).
