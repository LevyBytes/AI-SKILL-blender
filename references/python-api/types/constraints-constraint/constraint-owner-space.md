# bpy.types.Constraint: owner_space

owner_space

Coordinate space in which the owner is evaluated (default 'WORLD' )

- WORLD
World Space – The constraint is applied relative to the world coordinate system.

- CUSTOM
Custom Space – The constraint is applied in local space of a custom object/bone/vertex group.

- POSE
Pose Space – The constraint is applied in Pose Space, the object transformation is ignored.

- `LOCAL_WITH_PARENT`
Local With Parent – The constraint is applied relative to the rest pose local coordinate system of the bone, thus including the parent-induced transformation.

- LOCAL
Local Space – The constraint is applied relative to the local coordinate system of the object.

Type :

Literal[‘WORLD’, ‘CUSTOM’, ‘POSE’, ‘`LOCAL_WITH_PARENT`’, ‘LOCAL’]

[Related references](INDEX.md).
