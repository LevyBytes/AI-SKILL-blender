# Realize Instances Node

## Realize Instances Node

### Realize Instances Node

The Realize Instances node converts instances into unique geometry data. This allows per-instance modification; without it, the same changes apply to all instances of shared geometry. However, performance degrades when realizing many complex-geometry instances, a fundamental computational trade-off.

Note: If input contains multiple volume instances, only the first volume moves to output.

### Attributes

When merging attributes from multiple geometry sources, the highest-complexity data type is chosen. For example, if a weight attribute is boolean on one source and vector on another, the output uses vector.

Named and anonymous attributes propagate from the instance domain to realized geometry. If an attribute exists on both base geometry and an instance, base-geometry values take precedence.

Note:

- The id attribute receives special handling to avoid duplication. Indices of each instance merge with id values from geometry points.

- Vertex groups preserve when realizing instances or joining geometries. If propagation rules yield vertex domain and float type, the attribute becomes a vertex group on output.

### Inputs

Geometry
Input geometry.

Selection
Which top-level instances to realize.

Realize All
Realize all nested-instancing levels for each top-level instance (overrides Depth).

Depth
Nesting levels to realize per top-level instance.

### Outputs

Geometry
Output geometry.

[Related references](INDEX.md).
