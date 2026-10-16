# Flip Faces Node

## Flip Faces Node

### Flip Faces Node

The Flip Faces node reverses vertex and edge order for each selected face. Primary use: inverting face normals. Face-corner domain attributes reverse as well.

While normals are typically the goal, the node is not called "Flip Normals" for a key reason: it does not directly modify normals. The right-hand rule defines normals from vertex order, so reversing the vertex list inverts the surface direction.

### Inputs

Mesh
Input geometry.

Selection
Boolean: true = flip, false = leave unchanged.

### Output

Mesh
Output geometry.

[Related references](INDEX.md).
