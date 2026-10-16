# Select All by Trait: Non Manifold, Options, Loose Geometry, Interior Faces, Faces by Sides

## Select All by Trait

### Select All by Trait

### Non Manifold

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select All by Trait ‣ Non Manifold

Selects a mesh's non-manifold geometry. Only the Vertex and Edge selection modes offer this entry.

### Options

Extend
Adds to what's selected rather than replacing it.

Wire
Edges attached to no face.

Boundaries
Edges along boundaries and holes.

Multiple Faces
Edges shared by three or more faces.

Non Contiguous
Edges on exactly two faces whose normals oppose each other.

Vertices
Isolated vertices, those on a Wire or Multiple Faces edge, or the lone vertex bridging two faces.

### Loose Geometry

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select All by Trait ‣ Loose Geometry

According to the selection mode, this picks out vertices in no edge, edges in no face, or faces sharing an edge with no other face.

### Interior Faces

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select All by Trait ‣ Interior Faces

Catches faces that may have been created inside the mesh by accident rather than on its surface. To be exact, it grabs faces with "abnormal" neighbors (several neighbors meeting at one edge), plus the "normal" neighbors of those faces.

### Faces by Sides

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select All by Trait ‣ Faces by Sides

Picks every face with a given edge count, which you set in the Adjust Last Operation panel.

[Related references](INDEX.md).
