# bpy.ops.nla.duplicate_linked_move

bpy.ops.nla. duplicate_linked_move ( * , `NLA_OT`_duplicate = {} , `TRANSFORM_OT`_translate = {} ) 

Make linked copies of marked NLA-Sections, putting the copies on fresh track(s)

Parameters :

- `NLA_OT`_duplicate ( dict [ str , Any ] ) – Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s) (optional, bpy.ops.nla.duplicate() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Reposition picked items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
