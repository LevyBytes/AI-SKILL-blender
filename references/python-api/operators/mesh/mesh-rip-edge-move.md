# bpy.ops.mesh.rip_edge_move

bpy.ops.mesh. rip_edge_move ( * , `MESH_OT`_rip_edge = {} , `TRANSFORM_OT`_translate = {} ) 

Push vertices from edges and reposition the result

Parameters :

- `MESH_OT`_rip_edge ( dict [ str , Any ] ) – Push Vertices, Push out vertices from the nearest edge in the viewport (optional, bpy.ops.mesh.rip_edge() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Shift, Reposition picked items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
