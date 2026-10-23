# bpy.types.MeshLoop: properties

## MeshLoop(bpy_struct)

### MeshLoop(bpy_struct)

base class: bpy_struct
class bpy.types. MeshLoop ( bpy_struct )

Loop in a Mesh data-block
bitangent

Bitangent vector of this vertex for this face (must be computed beforehand using calc_tangents, use it only if really needed, slower access than bitangent_sign) (array of 3 items, in [-1, 1], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
bitangent_sign

Sign of the bitangent vector of this vertex for this face (must be computed beforehand using calc_tangents, bitangent = bitangent_sign * cross(normal, tangent)) (in [-1, 1], default 0.0, readonly)

Type :

float
edge_index

Edge index (in [0, inf], default 0)

Type :

int
index

Index of this loop (in [0, inf], default 0, readonly)

Type :

int
normal

The normal direction of the face corner, taking into account sharp faces, sharp edges, and custom normal data (array of 3 items, in [-1, 1], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
tangent

Local space unit length tangent vector of this vertex for this face (must be computed beforehand using calc_tangents) (array of 3 items, in [-1, 1], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
vertex_index

Vertex index (in [0, inf], default 0)

Type :

int

[Related references](INDEX.md).
