# bpy.ops.node.select_link_viewer

bpy.ops.node. select_link_viewer ( * , `NODE_OT`_select = {} , `NODE_OT`_link_viewer = {} ) 

Pick node and establish path to an inspection terminal

Parameters :

- `NODE_OT`_select ( dict [ str , Any ] ) – Select, Pick the node underneath the cursor position (optional, bpy.ops.node.select() keyword arguments)

- `NODE_OT`_link_viewer ( dict [ str , Any ] ) – Link to Viewer Node, Establish connection to inspection terminal node (optional, bpy.ops.node.link_viewer() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
