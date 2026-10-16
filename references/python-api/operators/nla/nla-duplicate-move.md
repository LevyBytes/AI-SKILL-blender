# bpy.ops.nla.duplicate_move

bpy.ops.nla. duplicate_move ( * , `NLA_OT`_duplicate = {} , `TRANSFORM_OT`_translate = {} ) 

Make copies of marked NLA-Sections, putting the duplicates on fresh track(s)

Parameters :

- `NLA_OT`_duplicate ( dict [ str , Any ] ) – Make Copies, Make copies of marked NLA-Sections, putting the duplicates on fresh track(s) (optional, bpy.ops.nla.duplicate() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Shift, Reposition picked items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
