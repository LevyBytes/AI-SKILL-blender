# bpy.types.SplinePoint: properties

## SplinePoint(bpy_struct)

### SplinePoint(bpy_struct)

base class — bpy_struct
class bpy.types. SplinePoint ( bpy_struct )

A spline point that carries no handles
co

Coordinates of the point (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Vector
hide

Whether the point is visible (default False)

Type :

bool
radius

Radius used when beveling (in [0, inf], default 0.0)

Type :

float
select

Whether the point is selected (default False)

Type :

bool
tilt

Tilt as seen in the 3D View (in [-376.991, 376.991], default 0.0)

Type :

float
weight

Weight for NURBS (in [-inf, inf], default 0.0)

Type :

float
weight_softbody

Goal weight for softbody (in [0.01, 100], default 0.0)

Type :

float

[Related references](INDEX.md).
