# bpy.types.EditBone: bbone_handle_type_end

bbone_handle_type_end

How the B-Bone’s end handle is worked out (default 'AUTO' )

- AUTO
Automatic – Derive the handle from the connected parent and children.

- ABSOLUTE
Absolute – Derive the handle from the named bone’s position.

- RELATIVE
Relative – Derive the handle from how far the named bone sits from its rest pose.

- TANGENT
Tangent – Derive the handle from the named bone’s orientation, leaving its location out.

Type :

Literal[‘AUTO’, ‘ABSOLUTE’, ‘RELATIVE’, ‘TANGENT’]

[Related references](INDEX.md).
