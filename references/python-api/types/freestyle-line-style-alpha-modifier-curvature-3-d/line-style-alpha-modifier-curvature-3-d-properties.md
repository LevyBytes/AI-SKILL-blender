# bpy.types.LineStyleAlphaModifier_Curvature_3D: properties

## LineStyleAlphaModifier_Curvature_3D(LineStyleAlphaModifier)

### LineStyleAlphaModifier_Curvature_3D(LineStyleAlphaModifier) 

base classes — bpy_struct, LineStyleModifier, LineStyleAlphaModifier
class bpy.types. LineStyleAlphaModifier_Curvature_3D ( LineStyleAlphaModifier ) 

Drives alpha transparency from the radial curvature measured on 3D mesh surfaces
blend 

How this modifier's output is combined with the underlying base value (default 'MIX' )

Type :

Literal[‘MIX’, ‘ADD’, ‘SUBTRACT’, ‘MULTIPLY’, ‘DIVIDE’, ‘DIFFERENCE’, ‘MINIMUM’, ‘MAXIMUM’]
curvature_max 

Maximum Curvature (in [0, 10000], default 0.0)

Type :

float
curvature_min 

Minimum Curvature (in [0, 10000], default 0.0)

Type :

float
curve 

The curve that drives the curve-based mapping (readonly)

Type :

CurveMapping
expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
influence 

How strongly this modifier shifts the affected property, weighting its contribution (in [0, 1], default 0.0)

Type :

float
invert 

Flip the direction in which the linear mapping fades out (default False)

Type :

bool
mapping 

Choose which mapping kind applies (default 'LINEAR' )

- LINEAR
Linear – Use linear mapping.

- CURVE
Curve – Use curve mapping.

Type :

Literal[‘LINEAR’, ‘CURVE’]
type 

Which kind of modifier this is (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Alpha Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool

[Related references](INDEX.md).
