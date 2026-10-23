# bpy.types.MaskSpline: properties

## MaskSpline(bpy_struct)

### MaskSpline(bpy_struct)

base class: bpy_struct
class bpy.types. MaskSpline ( bpy_struct )

A single spline that helps define the mask's shape.
offset_mode

Which method computes the feather offset (default 'EVEN' )

- EVEN
Even – Calculate even feather offset.

- SMOOTH
Smooth – Calculate feather offset as a second curve.

Type :

Literal[‘EVEN’, ‘SMOOTH’]
points

Set of points (default None, readonly)

Type :

MaskSplinePoints[MaskSplinePoint]
use_cyclic

Close this spline into a loop (default False)

Type :

bool
use_fill

Fill this spline (default True)

Type :

bool
use_self_intersection_check

Stop the feather from crossing itself (default False)

Type :

bool
weight_interpolation

Interpolation mode used for the spline's weights (default 'LINEAR' )

Type :

Literal[‘LINEAR’, ‘EASE’]

[Related references](INDEX.md).
