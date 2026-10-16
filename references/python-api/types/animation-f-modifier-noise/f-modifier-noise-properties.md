# bpy.types.FModifierNoise: properties

## FModifierNoise(FModifier)

### FModifierNoise(FModifier)

base classes — bpy_struct, FModifier
class bpy.types. FModifierNoise ( FModifier )

Adds randomness to the F-Curve it modifies.
blend_type

How the noise is combined with the existing F-Curve (default 'REPLACE' )

Type :

Literal[‘REPLACE’, ‘ADD’, ‘SUBTRACT’, ‘MULTIPLY’]
depth

How much fine-grained detail the noise carries (in [0, 32767], default 0)

Type :

int
lacunarity

Spacing between successive frequencies. Depth must exceed 0 for this to matter. (in [-inf, inf], default 2.0)

Type :

float
offset

Shift in time applied to the noise (in [-inf, inf], default 0.0)

Type :

float
phase

Random seed driving the noise (in [-inf, inf], default 1.0)

Type :

float
roughness

How much high-frequency detail appears. Depth must exceed 0 for this to matter. (in [-inf, inf], default 0.5)

Type :

float
scale

How the noise is stretched along the time axis (in [-inf, inf], default 1.0)

Type :

float
strength

Noise amplitude, i.e. how far it shifts the underlying curve (in [-inf, inf], default 1.0)

Type :

float
use_legacy_noise

Generate noise the old way, which has the drawback of sometimes producing values beyond the -1/1 range (default False)

Type :

bool

[Related references](INDEX.md).
