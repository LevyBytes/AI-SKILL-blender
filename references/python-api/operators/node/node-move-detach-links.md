# bpy.ops.node.move_detach_links

bpy.ops.node. move_detach_links ( * , `NODE_OT`_links_detach = {} , `TRANSFORM_OT`_translate = {} ) 

Shift a node to break links

Parameters :

- `NODE_OT`_links_detach ( dict [ str , Any ] ) – Detach Links, Strip all links to selected nodes, and try to connect neighbor nodes together (optional, bpy.ops.node.links_detach() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
