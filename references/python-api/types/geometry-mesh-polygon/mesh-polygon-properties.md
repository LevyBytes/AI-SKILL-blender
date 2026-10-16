# bpy.types.MeshPolygon: properties

## MeshPolygon(bpy_struct)

### MeshPolygon(bpy_struct)

base class — bpy_struct
class bpy.types. MeshPolygon ( bpy_struct )

Polygon in a Mesh data-block
area

Read only area of this face (in [0, inf], default 0.0, readonly)

Type :

float
center

Center of this face (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
hide

(default False)

Type :

bool
index

Index of this face (in [0, inf], default 0, readonly)

Type :

int
loop_start

Index of the first loop of this face (in [0, inf], default 0)

Type :

int
loop_total

Number of loops used by this face (in [0, inf], default 0, readonly)

Type :

int
material_index

Material slot index of this face (in [0, inf], default 0)

Type :

int
normal

Local space unit length normal vector for this face (array of 3 items, in [-1, 1], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
select

(default False)

Type :

bool
use_smooth

(default False)

Type :

bool
vertices

Vertex indices (array of 3 items, in [0, inf], default (0, 0, 0))

Type :

bpy_prop_array[int]
edge_keys

(readonly)
loop_indices

(readonly)

[Related references](INDEX.md).
