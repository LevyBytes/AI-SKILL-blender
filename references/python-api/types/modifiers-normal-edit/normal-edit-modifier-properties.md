# bpy.types.NormalEditModifier: properties

invert_vertex_group 

Flip the sway of the vertex group (default False)

Type :

bool
mix_factor 

Proportion of the generated normals to blend over the existing ones (in [0, 1], default 1.0)

Type :

float
mix_limit 

Largest angle allowed between the old and new normals (in [0, 3.14159], default 3.14159)

Type :

float
mix_mode 

The way generated normals combine with the ones already there (default 'COPY' )

- COPY
Copy – Replace the existing normals with the new ones.

- ADD
Add – Write the sum of the new and old normals.

- SUB
Subtract – Write the new normals with the old ones taken away.

- MUL
Multiply – Write the product of old and new normals (not a cross product).

Type :

Literal[‘COPY’, ‘ADD’, ‘SUB’, ‘MUL’]
mode 

The approach used to generate or affect normals (default 'RADIAL' )

- RADIAL
Radial – Derived from an ellipsoid whose shape comes from the boundbox dimensions; a target is optional.

- DIRECTIONAL
Directional – Normals point toward (‘track’) the target object.

Type :

Literal[‘RADIAL’, ‘DIRECTIONAL’]
no_polynors_fix 

Leave polygons unflipped even where their normals disagree with the freshly computed custom vertex normals (default False)

Type :

bool
offset 

Displacement measured from the object's center (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
target 

The target object that drives the normals

Type :

Object
use_direction_parallel 

Apply one shared direction to every normal, running from the origin to the target's center (Directional mode only) (default True)

Type :

bool
vertex_group 

Name of the vertex group that picks out and weights the affected regions (default “”, never None)

Type :

str

[Related references](INDEX.md).
