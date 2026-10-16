# bpy.types.CorrectiveSmoothModifier: properties

## CorrectiveSmoothModifier(Modifier)

### CorrectiveSmoothModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. CorrectiveSmoothModifier ( Modifier )

Counteract the distortion that deformation introduces.
factor

Strength of the smoothing pass (in [-inf, inf], default 0.5)

Type :

float
invert_vertex_group

Flip the weighting of the vertex group (default False)

Type :

bool
is_bind

(default False, readonly)

Type :

bool
iterations

(in [0, 32767], default 5)

Type :

int
rest_source

Pick where the rest positions are taken from (default 'ORCO' )

- ORCO
Original Coords – Take rest positions from the base mesh's own vertex coordinates.

- BIND
Bind Coords – Take rest positions from the bound vertex coordinates instead.

Type :

Literal['ORCO', 'BIND']
scale

Counterbalance any scaling applied by modifiers further up the stack (in [-inf, inf], default 1.0)

Type :

float
smooth_type

Which algorithm carries out the smoothing (default 'SIMPLE' )

- SIMPLE
Simple – Average the neighbouring edge-vertices together.

- `LENGTH_WEIGHTED`
Length Weight – Average the neighbouring edge-vertices, but weight each by edge length.

Type :

Literal['SIMPLE', '`LENGTH_WEIGHTED`']
use_only_smooth

Smooth the mesh but skip rebuilding the surface (default False)

Type :

bool
use_pin_boundary

Hold boundary vertices fixed so they aren't smoothed (default False)

Type :

bool
vertex_group

The vertex group whose weights set the modifier's per-point strength (default "", never None)

Type :

str

[Related references](INDEX.md).
