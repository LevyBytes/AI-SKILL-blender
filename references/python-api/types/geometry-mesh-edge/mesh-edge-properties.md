# bpy.types.MeshEdge: properties

## MeshEdge(bpy_struct)

### MeshEdge(bpy_struct)

base class — bpy_struct
class bpy.types. MeshEdge ( bpy_struct )

Edge in a Mesh data-block
hide

(default False)

Type :

bool
index

Index of this edge (in [0, inf], default 0, readonly)

Type :

int
is_loose

Edge is not connected to any faces (default False, readonly)

Type :

bool
select

(default False)

Type :

bool
use_edge_sharp

Sharp edge for shading (default False)

Type :

bool
use_seam

Seam edge for UV unwrapping (default False)

Type :

bool
vertices

Vertex indices (array of 2 items, in [0, inf], default (0, 0))

Type :

bpy_prop_array[int]

key

(readonly)

[Related references](INDEX.md).
