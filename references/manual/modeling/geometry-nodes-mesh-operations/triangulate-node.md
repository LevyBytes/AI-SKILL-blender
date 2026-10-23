# Triangulate Node

## Triangulate Node

### Triangulate Node

Converts all quads and n-gons to triangles; equivalent to Triangulate in Edit Mode.

### Inputs

Mesh: Standard input.

Selection: Boolean; which faces triangulate.

Quad Method

Beauty: Good triangles, slower.

Fixed: Diagonal through vertices 1 and 3.

Fixed Alternate: Diagonal through vertices 2 and 4.

Shortest Diagonal: Splits along shortest edge.

Longest Diagonal: Splits along longest edge (preferred for cloth).

N-gon Method

Beauty: Optimal triangles, slower.

Clip: Ear-clipping tessellation (viewport default).

### Outputs

Mesh: Standard output.

### Example

Before/after triangulation comparison.

[Related references](INDEX.md).
