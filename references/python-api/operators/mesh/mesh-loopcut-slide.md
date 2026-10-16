# bpy.ops.mesh.loopcut_slide

bpy.ops.mesh. loopcut_slide ( * , `MESH_OT`_loopcut = {} , `TRANSFORM_OT`_edge_slide = {} )

Score a mesh loop and move it

Parameters :

- `MESH_OT`_loopcut ( dict [ str , Any ] ) – Loop Cut, Add a new loop between existing loops (optional, bpy.ops.mesh.loopcut() keyword arguments)

- `TRANSFORM_OT`_edge_slide ( dict [ str , Any ] ) – Edge Slide, Slide an edge loop along a mesh (optional, bpy.ops.transform.edge_slide() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
