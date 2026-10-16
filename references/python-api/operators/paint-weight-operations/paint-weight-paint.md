# bpy.ops.paint.weight_paint

bpy.ops.paint. weight_paint ( * , stroke = None , mode = 'NORMAL' , brush_toggle = 'None' , pen_flip = False , override_location = False ) 

Paint a stroke into the currently active vertex group to modify weights

Parameters :

- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)

- mode ( Literal [ 'NORMAL' , 'INVERT' ] ) – Stroke Mode, Action taken when a paint stroke is made (optional)

- NORMAL
Regular – Applies the brush as normal without modification.

- INVERT
Invert – Reverses the brush's action throughout the stroke.

- brush_toggle ( Literal [ 'None' , 'SMOOTH' , 'ERASE' , 'MASK' ] ) – Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

- None
None – Leaves the brush unchanged.

- SMOOTH
Smooth – Temporarily switches to the smooth variant for this stroke.

- ERASE
Erase – Temporarily switches to the erase variant for this stroke.

- MASK
Mask – Temporarily switches to the mask variant for this stroke.

- pen_flip ( bool ) – Pen Flip, Whether a tablet's eraser mode is being used (optional)

- override_location ( bool ) – Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
