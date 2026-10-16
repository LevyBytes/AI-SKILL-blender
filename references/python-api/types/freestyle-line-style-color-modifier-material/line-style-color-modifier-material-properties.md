# bpy.types.LineStyleColorModifier_Material: properties

## LineStyleColorModifier_Material(LineStyleColorModifier)

### LineStyleColorModifier_Material(LineStyleColorModifier) 

base classes — bpy_struct, LineStyleModifier, LineStyleColorModifier
class bpy.types. LineStyleColorModifier_Material ( LineStyleColorModifier ) 

Varies line color from a chosen material attribute
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
material_attribute 

Pick which attribute of the material drives the result (default 'LINE' )

Type :

Literal[‘LINE’, ‘`LINE_R`’, ‘`LINE_G`’, ‘`LINE_B`’, ‘`LINE_A`’, ‘DIFF’, ‘`DIFF_R`’, ‘`DIFF_G`’, ‘`DIFF_B`’, ‘SPEC’, ‘`SPEC_R`’, ‘`SPEC_G`’, ‘`SPEC_B`’, ‘`SPEC_HARD`’, ‘ALPHA’]
type 

Which kind of modifier this is (default '`ALONG_STROKE`' , readonly)

Type :

Literal[Linestyle Color Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool
use_ramp 

Run the BW average through a color ramp to obtain an RGB color (default False)

Type :

bool

[Related references](INDEX.md).
