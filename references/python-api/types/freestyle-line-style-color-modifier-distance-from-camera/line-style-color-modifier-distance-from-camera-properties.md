# bpy.types.LineStyleColorModifier_DistanceFromCamera: properties

## LineStyleColorModifier_DistanceFromCamera(LineStyleColorModifier)

### LineStyleColorModifier_DistanceFromCamera(LineStyleColorModifier) 

base classes: bpy_struct, LineStyleModifier, LineStyleColorModifier
class bpy.types. LineStyleColorModifier_DistanceFromCamera ( LineStyleColorModifier ) 

Varies line color according to how far the geometry sits from the camera
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
range_max 

Top of the input range over which the mapping operates (in [-inf, inf], default 0.0)

Type :

float
range_min 

Bottom of the input range over which the mapping operates (in [-inf, inf], default 0.0)

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
