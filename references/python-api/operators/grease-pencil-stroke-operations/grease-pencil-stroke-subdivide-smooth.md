# bpy.ops.grease_pencil.stroke_subdivide_smooth

bpy.ops.grease_pencil.stroke_subdivide_smooth ( * , `GREASE_PENCIL_OT`_stroke_subdivide = {} , `GREASE_PENCIL_OT`_stroke_smooth = {} )
Add intermediate points and then blend them

Parameters:
- `GREASE_PENCIL_OT`_stroke_subdivide ( dict [ str , Any ] ) – Subdivide Stroke, Insert points between continuous highlighted points (optional, bpy.ops.grease_pencil.stroke_subdivide() keyword arguments)
- `GREASE_PENCIL_OT`_stroke_smooth ( dict [ str , Any ] ) – Smooth Stroke, Reduce roughness in highlighted strokes (optional, bpy.ops.grease_pencil.stroke_smooth() keyword arguments)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
