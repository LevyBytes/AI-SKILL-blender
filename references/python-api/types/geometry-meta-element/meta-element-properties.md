# bpy.types.MetaElement: properties

## MetaElement(bpy_struct)

### MetaElement(bpy_struct)

base class: bpy_struct
class bpy.types. MetaElement ( bpy_struct )

One blobby component within a metaball data-block
co

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
hide

Hide element (default False)

Type :

bool
radius

(in [0, inf], default 0.0)

Type :

float
rotation

Normalized quaternion rotation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion
select

Select element (default False)

Type :

bool
size_x

Size of element, use of components depends on element type (in [0, 20], default 0.0)

Type :

float
size_y

Size of element, use of components depends on element type (in [0, 20], default 0.0)

Type :

float
size_z

Size of element, use of components depends on element type (in [0, 20], default 0.0)

Type :

float
stiffness

Stiffness defines how much of the element to fill (in [0, 10], default 0.0)

Type :

float
type

Metaball type (default 'BALL' )

Type :

Literal[Metaelem Type Items]
use_negative

Set metaball as negative one (default False)

Type :

bool
use_scale_stiffness

Scale stiffness instead of radius (default True)

Type :

bool

[Related references](INDEX.md).
