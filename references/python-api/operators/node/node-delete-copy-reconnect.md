# bpy.ops.node.delete_copy_reconnect

bpy.ops.node. delete_copy_reconnect ( * , `NODE_OT`_clipboard_copy = {} , `NODE_OT`_delete_reconnect = {} ) 

Grab nodes to clipboard, take out and re-join them.

Parameters :

- `NODE_OT`_clipboard_copy ( dict [ str , Any ] ) – Copy to Clipboard, Grab the marked nodes to the inward clipboard (optional, bpy.ops.node.clipboard_copy() keyword arguments)

- `NODE_OT`_delete_reconnect ( dict [ str , Any ] ) – Delete with Reconnect, Take out nodes and re-join nodes as if removal was skipped (optional, bpy.ops.node.delete_reconnect() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
