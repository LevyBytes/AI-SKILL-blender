# Triangulate Modifier

## Triangulate Modifier

### Triangulate Modifier

Apply the Triangulate modifier and each face of a mesh, whether a quad or an n-gon, gets cut into triangles. The result is identical to running the Triangulate tool from within Edit Mode.

| Description | Description |
| --- | --- |
| Mesh before Triangulate modifier. | Mesh after Triangulate modifier. |

### Options

The Triangulate modifier.

Quad Method

Beauty
Cuts the quads into tidy triangles; this is the slower route.

Fixed
Divides each quad across its 1st and 3rd vertices.

Fixed Alternate
Divides each quad across its 2nd and 4th vertices.

Shortest Diagonal
Cuts each quad along whichever diagonal is shorter.

Longest Diagonal
Cuts each quad along whichever diagonal is longer. For cloth simulations this is the mode to reach for.

N-gon Method

Beauty
Lays out the resulting triangles neatly; this is the slower route.

Clip
Breaks n-gons apart with an ear-clipping algorithm
(the same tessellation used to draw them in the viewport).

Minimum Vertices
The fewest vertices a face needs before it qualifies for triangulation.
Set it to 5, for instance, and quads are left alone
while only n-gons get triangulated.

[Related references](INDEX.md).
