# bpy.types.Bone: bbone_handle_type_start

bbone_handle_type_start

Chooses the method for deriving the B-Bone's start handle (default 'AUTO')

- AUTO
Automatic – Use connected parent and children to compute the handle.

- ABSOLUTE
Absolute – Use the position of the specified bone to compute the handle.

- RELATIVE
Relative – Use the offset of the specified bone from rest pose to compute the handle.

- TANGENT
Tangent – Use the orientation of the specified bone to compute the handle, ignoring the location.

Type:
Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT']

[Related references](INDEX.md).
