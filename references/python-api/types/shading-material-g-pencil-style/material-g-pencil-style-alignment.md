# bpy.types.MaterialGPencilStyle: alignment_mode, alignment_rotation

alignment_mode

Sets how Dots and Boxes line up with the drawing path and object rotation (default 'PATH' )

- PATH
Path – Follow stroke drawing path and object rotation.

- OBJECT
Object – Follow object rotation only.

- FIXED
Fixed – Do not follow drawing path or object rotation and keeps aligned with viewport.

Type :

Literal[‘PATH’, ‘OBJECT’, ‘FIXED’]
alignment_rotation

Extra rotation added to dots and square stroke textures. Takes effect only in texture shading mode. (in [-1.5708, 1.5708], default 0.0)

Type :

float

[Related references](INDEX.md).
