# bpy.types.FollowPathConstraint: properties

## FollowPathConstraint(Constraint)

### FollowPathConstraint(Constraint)

base classes — bpy_struct, Constraint
class bpy.types. FollowPathConstraint ( Constraint )

Pins an object's motion to follow the target path.
forward_axis

Axis that points forward along the path (default '`FORWARD_X`' )

Type :

Literal[‘`FORWARD_X`’, ‘`FORWARD_Y`’, ‘`FORWARD_Z`’, ‘`TRACK_NEGATIVE_X`’, ‘`TRACK_NEGATIVE_Y`’, ‘`TRACK_NEGATIVE_Z`’]
offset

Shift away from the position that matches the current time frame (in [-1.04857e+06, 1.04857e+06], default 0.0)

Type :

float
offset_factor

Percentage that places the target somewhere along the curve's length (in [-inf, inf], default 0.0)

Type :

float
target

Target Curve object

Type :

Object
up_axis

Axis that points upward (default '`UP_X`' )

Type :

Literal[‘`UP_X`’, ‘`UP_Y`’, ‘`UP_Z`’]
use_curve_follow

Object will follow the heading and banking of the curve (default False)

Type :

bool
use_curve_radius

Object is scaled by the curve radius (default False)

Type :

bool
use_fixed_location

Keep the object locked to one fixed point along the curve's length no matter the time (default False)

Type :

bool

[Related references](INDEX.md).
