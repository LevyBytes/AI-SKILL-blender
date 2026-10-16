# bpy.types.LineStyleGeometryModifier_2DTransform: properties

## LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier)

### LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier) 

base classes — bpy_struct, LineStyleModifier, LineStyleGeometryModifier
class bpy.types. LineStyleGeometryModifier_2DTransform ( LineStyleGeometryModifier ) 

Scale and rotate the stroke backbone geometry within two dimensions
angle 

Rotation angle (in [-inf, inf], default 0.0)

Type :

float
expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
pivot 

Point around which scaling and rotation are performed (default 'CENTER' )

Type :

Literal[‘CENTER’, ‘START’, ‘END’, ‘PARAM’, ‘ABSOLUTE’]
pivot_u 

Pivot given as the stroke-point parameter u, where 0 <= u <= 1 (in [0, 1], default 0.0)

Type :

float
pivot_x 

X coordinate of the absolute pivot in 2D (in [-inf, inf], default 0.0)

Type :

float
pivot_y 

Y coordinate of the absolute pivot in 2D (in [-inf, inf], default 0.0)

Type :

float
scale_x 

Scaling factor along the X axis (in [-inf, inf], default 0.0)

Type :

float
scale_y 

Scaling factor along the Y axis (in [-inf, inf], default 0.0)

Type :

float
type 

Which kind of modifier this is (default '2`D_OFFSET`' , readonly)

Type :

Literal[Linestyle Geometry Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool

[Related references](INDEX.md).
