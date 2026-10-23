# bpy.types.LineStyleGeometryModifier_Blueprint: properties

## LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier)

### LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier) 

base classes: bpy_struct, LineStyleModifier, LineStyleGeometryModifier
class bpy.types. LineStyleGeometryModifier_Blueprint ( LineStyleGeometryModifier ) 

Generate a blueprint look from circular, elliptic, and square contour strokes
backbone_length 

Amount of backbone stretching (in [-inf, inf], default 0.0)

Type :

float
expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
random_backbone 

How much the backbone stretching is randomized (in [0, inf], default 0)

Type :

int
random_center 

How much the center is randomized (in [0, inf], default 0)

Type :

int
random_radius 

How much the radius is randomized (in [0, inf], default 0)

Type :

int
rounds 

Number of rounds in contour strokes (in [1, 1000], default 0)

Type :

int
shape 

Pick the contour-stroke shape used for the blueprint (default 'CIRCLES' )

- CIRCLES
Circles – Draw a blueprint using circular contour strokes.

- ELLIPSES
Ellipses – Draw a blueprint using elliptic contour strokes.

- SQUARES
Squares – Draw a blueprint using square contour strokes.

Type :

Literal[‘CIRCLES’, ‘ELLIPSES’, ‘SQUARES’]
type 

Which kind of modifier this is (default '2`D_OFFSET`' , readonly)

Type :

Literal[Linestyle Geometry Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool

[Related references](INDEX.md).
