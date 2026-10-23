# bpy.types.WorldMistSettings: properties

## WorldMistSettings(bpy_struct)

### WorldMistSettings(bpy_struct) 

base class: bpy_struct
class bpy.types. WorldMistSettings ( bpy_struct ) 

Mist settings attached to a World data-block
depth 

The range across which mist gradually reaches full strength (in [0, inf], default 25.0)

Type :

float
falloff 

Curve that governs how the mist tapers off (default 'QUADRATIC' )

- QUADRATIC
Quadratic – Use quadratic progression.

- LINEAR
Linear – Use linear progression.

- `INVERSE_QUADRATIC`
Inverse Quadratic – Use inverse quadratic progression.

Type :

Literal[‘QUADRATIC’, ‘LINEAR’, ‘`INVERSE_QUADRATIC`’]
height 

Governs how quickly mist thins out as elevation rises (in [0, 100], default 0.0)

Type :

float
intensity 

Floor on the mist effect's overall strength (in [0, 1], default 0.0)

Type :

float
start 

Where the mist begins, measured outward from the camera (in [0, inf], default 5.0)

Type :

float
use_mist 

Hide distant objects behind the environment color as distance grows (default False)

Type :

bool

[Related references](INDEX.md).
