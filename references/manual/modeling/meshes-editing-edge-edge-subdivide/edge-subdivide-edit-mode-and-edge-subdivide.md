# Subdivide: Edit Mode, Edge ‣ Subdivide

## Subdivide

### Subdivide 

Reference

Mode :

Edit Mode

Menu :

Edge ‣ Subdivide

Boosts mesh resolution by chopping faces or edges into smaller pieces.

What happens depends on the selection, following a handful of rules:

- With just one edge of a triangle or quad selected, that face becomes a quad or N-gon
respectively. Disable Create N-Gons and the face splits into triangles instead.

- With two edges of a face selected:

- On a triangle, a fresh edge joins the two new vertices, breaking the triangle into a triangle
and a quad.

- On a quad whose selected edges are neighbors, the split follows the Quad Corner Type setting
(see below).

- On a quad whose selected edges are opposite, an edge connecting the two new vertices simply
divides it into two quads.

- With three edges of a face selected:

- On a triangle, the whole face is effectively selected, so it splits into four smaller
triangles.

- On a quad, the two opposite edges subdivide as above first; then the "middle" edge subdivides,
treating its new "sub-quad" the way a single-edge case is treated.

- With all four edges of a quad selected, the face splits into four smaller quads.

- With one or more edges of an N-gon selected, those edges subdivide individually while the
face itself stays whole.

[Related references](INDEX.md).
