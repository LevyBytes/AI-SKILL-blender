# bpy.types.FluidEffectorSettings: properties

## FluidEffectorSettings(bpy_struct)

### FluidEffectorSettings(bpy_struct)

base class — bpy_struct
class bpy.types. FluidEffectorSettings ( bpy_struct )

Settings controlling how an object collides with smoke.
effector_type

Switch the role this effector plays in the simulation (default 'COLLISION' )

- COLLISION
Collision – Create collision object.

- GUIDE
Guide – Create guide object.

Type :

Literal[‘COLLISION’, ‘GUIDE’]
guide_mode

Sets the way guiding velocities are built (default 'OVERRIDE' )

- MAXIMUM
Maximize – Compare velocities from previous frame with new velocities from current frame and keep the maximum.

- MINIMUM
Minimize – Compare velocities from previous frame with new velocities from current frame and keep the minimum.

- OVERRIDE
Override – Always write new guide velocities for every frame (each frame only contains current velocities from guiding objects).

- AVERAGED
Averaged – Take average of velocities from previous frame and new velocities from current frame.

Type :

Literal[‘MAXIMUM’, ‘MINIMUM’, ‘OVERRIDE’, ‘AVERAGED’]
subframes

Extra samples taken between frames to sharpen the result for fast-moving effector objects (in [0, 200], default 0)

Type :

int
surface_distance

Extra band around the mesh surface still treated as effector (in [0, 10], default 0.0)

Type :

float
use_effector

Decide at which times the effector takes effect (default True)

Type :

bool
use_plane_init

Treat this object as a planar, unclosed mesh (default False)

Type :

bool
velocity_factor

Multiplier of obstacle velocity (in [-100, 100], default 1.0)

Type :

float

[Related references](INDEX.md).
