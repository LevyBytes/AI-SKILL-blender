# bpy.types.OperatorStrokeElement: properties

## OperatorStrokeElement(PropertyGroup)

### OperatorStrokeElement(PropertyGroup) 

base classes — bpy_struct, PropertyGroup
class bpy.types. OperatorStrokeElement ( PropertyGroup )
is_start 

(default False)

Type :

bool
location 

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
mouse 

(array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
mouse_event 

(array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
pressure 

Tablet pressure (in [0, 1], default 0.0)

Type :

float
size 

Brush size in screen space (in [0, inf], default 0.0)

Type :

float
time 

(in [0, inf], default 0.0)

Type :

float
x_tilt 

Pen tilt from left (-1.0) to right (+1.0) (in [-1, 1], default 0.0)

Type :

float
y_tilt 

Pen tilt from backward (-1.0) to forward (+1.0) (in [-1, 1], default 0.0)

Type :

float

[Related references](INDEX.md).
