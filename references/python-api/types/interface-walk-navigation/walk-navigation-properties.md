# bpy.types.WalkNavigation: properties

## WalkNavigation(bpy_struct)

### WalkNavigation(bpy_struct)

base class: bpy_struct
class bpy.types. WalkNavigation ( bpy_struct )

Settings for walk navigation.
jump_height

How high a jump can reach (in [0.1, 100], default 0.4)

Type :

float
mouse_speed

How responsive looking around feels; larger numbers make the mouse turn faster (in [0.01, 10], default 1.0)

Type :

float
teleport_time

Length of the time warp applied when teleporting during navigation (in [0, 10], default 0.2)

Type :

float
use_gravity

Walk under gravity, or move around freely (default False)

Type :

bool
use_mouse_reverse

Flip the mouse's vertical axis (default False)

Type :

bool
view_height

Eye height above the floor while walking (in [0, 1000], default 1.6)

Type :

float
walk_speed

Baseline speed used for both walking and flying (in [0.01, 100], default 2.5)

Type :

float
walk_speed_factor

Multiplier applied when the fast or slow modifier keys are held (in [0.01, 10], default 5.0)

Type :

float

[Related references](INDEX.md).
