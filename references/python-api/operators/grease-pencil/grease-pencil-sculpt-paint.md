# bpy.ops.grease_pencil.sculpt_paint

bpy.ops.grease_pencil.sculpt_paint ( * , stroke = None , mode = 'NORMAL' , brush_toggle = 'None' , pen_flip = False )
Shape strokes in the active Grease Pencil object

Parameters:
- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)
- mode ( Literal [ 'NORMAL' , 'INVERT' ] ) – Stroke Mode, Operation applied during brush motion (optional)
- NORMAL: Apply sculpting tool normally
- INVERT: Reverse the sculpting effect during this stroke
- brush_toggle ( Literal [ 'None' , 'SMOOTH' , 'ERASE' , 'MASK' ] ) – Temporary Brush Toggle Type, Alternate brush active for this stroke only (optional)
- None: Use the current sculpting tool
- SMOOTH: Temporarily activate smoothing (optional)
- ERASE: Temporarily activate eraser (optional)
- MASK: Temporarily activate masking (optional)
- pen_flip ( bool ) – Pen Flip, Indicates stylus eraser mode engagement (optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
