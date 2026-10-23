# bpy.types.MeshLoopTriangle: properties

## MeshLoopTriangle(bpy_struct)

### MeshLoopTriangle(bpy_struct)

base class: bpy_struct
class bpy.types. MeshLoopTriangle ( bpy_struct )

Tessellated triangle in a Mesh data-block
area

Area of this triangle (in [0, inf], default 0.0, readonly)

Type :

float
index

Index of this loop triangle (in [0, inf], default 0, readonly)

Type :

int
loops

Indices of mesh loops that make up the triangle (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
material_index

Material slot index of this triangle (in [0, inf], default 0, readonly)

Type :

int
normal

Local space unit length normal vector for this triangle (array of 3 items, in [-1, 1], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
polygon_index

Index of mesh face that the triangle is a part of (in [0, inf], default 0, readonly)

Type :

int
split_normals

Local space unit length custom normal vectors of the face corners of this triangle (multi-dimensional array of 3 * 3 items, in [-1, 1], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), readonly)

Type :

bpy_prop_array[float]
use_smooth

(default False, readonly)

Type :

bool
vertices

Indices of triangle vertices (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
center

The midpoint of the face.

(readonly)
edge_keys

(readonly)

[Related references](INDEX.md).
