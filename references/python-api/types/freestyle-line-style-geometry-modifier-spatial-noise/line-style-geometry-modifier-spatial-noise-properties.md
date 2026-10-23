# bpy.types.LineStyleGeometryModifier_SpatialNoise: properties

## LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier)

### LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier) 

base classes: bpy_struct, LineStyleModifier, LineStyleGeometryModifier
class bpy.types. LineStyleGeometryModifier_SpatialNoise ( LineStyleGeometryModifier ) 

Apply spatial noise to the stroke backbone geometry
amplitude 

Amplitude of the spatial noise (in [-inf, inf], default 0.0)

Type :

float
expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
octaves 

Octave count, which sets how much spatial-noise detail is present (in [0, inf], default 0)

Type :

int
scale 

Scale of the spatial noise (in [-inf, inf], default 0.0)

Type :

float
smooth 

When enabled, the spatial noise is smoothed (default False)

Type :

bool
type 

Which kind of modifier this is (default '2`D_OFFSET`' , readonly)

Type :

Literal[Linestyle Geometry Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

Type :

bool
use_pure_random 

When enabled, the spatial noise has no coherence at all (default False)

Type :

bool

[Related references](INDEX.md).
