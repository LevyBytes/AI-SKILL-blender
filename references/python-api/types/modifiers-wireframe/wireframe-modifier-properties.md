# bpy.types.WireframeModifier: properties

## WireframeModifier(Modifier)

### WireframeModifier(Modifier) 

base classes: bpy_struct, Modifier
class bpy.types. WireframeModifier ( Modifier ) 

A modifier that converts geometry into a wireframe
crease_weight 

Weight used for creasing, when creasing is on (in [-inf, inf], default 1.0)

Type :

float
invert_vertex_group 

Flip the effect of the chosen vertex group (default False)

Type :

bool
material_offset 

Shift the material slot index assigned to the new faces (in [-32768, 32767], default 0)

Type :

int
offset 

How far the thickness extends out from the midline (in [-inf, inf], default 0.0)

Type :

float
thickness 

Multiplier controlling wire thickness (in [-inf, inf], default 0.02)

Type :

float
thickness_vertex_group 

The thickness multiplier applied where vertex group weight is zero (in [0, 1], default 0.0)

Type :

float
use_boundary 

Also generate wires along open edges of the mesh (default False)

Type :

bool
use_crease 

Mark hub edges as creased so subdivision surfaces behave better (default False)

Type :

bool
use_even_offset 

Adjust the offset so wire thickness stays more uniform (default True)

Type :

bool
use_relative_offset 

Make the offset scale with nearby geometry (default False)

Type :

bool
use_replace 

Discard the source geometry, leaving only the wires (default True)

Type :

bool
vertex_group 

Name of the vertex group that limits which areas are affected (default “”, never None)

Type :

str

[Related references](INDEX.md).
