# bpy.ops.sculpt_curves.brush_stroke

bpy.ops.sculpt_curves. brush_stroke ( * , stroke = None , mode = 'NORMAL' , brush_toggle = 'None' , pen_flip = False )

Form curves using a tool

Parameters :

- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)

- mode ( Literal [ 'NORMAL' , 'INVERT' ] ) – Stroke Mode, How the brush applies when drawing a mark (optional)

- NORMAL
Regular – Apply brush normally.

- INVERT
Invert – Invert action of brush for duration of stroke.

- brush_toggle ( Literal [ 'None' , 'SMOOTH' , 'ERASE' , 'MASK' ] ) – Temporary Brush Toggle Type, Alternative brush available during the mark (optional)

- None
None – Apply brush normally.

- SMOOTH
Smooth – Switch to smooth brush for duration of stroke.

- ERASE
Erase – Switch to erase brush for duration of stroke.

- MASK
Mask – Switch to mask brush for duration of stroke.

- pen_flip ( bool ) – Pen Flip, Whether a tablet's eraser mode is being used (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
