# Displace Geometry Node

## Displace Geometry Node

### Displace Geometry Node

Shifts geometry components along a direction vector or surface normal, creating deformations. Useful for texture-based detail, wave simulation, or field-driven surface variation.

**Inputs**
- Geometry: Elements to offset.
- Selection: Boolean field; unselected parts remain stationary.
- Strength: Magnitude of displacement per element.
- Offset Method: How direction is computed.
  - Normal: Move along local surface normal.
  - Vector: Move along supplied vector (normalized internally).
- Offset Distance Normal: Distance in Normal mode.
- Offset Vector: Vector input in Vector mode.
- Substeps: Count of iterative steps; fields recomputed at each step for stability.
- Post Substep Process: Closure applied after each substep, receiving geometry, selection, strength, and substep index.

**Outputs**
- Geometry: Displaced result.

[Related references](INDEX.md).
