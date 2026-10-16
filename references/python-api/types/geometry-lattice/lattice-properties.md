# bpy.types.Lattice: properties

## Lattice(ID)

### Lattice(ID) 

base classes — bpy_struct, ID
class bpy.types. Lattice ( ID ) 

Lattice data-block defining a grid for deforming other objects
animation_data 

Animation data for this data-block (readonly)

Type :

AnimData
interpolation_type_u 

(default '`KEY_BSPLINE`' )

Type :

Literal[‘`KEY_LINEAR`’, ‘`KEY_CARDINAL`’, ‘`KEY_CATMULL_ROM`’, ‘`KEY_BSPLINE`’]
interpolation_type_v 

(default '`KEY_BSPLINE`' )

Type :

Literal[‘`KEY_LINEAR`’, ‘`KEY_CARDINAL`’, ‘`KEY_CATMULL_ROM`’, ‘`KEY_BSPLINE`’]
interpolation_type_w 

(default '`KEY_BSPLINE`' )

Type :

Literal[‘`KEY_LINEAR`’, ‘`KEY_CARDINAL`’, ‘`KEY_CATMULL_ROM`’, ‘`KEY_BSPLINE`’]
is_editmode 

True when the lattice is being used in edit mode (default False, readonly)

Type :

bool
points 

The grid points making up the lattice (default None, readonly)

Type :

bpy_prop_collection[LatticePoint]
points_u 

Point count along U (locked once shape keys exist) (in [1, 64], default 0)

Type :

int
points_v 

Point count along V (locked once shape keys exist) (in [1, 64], default 0)

Type :

int
points_w 

Point count along W (locked once shape keys exist) (in [1, 64], default 0)

Type :

int
shape_keys 

(readonly)

Type :

Key
use_outside 

Show and account for only the outermost vertices (default False)

Type :

bool
vertex_group 

Vertex group controlling where the lattice exerts its influence (default “”, never None)

Type :

str

[Related references](INDEX.md).
