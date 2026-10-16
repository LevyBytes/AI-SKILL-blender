# bpy.types.LineStyleColorModifier_Noise: properties

## LineStyleColorModifier_Noise(LineStyleColorModifier)

### LineStyleColorModifier_Noise(LineStyleColorModifier) 

base classes — bpy_struct, LineStyleModifier, LineStyleColorModifier
class bpy.types. LineStyleColorModifier_Noise ( LineStyleColorModifier ) 

Varies line color from a random noise signal
amplitude 

Amplitude of the noise (in [-inf, inf], default 0.0)

Type :

float
blend 

How this modifier's output is combined with the underlying base value (default 'MIX' )

Type :

Literal[Ramp Blend Items]
color_ramp 

The color ramp that remaps the line color (readonly)

Type :

ColorRamp
expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
influence 

How strongly this modifier shifts the affected property, weighting its contribution (in [0, 1], default 0.0)

Type :

float
period 

Period of the noise (in [-inf, inf], default 0.0)

Type :

float
seed 

Seed for the noise generation (in [1, 32767], default 0)

Type :

int
type 

Which kind of modifier this is (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Color Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool

[Related references](INDEX.md).
