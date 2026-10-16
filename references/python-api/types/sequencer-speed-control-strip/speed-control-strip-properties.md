# bpy.types.SpeedControlStrip: properties

## SpeedControlStrip(EffectStrip)

### SpeedControlStrip(EffectStrip)

base classes — bpy_struct, Strip, EffectStrip
class bpy.types. SpeedControlStrip ( EffectStrip )

Strip used to govern how fast other strips play
input_1

The effect strip's first input (never None)

Type :

Strip
input_count

(in [0, inf], default 0, readonly)

Type :

int
speed_control

Which method controls the speed (default 'STRETCH' )

- STRETCH
Stretch – Change the input's playback speed so its length matches the strip.

- MULTIPLY
Multiply – Scale the speed by the speed factor.

- `FRAME_NUMBER`
Frame Number – A frame number within the input strip.

- LENGTH
Length – A percentage of the input strip's length.

Type :

Literal[‘STRETCH’, ‘MULTIPLY’, ‘`FRAME_NUMBER`’, ‘LENGTH’]
speed_factor

Scale the strip's present speed by this number, or remap the current frame onto this frame (in [-inf, inf], default 0.0)

Type :

float
speed_frame_number

A frame number within the input strip (in [-inf, inf], default 0.0)

Type :

float
speed_length

A percentage of the input strip's length (in [-inf, inf], default 0.0)

Type :

float
use_frame_interpolate

Crossfade-blend the current frame into the next one (default False)

Type :

bool

[Related references](INDEX.md).
