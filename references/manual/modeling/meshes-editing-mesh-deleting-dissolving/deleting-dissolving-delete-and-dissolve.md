# Deleting & Dissolving: Delete, Dissolve, Dissolve Vertices

## Deleting & Dissolving

### Deleting & Dissolving 

### Delete 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Delete

Shortcut :

X or Delete

Removes the selected mesh elements. The menu offers:

Vertices
Removes the selected vertices, plus every edge and face they belong to.

Edges
Removes the selected edges, plus any faces they belong to. Stranded vertices go too.

Faces
Removes the selected faces. Stranded vertices and edges go too.

Only Edges & Faces
Removes the selected edges and faces, plus any unselected face holding a selected edge. Stranded
vertices stay put.

Only Faces
Removes the selected faces. Stranded vertices and edges stay put.

### Dissolve 

Where deleting leaves a hole, dissolving instead keeps the surface sealed.

### Dissolve Vertices 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Delete ‣ Dissolve Vertices

Shortcut :

X , Delete , or Ctrl - X

Removes each selected vertex and fuses its surrounding faces into a single one. (N-gons often
result.)

Should a vertex belong to a wire — a chain of edges in no face — its surrounding edges merge
instead.

The Adjust Last Operation panel offers the following options:

Face Split
Where possible, splits surrounding faces so only a corner triangle merges rather than the whole
face. This shrinks the final "hole-filling" faces and evens them out.

Tear Boundaries
At the mesh boundary, deletes faces rather than merging them. Such faces always split, even with
Face Split off.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Original mesh  | Face Split: Off  Tear Boundaries: Off | Face Split: On  Tear Boundaries: Off | Face Split: On/Off  Tear Boundaries: On |

[Related references](INDEX.md).
