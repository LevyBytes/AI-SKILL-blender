# bpy.types.LineStyleColorModifier_CreaseAngle: properties

## LineStyleColorModifier_CreaseAngle(LineStyleColorModifier)

### LineStyleColorModifier_CreaseAngle(LineStyleColorModifier) 

base classes — bpy_struct, LineStyleModifier, LineStyleColorModifier
class bpy.types. LineStyleColorModifier_CreaseAngle ( LineStyleColorModifier ) 

Varies line color according to the crease angle beneath it
angle_max 

Upper angle bound for adjusting thickness (in [-inf, inf], default 0.0)

Type :

float
angle_min 

Lower angle bound for adjusting thickness (in [-inf, inf], default 0.0)

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
type 

Which kind of modifier this is (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Color Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool

[Related references](INDEX.md).
