# Subdivision Surface Node

## Subdivision Surface Node

### Subdivision Surface Node

Applies Catmull-Clark smoothing to mesh faces.

### Inputs

Mesh — Standard input.

Level — Subdivision count.

Edge Crease — Sharpness via weighted creases.

Vertex Crease — Vertex attractiveness (like edge creases per vertex).

Limit Surface — Positions vertices at infinite-subdivision limit (maximum smoothness).

UV Smooth — UV smoothing behavior.

None — No UV change.

Keep Corners — Islands smooth, boundaries fixed.

Keep Corners, Junctions — Islands smooth, discontinuous corners and tri-region nodes fixed.

Keep Corners, Junctions, Concave — Islands smooth, corners, junctions, darts, concave shapes fixed.

Keep Boundaries — Islands smooth, edges fixed.

All — Full smoothing.

Boundary Smooth — Open boundary treatment.

All — Smooth all boundaries and corners.

Keep Corners — Smooth edges, sharp corners.

### Outputs

Mesh — Standard output.

[Related references](INDEX.md).
