# Grid Divergence Node

## Grid Divergence Node

Computes the divergence of a vector field in a voxel grid. Divergence measures how much a field "spreads out" or "converges"—net flow entering or leaving each voxel. Positive divergence = field expanding outward (source); negative = converging inward (sink); near-zero = locally balanced flow. Used in fluid/smoke simulations for incompressibility enforcement or flow visualization.

Mathematically, divergence of F = (Fx, Fy, Fz):
∇ · F = (∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z)

Inputs:
- Grid: Vector grid for divergence calculation (must store 3D vectors like velocity/directional fields)

Outputs:
- Divergence: Float grid representing field divergence; positive values = regions where vectors spread (sources); negative = regions where vectors converge (sinks)

[Related references](INDEX.md).
