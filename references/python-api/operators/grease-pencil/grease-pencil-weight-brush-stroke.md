# bpy.ops.grease_pencil.weight_brush_stroke

bpy.ops.grease_pencil.weight_brush_stroke ( * , stroke = None , mode = 'NORMAL' , brush_toggle = 'None' , pen_flip = False )
Tint vertex weights onto points in the active Grease Pencil object

Parameters:
- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)
- mode ( Literal [ 'NORMAL' , 'INVERT' ] ) – Stroke Mode, Operation applied during brush motion (optional)
- NORMAL: Apply weight coloring normally
- INVERT: Reverse the weight coloring effect during this stroke
- brush_toggle ( Literal [ 'None' , 'SMOOTH' , 'ERASE' , 'MASK' ] ) – Temporary Brush Toggle Type, Alternate brush active for this stroke only (optional)
- None: Use the current weight tool
- SMOOTH: Temporarily activate smoothing (optional)
- ERASE: Temporarily activate eraser (optional)
- MASK: Temporarily activate masking (optional)
- pen_flip ( bool ) – Pen Flip, Indicates stylus eraser mode engagement (optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
