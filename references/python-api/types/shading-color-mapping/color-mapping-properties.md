# bpy.types.ColorMapping: properties

## ColorMapping(bpy_struct)

### ColorMapping(bpy_struct)

base class — bpy_struct
class bpy.types. ColorMapping ( bpy_struct )

Settings controlling color mapping
blend_color

The color blended into the texture's output color (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
blend_factor

(in [-inf, inf], default 0.0)

Type :

float
blend_type

Which blend mode is used against the texture's output color (default 'MIX' )

Type :

Literal[‘MIX’, ‘DARKEN’, ‘MULTIPLY’, ‘LIGHTEN’, ‘SCREEN’, ‘ADD’, ‘OVERLAY’, ‘`SOFT_LIGHT`’, ‘`LINEAR_LIGHT`’, ‘DIFFERENCE’, ‘SUBTRACT’, ‘DIVIDE’, ‘HUE’, ‘SATURATION’, ‘COLOR’, ‘VALUE’]
brightness

Tune how bright the texture is (in [0, 2], default 0.0)

Type :

float
color_ramp

(readonly)

Type :

ColorRamp
contrast

Tune the texture's contrast (in [0, 5], default 0.0)

Type :

float
saturation

Tune how saturated the texture's colors are (in [0, 2], default 0.0)

Type :

float
use_color_ramp

Switch color ramp operations on or off (default False)

Type :

bool

[Related references](INDEX.md).
