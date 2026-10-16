# bpy.ops.grease_pencil.duplicate_move

bpy.ops.grease_pencil.duplicate_move ( * , `GREASE_PENCIL_OT`_duplicate = {} , `TRANSFORM_OT`_translate = {} )
Create copies of strokes and reposition them interactively

Parameters:
- `GREASE_PENCIL_OT`_duplicate ( dict [ str , Any ] ) – Duplicate, Replicate the highlighted points (optional, bpy.ops.grease_pencil.duplicate() keyword arguments)
- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Translate selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
