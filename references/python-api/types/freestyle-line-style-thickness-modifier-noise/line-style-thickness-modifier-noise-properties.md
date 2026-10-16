# bpy.types.LineStyleThicknessModifier_Noise: properties

## LineStyleThicknessModifier_Noise(LineStyleThicknessModifier)

### LineStyleThicknessModifier_Noise(LineStyleThicknessModifier)

base classes — bpy_struct, LineStyleModifier, LineStyleThicknessModifier
class bpy.types. LineStyleThicknessModifier_Noise ( LineStyleThicknessModifier )

Drives line width from a random noise signal.
amplitude

Strength of the noise signal (in [-inf, inf], default 0.0)

Type :

float
blend

Sets the way this modifier's output is combined with the underlying base value (default 'MIX' )

Type :

Literal[‘MIX’, ‘ADD’, ‘SUBTRACT’, ‘MULTIPLY’, ‘DIVIDE’, ‘DIFFERENCE’, ‘MINIMUM’, ‘MAXIMUM’]
expanded

True when the modifier's tab is shown unfolded (default False)

Type :

bool
influence

Weight that scales how strongly the modifier alters the property (in [0, 1], default 0.0)

Type :

float
period

Wavelength over which the noise repeats (in [-inf, inf], default 0.0)

Type :

float
seed

Seed value feeding the noise generator (in [1, 32767], default 0)

Type :

int
type

The modifier's kind (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Thickness Modifier Type Items]
use

Turn this modifier on or off while strokes are rendered (default False)

Type :

bool
use_asymmetric

Permit width to be applied unevenly to either side (default False)

Type :

bool

[Related references](INDEX.md).
