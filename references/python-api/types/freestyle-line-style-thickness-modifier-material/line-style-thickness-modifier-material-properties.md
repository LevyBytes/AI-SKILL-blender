# bpy.types.LineStyleThicknessModifier_Material: properties

## LineStyleThicknessModifier_Material(LineStyleThicknessModifier)

### LineStyleThicknessModifier_Material(LineStyleThicknessModifier)

base classes — bpy_struct, LineStyleModifier, LineStyleThicknessModifier
class bpy.types. LineStyleThicknessModifier_Material ( LineStyleThicknessModifier )

Drives line width from a selected material attribute.
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
material_attribute

Pick which attribute of the material feeds the modifier (default 'LINE' )

Type :

Literal[‘LINE’, ‘`LINE_R`’, ‘`LINE_G`’, ‘`LINE_B`’, ‘`LINE_A`’, ‘DIFF’, ‘`DIFF_R`’, ‘`DIFF_G`’, ‘`DIFF_B`’, ‘SPEC’, ‘`SPEC_R`’, ‘`SPEC_G`’, ‘`SPEC_B`’, ‘`SPEC_HARD`’, ‘ALPHA’]
type

The modifier's kind (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Thickness Modifier Type Items]
use

Turn this modifier on or off while strokes are rendered (default False)

Type :

bool
value_max

Highest value the mapping can output (in [-inf, inf], default 0.0)

Type :

float
value_min

Lowest value the mapping can output (in [-inf, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
