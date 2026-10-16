# Set Mesh Normal Node

## Set Mesh Normal Node

Set Mesh Normal Node

Stores a normal vector for each mesh element, controlling shading and influencing operations that use surface normals.

Inputs
Mesh: Standard geometry input.
Remove Custom Sharpness: If enabled, removes any existing custom normals or sharpness data. (Sharpness mode)
Edge Sharpness: Boolean field defining whether an edge is marked sharp. True = sharp edges, false = smooth shading. (Sharpness mode)
Face Sharpness: Boolean field defining whether a face is marked flat. True = flat-shaded faces, false = smooth shading. (Sharpness mode)
Custom Normal: The vector to store as the custom normal. (Free mode, Tangent Space mode)

Properties
Mode: Storage mode for custom normal data.
  Sharpness: Store face or edge sharpness, like "Shade Smooth" and "Shade Flat" operators.
  Free: Keep custom normals as plain vectors expressed in the mesh's local space. Fast, but offers no deformation support.
  Tangent Space: Store normals in a deformation-aware transformation space. Slower but handles mesh changes better.
Domain (Free mode): Where to store free custom normals.
  Point: Per-vertex normals.
  Face: Per-face normals.
  Face Corner: Per-corner normals. Needed to bake mixed sharp and smooth edges into custom vectors.

Outputs
Mesh: Standard geometry output.

[Related references](INDEX.md).
