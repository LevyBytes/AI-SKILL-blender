# bpy.types.BezierSplinePoint: properties

## BezierSplinePoint(bpy_struct)

Spline anchor point with directional tangent handles for curve control.

base class — bpy_struct
class bpy.types. BezierSplinePoint ( bpy_struct )

Control point on a Bézier curve with attached tangent vector handles
co 

Location of the anchor point in 3D space (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
handle_left 

Position of the incoming tangent handle (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
handle_left_type 

Behavior mode for the incoming handle (default 'FREE' )

Type :

Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']
handle_right 

Position of the outgoing tangent handle (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
handle_right_type 

Behavior mode for the outgoing handle (default 'FREE' )

Type :

Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']
hide 

Whether the point is concealed (default False)

Type :

bool
radius 

Thickness value for extrusion along the curve (in [0, inf], default 0.0)

Type :

float
select_control_point 

Whether the anchor point is selected (default False)

Type :

bool
select_left_handle 

Whether the incoming handle is selected (default False)

Type :

bool
select_right_handle 

Whether the outgoing handle is selected (default False)

Type :

bool
tilt 

Rotational twisting along the curve direction (in [-376.991, 376.991], default 0.0)

Type :

float
weight_softbody 

Influence on softbody simulation (in [0.01, 100], default 0.0)

Type :

float

[Related references](INDEX.md).
