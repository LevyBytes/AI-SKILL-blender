# bpy.types.CurveMapping: properties

## CurveMapping(bpy_struct)

### CurveMapping(bpy_struct)

base class: bpy_struct
class bpy.types. CurveMapping ( bpy_struct )

A curve, drawn by the user, that remaps color, vector, and scalar values onto new ones.
black_level

On RGB curves, which color black gets remapped to (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
clip_max_x

(in [-100, 100], default 0.0)

Type :

float
clip_max_y

(in [-100, 100], default 0.0)

Type :

float
clip_min_x

(in [-100, 100], default 0.0)

Type :

float
clip_min_y

(in [-100, 100], default 0.0)

Type :

float
curves

(default None, readonly)

Type :

bpy_prop_collection[CurveMap]
extend

Whether the curve is extrapolated past its ends or simply held flat (default 'HORIZONTAL' )

Type :

Literal['HORIZONTAL', 'EXTRAPOLATED']
tone

Tone of the curve (default 'STANDARD' )

- STANDARD
Standard – Run the combined curve on each channel by itself, which can shift the hue.

- FILMLIKE
Filmlike – Holds the hue steady.

Type :

Literal['STANDARD', 'FILMLIKE']
use_clip

Constrain the curve view so it stays inside a set boundary (default False)

Type :

bool
white_level

On RGB curves, which color white gets remapped to (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color

[Related references](INDEX.md).
