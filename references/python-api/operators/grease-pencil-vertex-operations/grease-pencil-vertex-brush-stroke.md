# bpy.ops.grease_pencil.vertex_brush_stroke

bpy.ops.grease_pencil.vertex_brush_stroke ( * , stroke = None , mode = 'NORMAL' , brush_toggle = 'None' , pen_flip = False )
Paint color onto vertex data in the active Grease Pencil object

Parameters:
- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)
- mode ( Literal [ 'NORMAL' , 'INVERT' ] ) – Stroke Mode, Operation applied during brush motion (optional)
- NORMAL: Apply vertex coloring normally
- INVERT: Reverse the vertex coloring effect during this stroke
- brush_toggle ( Literal [ 'None' , 'SMOOTH' , 'ERASE' , 'MASK' ] ) – Temporary Brush Toggle Type, Alternate brush active for this stroke only (optional)
- None: Use the current vertex coloring tool
- SMOOTH: Temporarily activate smoothing (optional)
- ERASE: Temporarily activate eraser (optional)
- MASK: Temporarily activate masking (optional)
- pen_flip ( bool ) – Pen Flip, Indicates stylus eraser mode engagement (optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
