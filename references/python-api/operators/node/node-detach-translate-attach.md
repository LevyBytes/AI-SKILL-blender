# bpy.ops.node.detach_translate_attach

bpy.ops.node. detach_translate_attach ( * , `NODE_OT`_detach = {} , `TRANSFORM_OT`_translate = {} , `NODE_OT`_attach = {} ) 

Let go of nodes, shift and affix to frame

Parameters :

- `NODE_OT`_detach ( dict [ str , Any ] ) – Detach Nodes, Let go of marked nodes from frames (optional, bpy.ops.node.detach() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Shift, Reposition picked items (optional, bpy.ops.transform.translate() keyword arguments)

- `NODE_OT`_attach ( dict [ str , Any ] ) – Attach Nodes, Fasten working node to a frame (optional, bpy.ops.node.attach() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
