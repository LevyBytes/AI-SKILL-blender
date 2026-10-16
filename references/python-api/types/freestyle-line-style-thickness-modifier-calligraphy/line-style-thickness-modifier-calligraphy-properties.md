# bpy.types.LineStyleThicknessModifier_Calligraphy: properties

## LineStyleThicknessModifier_Calligraphy(LineStyleThicknessModifier)

### LineStyleThicknessModifier_Calligraphy(LineStyleThicknessModifier)

base classes — bpy_struct, LineStyleModifier, LineStyleThicknessModifier
class bpy.types. LineStyleThicknessModifier_Calligraphy ( LineStyleThicknessModifier )

Varies the stroke width so the result resembles strokes drawn with a calligraphy pen.
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
orientation

Angle defining the principal direction (in [-inf, inf], default 0.0)

Type :

float
thickness_max

Largest width applied along the principal direction (in [0, 10000], default 0.0)

Type :

float
thickness_min

Smallest width applied perpendicular to the principal direction (in [0, 10000], default 0.0)

Type :

float
type

The modifier's kind (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Thickness Modifier Type Items]
use

Turn this modifier on or off while strokes are rendered (default False)

Type :

bool

[Related references](INDEX.md).
