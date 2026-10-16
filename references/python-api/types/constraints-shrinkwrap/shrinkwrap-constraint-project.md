# bpy.types.ShrinkwrapConstraint: project_axis, project_axis_space, project_limit

project_axis

Axis constrain to (default '`POS_X`' )

Type :

Literal[Object Axis Items]
project_axis_space

Space for the projection axis (default 'WORLD' )

- WORLD
World Space – Evaluated against the world coordinate frame.

- CUSTOM
Custom Space – Evaluated in the local frame of a chosen object, bone, or vertex group.

- POSE
Pose Space – Evaluated in Pose Space, with the object transform left out.

- `LOCAL_WITH_PARENT`
Local With Parent – Evaluated against the bone's rest-pose local frame, so the parent's transform is folded in.

- LOCAL
Local Space – Evaluated against the object's own local frame.

Type :

Literal[‘WORLD’, ‘CUSTOM’, ‘POSE’, ‘`LOCAL_WITH_PARENT`’, ‘LOCAL’]
project_limit

Cap the distance allowed for projection (zero disables) (in [0, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
