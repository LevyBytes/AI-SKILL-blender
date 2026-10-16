# bpy.types.LineStyleThicknessModifier_DistanceFromCamera: properties

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
range_max

Top of the input range over which the mapping operates (in [-inf, inf], default 0.0)

Type :

float
range_min

Bottom of the input range over which the mapping operates (in [-inf, inf], default 0.0)

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
value_max

Highest value the mapping can output (in [-inf, inf], default 0.0)

Type :

float
value_min

Lowest value the mapping can output (in [-inf, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
