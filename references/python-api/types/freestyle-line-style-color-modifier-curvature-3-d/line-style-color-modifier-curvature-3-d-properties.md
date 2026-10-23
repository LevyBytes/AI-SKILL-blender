# bpy.types.LineStyleColorModifier_Curvature_3D: properties

## LineStyleColorModifier_Curvature_3D(LineStyleColorModifier)

### LineStyleColorModifier_Curvature_3D(LineStyleColorModifier) 

base classes: bpy_struct, LineStyleModifier, LineStyleColorModifier
class bpy.types. LineStyleColorModifier_Curvature_3D ( LineStyleColorModifier ) 

Varies line color from the radial curvature measured on 3D mesh surfaces
blend 

How this modifier's output is combined with the underlying base value (default 'MIX' )

Type :

Literal[Ramp Blend Items]
color_ramp 

The color ramp that remaps the line color (readonly)

Type :

ColorRamp
curvature_max 

Maximum Curvature (in [-inf, inf], default 0.0)

Type :

float
curvature_min 

Minimum Curvature (in [-inf, inf], default 0.0)

Type :

float
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
