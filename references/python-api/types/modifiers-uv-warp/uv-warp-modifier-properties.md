# bpy.types.UVWarpModifier: properties

axis_u 

The pole axis used for rotation (default 'X' )

Type :

Literal[Axis Xyz Items]
axis_v 

The pole axis used for rotation (default 'Y' )

Type :

Literal[Axis Xyz Items]
bone_from 

The bone that sets the offset (default "", never None)

Type :

str
bone_to 

The bone that sets the offset (default "", never None)

Type :

str
center 

The pivot used for rotate/scale (array of 2 items, in [-inf, inf], default (0.5, 0.5))

Type :

bpy_prop_array[float]
invert_vertex_group 

Flip the vertex group's influence (default False)

Type :

bool
object_from 

The object that sets the offset

Type :

Object
object_to 

The object that sets the offset

Type :

Object
offset 

Two-dimensional offset applied by the warp (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

bpy_prop_array[float]
rotation 

Two-dimensional rotation applied by the warp (in [-inf, inf], default 0.0)

Type :

float
scale 

Two-dimensional scale applied by the warp (array of 2 items, in [-inf, inf], default (1.0, 1.0))

Type :

bpy_prop_array[float]
uv_layer 

UV map name (default "", never None)

Type :

str
vertex_group 

Vertex group name (default "", never None)

Type :

str

[Related references](INDEX.md).
