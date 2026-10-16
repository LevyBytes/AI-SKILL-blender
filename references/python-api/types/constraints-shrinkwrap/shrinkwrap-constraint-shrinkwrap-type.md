# bpy.types.ShrinkwrapConstraint: shrinkwrap_type

shrinkwrap_type

Picks which shrinkwrap algorithm finds the target position (default '`NEAREST_SURFACE`' )

- `NEAREST_SURFACE`
Nearest Surface Point – Pull the point onto the closest spot on the target surface.

- PROJECT
Project – Pull the point onto the target surface measured along a chosen axis.

- `NEAREST_VERTEX`
Nearest Vertex – Pull the point onto the target's closest vertex.

- `TARGET_PROJECT`
Target Normal Project – Pull the point onto the target surface following the target's interpolated vertex normals.

Type :

Literal[‘`NEAREST_SURFACE`’, ‘PROJECT’, ‘`NEAREST_VERTEX`’, ‘`TARGET_PROJECT`’]

[Related references](INDEX.md).
