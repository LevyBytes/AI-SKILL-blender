# Mesh Primitives: Circle, UV Sphere, Icosphere

### Circle

Drops in a flat 2D ring of vertices that approximates a circle as a polygon. It's a handy launch point for cylindrical shapes, holes, pipe ends, or extrusion-driven modeling.

Vertices
How many vertices ring the circle; more of them, smoother the shape.

Fill Type
How the circle's interior is capped:

Triangle Fan :

Triangles meeting at a shared central vertex.

N-gon :

A single N-gon face.

Nothing :

No fill, just the rim vertices.

Radius
Center-to-rim distance.

### UV Sphere

Quad faces stacked into horizontal rings and vertical segments, capped by triangle fans at each pole, make up a UV sphere. The arrangement matches the usual way 2D textures get mapped (hence "UV"), so it textures cleanly.

Think latitude and longitude lines on a globe, which also makes it a fit for planetary models or any spherical shape needing pole-to-pole UV seams.

Segments
Count of vertical (longitudinal) divisions, the globe's meridians from pole to pole.

Rings
Count of horizontal (latitudinal) divisions, the globe's parallels stacked top to bottom.

Note

Rings map to face loops rather than edge loops, so you'll see one fewer edge loop than the ring count.

Radius
Center-to-surface distance.

Tip

For tidy shading, turn on Smooth Shading and add a Subdivision Surface modifier.

### Icosphere

Built entirely from equilateral triangles, an icosphere spreads its vertices more evenly than a UV sphere does, which suits sculpting, simulations, and anywhere uniform topology matters.

You get one by repeatedly subdividing an icosahedron, a 20-faced triangular polyhedron.

Subdivisions
Number of recursive subdivision steps. Each pass cuts every triangle into four, so resolution climbs exponentially.

- Level 1 gives you the bare icosahedron.

- Each level beyond that smooths the surface and adds vertices.

Warning

Vertex counts on an icosphere balloon fast. At 10 subdivisions, for instance, you'd top 5 million triangles and possibly crash Blender.

Radius
Center-to-surface distance.

Tip

Icospheres show up a lot in simulations, particle emitters, and sculpting, where even, triangle-only topology pays off.

[Related references](INDEX.md).
