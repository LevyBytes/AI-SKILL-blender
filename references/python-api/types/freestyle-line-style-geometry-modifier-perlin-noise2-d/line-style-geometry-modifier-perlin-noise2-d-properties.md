# bpy.types.LineStyleGeometryModifier_PerlinNoise2D: properties

## LineStyleGeometryModifier_PerlinNoise2D(LineStyleGeometryModifier)

### LineStyleGeometryModifier_PerlinNoise2D(LineStyleGeometryModifier) 

base classes: bpy_struct, LineStyleModifier, LineStyleGeometryModifier
class bpy.types. LineStyleGeometryModifier_PerlinNoise2D ( LineStyleGeometryModifier ) 

Apply two-dimensional Perlin noise to the stroke backbone geometry
amplitude 

Amplitude of the Perlin noise (in [-inf, inf], default 0.0)

Type :

float
angle 

Displacement direction (in [-inf, inf], default 0.0)

Type :

float
expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
frequency 

Frequency of the Perlin noise (in [-inf, inf], default 0.0)

Type :

float
octaves 

Octave count, which sets how much Perlin-noise detail is present (in [0, inf], default 0)

Type :

int
seed 

Seed for the random number generator; a negative value falls back to using time (in [-inf, inf], default 0)

Type :

int
type 

Which kind of modifier this is (default '2`D_OFFSET`' , readonly)

Type :

Literal[Linestyle Geometry Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool

[Related references](INDEX.md).
