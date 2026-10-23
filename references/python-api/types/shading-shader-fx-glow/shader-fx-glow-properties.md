# bpy.types.ShaderFxGlow: properties

## ShaderFxGlow(ShaderFx)

### ShaderFxGlow(ShaderFx)

base classes: bpy_struct, ShaderFx
class bpy.types. ShaderFxGlow ( ShaderFx )

Glow effect
blend_mode

Which blend mode applies (default 'REGULAR' )

Type :

Literal[‘REGULAR’, ‘ADD’, ‘SUBTRACT’, ‘MULTIPLY’, ‘DIVIDE’]
glow_color

The color the generated glow uses (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
mode

Which glow mode is active (default 'LUMINANCE' )

Type :

Literal[‘LUMINANCE’, ‘COLOR’]
opacity

How opaque the effect is (in [0, 1], default 0.0)

Type :

float
rotation

How much the effect is turned (in [-inf, inf], default 0.0)

Type :

float
samples

Sample count for the blur (in [1, 32], default 4)

Type :

int
select_color

The color picked out to receive the glow (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
size

How large the effect is (array of 2 items, in [0, inf], default (0.0, 0.0))

Type :

mathutils.Vector
threshold

Cutoff for picking the color that glows (in [0, 1], default 0.0)

Type :

float
use_glow_under

Glow only where alpha is present, which the Regular blend mode does not support (default False)

Type :

bool

[Related references](INDEX.md).
