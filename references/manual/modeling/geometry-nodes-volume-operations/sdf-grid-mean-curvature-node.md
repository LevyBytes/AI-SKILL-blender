# SDF Grid Mean Curvature Node

## SDF Grid Mean Curvature Node

Applies mean curvature flow smoothing to a Signed Distance Field. Evolves the surface based on mean curvature; high-curvature (sharp/noisy) regions smooth faster than flatter areas. Unlike simple averaging or Laplacian, mean curvature flow adapts to geometric features for natural, shape-preserving smoothing. Effective after booleans or mesh-to-SDF conversion for removing high-frequency noise.

Inputs:
- Grid: Signed distance field to smooth (typically from mesh or procedural operation)
- Iterations: Mean curvature flow pass count; each iteration progressively smooths; small values gently polish; large values significantly alter shape

Outputs:
- Grid: SDF after mean curvature smoothing; reduced high-curvature noise, smoother transitions, major structural features retained

[Related references](INDEX.md).
