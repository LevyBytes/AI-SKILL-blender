# Dual Mesh Node

## Dual Mesh Node

### Dual Mesh Node

Dual Mesh takes a mesh and emits its dual: every face turns into a vertex and every vertex into a face. Face-domain attributes transfer to the point domain in the dual.

Warning: Only works on manifold (water-tight) geometry. Remesh non-manifold input first.

### Inputs

Mesh
Input geometry.

Keep Boundaries
Preserve non-manifold mesh boundaries by creating additional geometry and skipping the dual transformation there.

### Output

Dual Mesh
Output geometry.

### Examples

The Dual Mesh Node pairs well with triangulated meshes. An Ico Sphere (evenly-spaced triangles) is a good example.

[Related references](INDEX.md).
