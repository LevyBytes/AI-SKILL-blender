# Bounding Box Node

## Bounding Box Node

Bounding Box Node

Creates the smallest box mesh encapsulating the input geometry and outputs bounding corner coordinates.

The mesh and Min/Max outputs ignore instances; instead, each instance receives its own bounding box. For instance-inclusive bounds, use Realize Instances Node.

Inputs:
Geometry: Standard geometry input.
Use Radius: When enabled, incorporates the radius attribute during bound computation for curves, point clouds, and Grease Pencil data.

Outputs:
Bounding Box: Encapsulating box mesh.
Min: Box corner at negative X, Y, Z extents.
Max: Box corner at positive X, Y, Z extents.

Examples:
Box encapsulating the monkey mesh via Bounding Box node.

[Related references](INDEX.md).
