# Mesh Boolean Node

## Mesh Boolean Node

### Mesh Boolean Node

This node performs set operations on two input geometries: intersection, union, and subtraction. It provides the same functionality as the Boolean modifier.

### Inputs

Mesh 1/2: Receives standard geometry.

Self Intersection Exact Solver: When present, handles cases where one or both operands contain self-intersections. The tradeoff is slower computation.

Hole Tolerant Exact Solver: Optimizes results for non-manifold surfaces. Higher computational cost applies; use only when the solver produces errors on non-manifold input.

### Properties

Operation

Intersect: Retains only the volume shared by both input geometries.

Union: Combines the two meshes and removes interior faces.

Difference: Removes geometry 2 from geometry 1, keeping everything outside geometry 2.

Solver: Algorithm for computing Boolean results.

Float: Fast but incompatible with overlapping surfaces.

Exact: Slower; handles coplanar or overlapping faces correctly.

Manifold: Fastest option; restricted to manifold meshes and Difference-plane operations.

### Output

Mesh: Standard geometry output.

Intersecting Edges Exact Solver: Boolean attribute; selects edges created at contact between inputs.

[Related references](INDEX.md).
