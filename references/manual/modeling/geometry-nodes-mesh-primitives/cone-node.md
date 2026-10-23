# Cone Node

## Cone Node

### Cone Node

Generates optionally truncated cone mesh.

### Inputs

Vertices: Top/bottom circle vertex count; minimum 3.

Side Segments: Vertical subdivisions; minimum 1.

Fill Segments: Concentric rings; minimum 1.

Radius Top: Top circle size. Zero = single point.

Radius Bottom: Bottom circle size. Zero = single point.

Depth: Height.

Note: Both radii zero produces a line.

### Properties

Fill Type: Circle fill behavior.

None: No fill.

N-Gon: Single face per circle.

Triangles: Triangle fan from center.

### Outputs

Mesh: Standard output.

Top - Selection: top faces (or edges if Fill Type=None, or vertex if Radius Top=0).

Side - Selection: side faces.

Bottom - Selection: bottom faces (or edges if Fill Type=None, or vertex if Radius Bottom=0).

UV Map: Default 2D coordinates. Connect to Store Named Attribute Node; UV data requires face-corner storage.

[Related references](INDEX.md).
