# bpy.ops.curve.duplicate_move

**bpy.ops.curve.duplicate_move**( * , `CURVE_OT`_duplicate = {} , `TRANSFORM_OT`_translate = {} )

Duplicate curve points and instantly move them.

Parameters:
- `CURVE_OT`_duplicate ( dict [ str , Any ] ) – Duplicate Curve, Create a copy of selected control points (optional, bpy.ops.curve.duplicate() keyword arguments)
- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Reposition selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
