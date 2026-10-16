# bpy.types.Constraint: target_space

target_space

Coordinate space in which the target is evaluated (default 'WORLD' )

- WORLD
World Space – The transformation of the target is evaluated relative to the world coordinate system.

- CUSTOM
Custom Space – The transformation of the target is evaluated relative to a custom object/bone/vertex group.

- POSE
Pose Space – The transformation of the target is only evaluated in the Pose Space, the target armature object transformation is ignored.

- `LOCAL_WITH_PARENT`
Local With Parent – The transformation of the target bone is evaluated relative to its rest pose local coordinate system, thus including the parent-induced transformation.

- LOCAL
Local Space – The transformation of the target is evaluated relative to its local coordinate system.

- `LOCAL_OWNER_ORIENT`
Local Space (Owner Orientation) – The transformation of the target bone is evaluated relative to its local coordinate system, followed by a correction for the difference in target and owner rest pose orientations. When applied as local transform to the owner produces the same global motion as the target if the parents are still in rest pose..

Type :

Literal[‘WORLD’, ‘CUSTOM’, ‘POSE’, ‘`LOCAL_WITH_PARENT`’, ‘LOCAL’, ‘`LOCAL_OWNER_ORIENT`’]

[Related references](INDEX.md).
