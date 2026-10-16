# bpy.ops.paint.image_paint

bpy.ops.paint. image_paint ( * , stroke = None , mode = 'NORMAL' , brush_toggle = 'None' , pen_flip = False ) 

Tint a movement inside the picture

Parameters :

- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)

- mode ( Literal [ 'NORMAL' , 'INVERT' ] ) – Stroke Mode, Activity executed once a tint movement is created (optional)

- NORMAL
Regular – Operate brush habitually.

- INVERT
Invert – Reverse activity of brush throughout movement span.

- brush_toggle ( Literal [ 'None' , 'SMOOTH' , 'ERASE' , 'MASK' ] ) – Temporary Brush Toggle Type, Brush to utilize throughout movement span (optional)

- None
None – Operate brush habitually.

- SMOOTH
Smooth – Exchange to polishing brush throughout movement span.

- ERASE
Erase – Exchange to wiping brush throughout movement span.

- MASK
Mask – Exchange to mask brush throughout movement span.

- pen_flip ( bool ) – Pen Flip, When a stylus's eliminating manner is in consumption (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
