# bpy.ops.mesh.duplicate_move

bpy.ops.mesh. duplicate_move ( * , `MESH_OT`_duplicate = {} , `TRANSFORM_OT`_translate = {} )

Produce a mesh replica and reposition it

Parameters :

- `MESH_OT`_duplicate ( dict [ str , Any ] ) – Duplicate, Duplicate selected vertices, edges or faces (optional, bpy.ops.mesh.duplicate() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
