# bpy.ops.mesh.extrude_manifold

bpy.ops.mesh. extrude_manifold ( * , `MESH_OT`_extrude_region = {} , `TRANSFORM_OT`_translate = {} )

Extend and smooth coplanar surface edges to incorporate newly created ones

Parameters :

- `MESH_OT`_extrude_region ( dict [ str , Any ] ) – Extrude Region, Extrude region of faces (optional, bpy.ops.mesh.extrude_region() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
