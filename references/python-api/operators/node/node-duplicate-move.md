# bpy.ops.node.duplicate_move

bpy.ops.node. duplicate_move ( * , `NODE_OT`_duplicate = {} , `NODE_OT`_translate_attach = {} ) 

Make copies of marked nodes and shift them

Parameters :

- `NODE_OT`_duplicate ( dict [ str , Any ] ) – Make Copies, Make copies of marked nodes (optional, bpy.ops.node.duplicate() keyword arguments)

- `NODE_OT`_translate_attach ( dict [ str , Any ] ) – Move and Attach, Shift nodes and affix to frame (optional, bpy.ops.node.translate_attach() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
