# bpy.ops.grease_pencil.set_corner_type

bpy.ops.grease_pencil.set_corner_type ( * , corner_type = 'SHARP' , miter_angle = 0.785398 )
Configure endpoint styling for highlighted points

Parameters:
- corner_type ( Literal [ 'ROUND' , 'FLAT' , 'SHARP' ] ) – Corner Type, (optional)
- miter_angle ( float ) – Miter Cut Angle, All junctions sharper than this angle will be beveled (in [0, 3.14159], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
