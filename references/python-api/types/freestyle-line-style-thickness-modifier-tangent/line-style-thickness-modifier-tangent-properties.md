# bpy.types.LineStyleThicknessModifier_Tangent: properties

## LineStyleThicknessModifier_Tangent(LineStyleThicknessModifier)

### LineStyleThicknessModifier_Tangent(LineStyleThicknessModifier)

base classes: bpy_struct, LineStyleModifier, LineStyleThicknessModifier
class bpy.types. LineStyleThicknessModifier_Tangent ( LineStyleThicknessModifier )

Sets line width from the stroke's running direction.
blend

Sets the way this modifier's output is combined with the underlying base value (default 'MIX' )

Type :

Literal[‘MIX’, ‘ADD’, ‘SUBTRACT’, ‘MULTIPLY’, ‘DIVIDE’, ‘DIFFERENCE’, ‘MINIMUM’, ‘MAXIMUM’]
curve

The curve that drives curve-based mapping (readonly)

Type :

CurveMapping
expanded

True when the modifier's tab is shown unfolded (default False)

Type :

bool
influence

Weight that scales how strongly the modifier alters the property (in [0, 1], default 0.0)

Type :

float
invert

Reverse the direction in which the linear mapping fades out (default False)

Type :

bool
mapping

Choose which mapping mode applies (default 'LINEAR' )

- LINEAR
Linear – Use linear mapping.

- CURVE
Curve – Use curve mapping.

Type :

Literal[‘LINEAR’, ‘CURVE’]
thickness_max

Largest width (in [0, 10000], default 0.0)

Type :

float
thickness_min

Smallest width (in [0, 10000], default 0.0)

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
