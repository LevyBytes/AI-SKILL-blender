# bpy.types.ShaderFxShadow: properties

amplitude

Height of the wave (in [0, inf], default 0.0)

Type :

float
blur

Pixel width used to soften the shadow, with 0 turning it off (array of 2 items, in [0, 32767], default (0, 0))

Type :

bpy_prop_array[int]
object

Object that sets where the rotation centers

Type :

Object
offset

How far the shadow is shifted (array of 2 items, in [-32768, 32767], default (0, 0))

Type :

bpy_prop_array[int]
orientation

Which way the wave travels (default 'HORIZONTAL' )

Type :

Literal[‘HORIZONTAL’, ‘VERTICAL’]
period

Length of one wave cycle (in [0, inf], default 0.0)

Type :

float
phase

Offset applied to the wave's phase (in [-inf, inf], default 0.0)

Type :

float
rotation

Turn applied around the center or the object (in [-6.28319, 6.28319], default 0.0)

Type :

float
samples

Sample count for the blur, where zero turns blurring off (in [0, 32], default 4)

Type :

int
scale

How large the shadow is drawn (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
shadow_color

The color applied to the shadow (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
use_object

Treat the object as the rotation center (default False)

Type :

bool
use_wave

Turn on the wave effect (default False)

Type :

bool

[Related references](INDEX.md).
