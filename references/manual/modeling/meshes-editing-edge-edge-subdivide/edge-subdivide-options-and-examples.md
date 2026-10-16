# Subdivide: Options, Examples, One Edge, Two Tri Edges, Two Opposite Quad Edges

### Options 

These options are available in the Adjust Last Operation panel after
running the operator:

Number of Cuts
How many cuts to make per edge. The default of 1 halves each edge; 2 thirds it, and onward.

Smoothness
Nudges the subdivisions to approximate curvature, producing an effect akin to how the
Subdivision Surface Modifier might reshape the mesh.

| Description | Description | Description |
| --- | --- | --- |
| Mesh before subdividing.  | Subdivided with no smoothing.  | Subdivided with Smoothness set to 1.  |

Create N-Gons
Uncheck to force the result into triangles or quads rather than n-gons (see examples below).

Quad Corner Type
Governs how quads split when two neighboring edges are selected.

Inner Vertices
The selected edges subdivide; an edge then bridges the two new vertices to form a small triangle;
that edge subdivides as well, and its resulting "inner vertex" links by a further edge to the
vertex opposite the originally selected edges. The outcome is a triangle plus two quads.

Path
The selected edges subdivide, after which new edges connect the new vertices and the existing
outer vertices, giving two triangles and a quad.

Straight Cut
The selected edges subdivide, then an edge across the two new vertices forms a small triangle and
an N-gon. With Create N-Gons off, this behaves like Inner Vertices instead.

Fan
The quad splits into a fan made of one quad and two triangles, all sharing the vertex opposite
the selected edges.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Inner Vertices corner type.  | Path corner type.  | Straight Cut corner type.  | Fan corner type.  |

Fractal
Throws the vertices in random directions once the mesh has been subdivided.

| Description | Description | Description |
| --- | --- | --- |
| Plane before subdivision.  | Regular subdivision.  | Same mesh with fractal added.  |

Along Normal
Confines that vertex movement to the normals rather than random directions.

Along Normal set to 1. 

Random Seed
Swaps the seed feeding the Fractal noise, so each value yields a different outcome.

Same mesh with a different seed value. 

See also

Randomize randomly displaces vertices without
subdividing first.

### Examples 

Some scenarios illustrating edge subdivision appear below.

The sample mesh. 

### One Edge 

| Description | Description |
| --- | --- |
| One edge.  | Create N-Gons unchecked.  |

### Two Tri Edges 

| Description | Description |
| --- | --- |
| Two tri edges.  | Create N-Gons unchecked.  |

### Two Opposite Quad Edges 

| Description | Description |
| --- | --- |
| Two quad edges.  | Create N-Gons unchecked.  |

[Related references](INDEX.md).
