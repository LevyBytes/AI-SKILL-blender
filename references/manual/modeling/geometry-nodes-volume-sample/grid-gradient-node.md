# Grid Gradient Node

## Grid Gradient Node

Calculates the gradient of a scalar voxel grid. Gradient is a vector field describing direction and rate of steepest increase at each voxel; shows how and where scalar quantity (density, temperature, distance) changes in 3D space. Gradient vector points toward increasing values; magnitude represents change rate in that direction.

Mathematically, gradient of f(x,y,z):
∇f = (∂f/∂x î + ∂f/∂y ĵ + ∂f/∂z k̂)

Used in procedural or simulation workflows deriving direction fields from scalars (surface normals from SDFs, flow direction from density/temperature).

Inputs:
- Grid: Grid for gradient computation (must contain float values like density/distance)

Outputs:
- Gradient: Vector grid representing field gradient; each vector points toward greatest value increase; length corresponds to change rate

[Related references](INDEX.md).
