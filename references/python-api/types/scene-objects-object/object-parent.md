# bpy.types.Object: parent, parent_bone, parent_type, parent_vertices

parent 

The object's parent

Type :

Object
parent_bone 

The parent bone's name when bone parenting is used (default “”, never None)

Type :

str
parent_type 

The kind of parenting relationship (default 'OBJECT' )

- OBJECT
Object – The object is parented to an object.

- ARMATURE
Armature.

- LATTICE
Lattice – The object is parented to a lattice.

- VERTEX
Vertex – The object is parented to a vertex.

- `VERTEX_3`
3 Vertices.

- BONE
Bone – The object is parented to a bone.

Type :

Literal[‘OBJECT’, ‘ARMATURE’, ‘LATTICE’, ‘VERTEX’, ‘`VERTEX_3`’, ‘BONE’]
parent_vertices 

The vertex indices used when vertex parenting applies (array of 3 items, in [0, inf], default (0, 0, 0))

Type :

bpy_prop_array[int]

[Related references](INDEX.md).
