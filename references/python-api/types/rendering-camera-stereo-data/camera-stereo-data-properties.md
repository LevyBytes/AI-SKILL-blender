# bpy.types.CameraStereoData: properties

## CameraStereoData(bpy_struct)

### CameraStereoData(bpy_struct)

base class — bpy_struct
class bpy.types. CameraStereoData ( bpy_struct )

Stereoscopic camera configuration
convergence_distance

Focal point distance (typically projector-to-screen gap) (in [1e-05, inf], default 1.95)

Type :

float
convergence_mode

(default 'OFFAXIS' )

- OFFAXIS
Off-Axis – Off-axis frustums converging in a plane.

- PARALLEL
Parallel – Parallel cameras with no convergence.

- TOE
Toe-in – Rotated cameras, looking at the same point at the convergence distance.

Type :

Literal['OFFAXIS', 'PARALLEL', 'TOE']
interocular_distance

Spacing between eyes; typically 1/30th of the stereo plane (in [0, inf], default 0.065)

Type :

float
pivot

(default 'LEFT' )

Type :

Literal['LEFT', 'RIGHT', 'CENTER']
pole_merge_angle_from

Angle where eye separation begins fading (in [0, 1.5708], default 1.0472)

Type :

float
pole_merge_angle_to

Angle where eye separation fully disappears (in [0, 1.5708], default 1.309)

Type :

float
use_pole_merge

Decrease eye separation at poles (in [-inf, inf], default False)

Type :

bool
use_spherical_stereo

Render via rotating camera around eye center (default False)

Type :

bool

[Related references](INDEX.md).
