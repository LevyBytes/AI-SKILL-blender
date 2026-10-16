# bpy.types.ShapeKey: properties

data

(default None, readonly)

Type :

bpy_prop_collection[UnknownType]
frame

Frame for absolute keys (in [-inf, inf], default 0.0, readonly)

Type :

float
interpolation

Interpolation type for absolute shape keys (default '`KEY_LINEAR`' )

Type :

Literal[‘`KEY_LINEAR`’, ‘`KEY_CARDINAL`’, ‘`KEY_CATMULL_ROM`’, ‘`KEY_BSPLINE`’]
lock_shape

Guard the shape key against unintended sculpting and editing (default False)

Type :

bool
mute

Switch this shape key on or off (default False)

Type :

bool
name

Name of Shape Key (default “”, never None)

Type :

str
points

Fast path to shape-key point data through foreach_get/foreach_set. Warning: Does not support legacy Curve shape keys. (default None, readonly)

Type :

bpy_prop_collection[ShapeKeyPoint]
relative_key

Shape used as a relative key (never None)

Type :

ShapeKey
select

Shape key selection state (default False)

Type :

bool
slider_max

Maximum for slider (in [-10, 10], default 1.0)

Type :

float
slider_min

Minimum for slider (in [-10, 10], default 0.0)

Type :

float
value

Value of shape key at the current frame (in [0, 1], default 0.0)

Type :

float
vertex_group

Vertex weight group, to blend with basis shape (default “”, never None)

Type :

str

[Related references](INDEX.md).
