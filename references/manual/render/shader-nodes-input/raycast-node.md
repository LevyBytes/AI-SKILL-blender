# Raycast Node

### Raycast Node

Cast a ray into the scene and report geometry data from the first surface intersection. This node is computationally expensive and can slow renders significantly; consider baking results for speed improvement.

**Cycles:** Treats all geometry as opaque; transparency doesn't discard hits.

**EEVEE:** Subject to standard Screen-Space Effects limitations.

### Inputs

- **Position**: Ray starting point. Defaults to surface position when unconnected.
- **Direction**: Ray direction. Defaults to surface normal when unconnected.
- **Length**: Maximum ray distance before "no hit" conclusion.

### Properties

**Only Local**: Report only hits on the object itself, not other scene objects.

### Outputs

- **Is Hit**: 1 if hit detected, 0 otherwise.
- **Self Hit**: 1 if hit was on the object itself, 0 otherwise.
- **Hit Distance**: Ray distance to impact. Returns ray Length if no hit found.
- **Hit Position**: Impact location. Returns zero vector if no hit found.
- **Hit Normal**: Geometry normal of hit surface. Returns zero vector if no hit found.

[Related references](INDEX.md).
