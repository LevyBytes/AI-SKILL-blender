# bpy.ops.grease_pencil.vertex_color_levels

bpy.ops.grease_pencil.vertex_color_levels ( * , mode = 'BOTH' , offset = 0.0 , gain = 1.0 )
Rescale vertex color intensity

Parameters:
- mode ( Literal [ 'STROKE' , 'FILL' , 'BOTH' ] ) – Mode, (optional)
- offset ( float ) – Offset, Constant to add to all colors (in [-1, 1], optional)
- gain ( float ) – Gain, Multiplier for all colors (in [0, inf], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
