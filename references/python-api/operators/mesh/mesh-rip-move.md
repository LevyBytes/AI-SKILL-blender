# bpy.ops.mesh.rip_move

bpy.ops.mesh. rip_move ( * , `MESH_OT`_rip = {} , `TRANSFORM_OT`_translate = {} ) 

Tear faces apart and shift the outcome

Parameters :

- `MESH_OT`_rip ( dict [ str , Any ] ) – Separate, Isolate vertices or edges from the rest of the mesh (optional, bpy.ops.mesh.rip() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Shift, Reposition picked items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
