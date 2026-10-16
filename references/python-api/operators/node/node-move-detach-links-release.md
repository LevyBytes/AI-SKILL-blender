# bpy.ops.node.move_detach_links_release

bpy.ops.node. move_detach_links_release ( * , `NODE_OT`_links_detach = {} , `NODE_OT`_translate_attach = {} ) 

Shift a node to break links

Parameters :

- `NODE_OT`_links_detach ( dict [ str , Any ] ) – Detach Links, Strip all links to selected nodes, and try to connect neighbor nodes together (optional, bpy.ops.node.links_detach() keyword arguments)

- `NODE_OT`_translate_attach ( dict [ str , Any ] ) – Move and Attach, Move nodes and attach to frame (optional, bpy.ops.node.translate_attach() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
