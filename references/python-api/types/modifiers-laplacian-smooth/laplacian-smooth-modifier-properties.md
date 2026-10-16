# bpy.types.LaplacianSmoothModifier: properties

## LaplacianSmoothModifier(Modifier)

### LaplacianSmoothModifier(Modifier) 

base classes — bpy_struct, Modifier
class bpy.types. LaplacianSmoothModifier ( Modifier ) 

Smoothing effect modifier
invert_vertex_group 

Flip how the vertex group weights apply (default False)

Type :

bool
iterations 

(in [0, 32767], default 1)

Type :

int
lambda_border 

Lambda factor in border (in [-inf, inf], default 0.01)

Type :

float
lambda_factor 

Smooth effect factor (in [-inf, inf], default 0.01)

Type :

float
use_normalized 

Refine and steady the enhanced shape (default True)

Type :

bool
use_volume_preserve 

Preserve volume once the smoothing has run (default True)

Type :

bool
use_x 

Apply smoothing on the X axis (default True)

Type :

bool
use_y 

Apply smoothing on the Y axis (default True)

Type :

bool
use_z 

Apply smoothing on the Z axis (default True)

Type :

bool
vertex_group 

Vertex Group that sets the modifier's per-point influence (default “”, never None)

Type :

str

[Related references](INDEX.md).
