# bpy.types.CastModifier: properties

## CastModifier(Modifier)

### CastModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. CastModifier ( Modifier )

Modifier that distorts mesh into other geometries
cast_type

Target geometry (default 'SPHERE' )

Type :

Literal['SPHERE', 'CYLINDER', 'CUBOID']
factor

(in [-inf, inf], default 0.5)

Type :

float
invert_vertex_group

Negate the effect of the vertex group (default False)

Type :

bool
object

Control object; its location determines the effect center

Type :

Object
radius

Deformation range from effect center, 0 = unlimited (in [0, inf], default 0.0)

Type :

float
size

Shape size, 0 = computed automatically (in [0, inf], default 0.0)

Type :

float
use_radius_as_size

Apply radius as shape size (0 = auto) (default True)

Type :

bool
use_transform

Respect object transform for shape control (default False)

Type :

bool
use_x

(default True)

Type :

bool
use_y

(default True)

Type :

bool
use_z

(default True)

Type :

bool
vertex_group

Vertex group name (default "", never None)

Type :

str

[Related references](INDEX.md).
