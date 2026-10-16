# bpy.types.MeshVertex: properties

## MeshVertex(bpy_struct)

### MeshVertex(bpy_struct)

base class — bpy_struct
class bpy.types. MeshVertex ( bpy_struct )

Vertex in a Mesh data-block
co

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
groups

Weights for the vertex groups this vertex is member of (default None, readonly)

Type :

bpy_prop_collection[VertexGroupElement]
hide

(default False)

Type :

bool
index

Index of this vertex (in [0, inf], default 0, readonly)

Type :

int
normal

Vertex Normal (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
select

(default False)

Type :

bool
undeformed_co

On meshes that carry modifiers, this is the vertex coordinate before any deforming modifiers run, which generated texture coordinates rely on (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector

[Related references](INDEX.md).
