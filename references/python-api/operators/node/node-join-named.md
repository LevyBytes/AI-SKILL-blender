# bpy.ops.node.join_named

bpy.ops.node. join_named ( * , `NODE_OT`_join = {} , `WM_OT`_call_panel = {} ) 

Establish a fresh container around the selected nodes and apply a label right away

Parameters :

- `NODE_OT`_join ( dict [ str , Any ] ) – Join Nodes in Frame, Bundle selected nodes beneath a single container (optional, bpy.ops.node.join() keyword arguments)

- `WM_OT`_call_panel ( dict [ str , Any ] ) – Call Panel, Bring up a predetermined panel (optional, bpy.ops.wm.call_panel() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
