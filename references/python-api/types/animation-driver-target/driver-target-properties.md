# bpy.types.DriverTarget: properties

bone_target

The PoseBone to treat as the target, by name (default “”, never None)

Type :

str
context_property

Which context-dependent data-block the property is read from (default '`ACTIVE_SCENE`' )

- `ACTIVE_SCENE`
Active Scene – The scene being evaluated right now.

- `ACTIVE_VIEW_LAYER`
Active View Layer – The view layer being evaluated right now.

Type :

Literal[‘`ACTIVE_SCENE`’, ‘`ACTIVE_VIEW_LAYER`’]
data_path

The RNA Path, relative to the ID-block, to the property in use (default “”, never None)

Type :

str
fallback_value

What to fall back on when the data path won’t resolve (in [-inf, inf], default 0.0)

Type :

float
id

The ID-block holding the property in question (set id_type first)

Type :

ID
id_type

Which kind of ID-block is allowed (default 'OBJECT' )

Type :

Literal[Id Type Items]
is_fallback_used

Reports that the latest variable evaluation fell back on the fallback value (default False, readonly)

Type :

bool
rotation_mode

How rotation channel values are worked out (default 'AUTO' )

Type :

Literal[Driver Target Rotation Mode Items]
transform_space

Which space the transforms are taken in (default '`WORLD_SPACE`' )

- `WORLD_SPACE`
World Space – Transforms fold in parenting/restpose and constraints.

- `TRANSFORM_SPACE`
Transform Space – Transforms leave out parenting/restpose and constraints.

- `LOCAL_SPACE`
Local Space – Transforms fold in constraints but leave out parenting/restpose.

Type :

Literal[‘`WORLD_SPACE`’, ‘`TRANSFORM_SPACE`’, ‘`LOCAL_SPACE`’]
transform_type

Which driver variable type this is (default '`LOC_X`' )

Type :

Literal[‘`LOC_X`’, ‘`LOC_Y`’, ‘`LOC_Z`’, ‘`ROT_X`’, ‘`ROT_Y`’, ‘`ROT_Z`’, ‘`ROT_W`’, ‘`SCALE_X`’, ‘`SCALE_Y`’, ‘`SCALE_Z`’, ‘`SCALE_AVG`’]
use_fallback_value

Fall back on the fallback value when the data path won’t resolve, rather than letting the driver fail to evaluate (default False)

Type :

bool

[Related references](INDEX.md).
