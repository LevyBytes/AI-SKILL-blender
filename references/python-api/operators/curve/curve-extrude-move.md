# bpy.ops.curve.extrude_move

**bpy.ops.curve.extrude_move**( * , `CURVE_OT`_extrude = {} , `TRANSFORM_OT`_translate = {} )

Extend curve points and instantly move the new geometry.

Parameters:
- `CURVE_OT`_extrude ( dict [ str , Any ] ) – Extrude, Extend a spline by pulling out selected control points (optional, bpy.ops.curve.extrude() keyword arguments)
- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Reposition selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
