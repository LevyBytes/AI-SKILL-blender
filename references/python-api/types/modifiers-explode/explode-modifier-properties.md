# bpy.types.ExplodeModifier: properties

## ExplodeModifier(Modifier)

### ExplodeModifier(Modifier)

base classes: bpy_struct, Modifier
class bpy.types. ExplodeModifier ( Modifier )

A modifier that drives an explosion effect off a particle system.
invert_vertex_group

Flip the influence of the vertex group (default False)

Type :

bool
particle_uv

Which UV map gets altered as particles age (default “”, never None)

Type :

str
protect

Keep vertex-group edges clean (in [0, 1], default 0.0)

Type :

float
show_alive

Display the mesh for living particles (default True)

Type :

bool
show_dead

Display the mesh for dead particles (default True)

Type :

bool
show_unborn

Display the mesh for not-yet-born particles (default True)

Type :

bool
use_edge_cut

Split face edges so the shrapnel looks cleaner (default False)

Type :

bool
use_size

Scale shrapnel by particle size (default False)

Type :

bool
vertex_group

(default “”, never None)

Type :

str

[Related references](INDEX.md).
