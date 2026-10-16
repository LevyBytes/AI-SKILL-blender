# Cylinder Node

## Cylinder Node

The Cylinder node generates a cylinder mesh. It resembles the Cone node but always uses the same radius for the circles at the top and bottom.

Inputs:
Vertices — number of vertices on the circle at the top and bottom; no geometry is generated below three.
Side Segments — number of edges running vertically along the side; no geometry is generated below one.
Fill Segments — number of concentric rings used to fill the round top and bottom faces; no geometry is generated below one.
Radius — distance of the vertices from the Z axis; if zero, the output is a single line.
Depth — height of the cylinder.

Properties:
Fill Type — how the top and bottom circles are filled with faces when their radius is larger than zero.
- None: do not fill the circles.
- N-Gon: fill the innermost segment of the circles with a single face.
- Triangles: fill the innermost segment of the circles with triangles connected to a new vertex on the Z axis.

Outputs:
Mesh — standard geometry output.
Top — a boolean attribute field selecting the faces on the top of the cylinder; if Fill Type is None, this selects the top edges instead, and if Radius is zero, it selects the top point.
Side — a boolean attribute field selecting the faces on the side of the cylinder.
Bottom — the same as the Top selection output, but on the bottom side of the geometry.
UV Map — a 2D vector giving the default X/Y coordinates of the UV Map for the primitive's shape; connect it to the Store Named Attribute Node to use once the Geometry Nodes Modifier is applied. The UV map must be stored on the face corner in order to be accessed.

[Related references](INDEX.md).
