# Convex Hull Node

## Convex Hull Node

### Convex Hull Node

Generates a mesh that wraps around and encloses all input geometry points.

When applied to instanced geometry, the algorithm processes each instance separately, producing a distinct convex shape per instance. Use the Realize Instances node to consolidate instance data before computing, if a single hull across all instances is needed.

Limitations: volumes cannot be processed by this operation; input attributes are not carried forward to output. Due to floating-point precision constraints, points lying very close together may merge in the output geometry.

**Inputs**
- Geometry: Standard input.

**Outputs**
- Convex Hull: Enclosing mesh.

[Related references](INDEX.md).
