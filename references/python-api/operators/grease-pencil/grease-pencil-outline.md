# bpy.ops.grease_pencil.outline

bpy.ops.grease_pencil.outline ( * , type = 'VIEW' , radius = 0.01 , offset_factor = -1.0 , corner_subdivisions = 2 )
Transform highlighted strokes into their outer boundary

Parameters:
- type ( Literal [ 'VIEW' , 'FRONT' , 'SIDE' , 'TOP' , 'CURSOR' , 'CAMERA' ] ) – Projection Mode, (optional)
- radius ( float ) – Radius, (in [0, 10], optional)
- offset_factor ( float ) – Offset Factor, (in [-1, 1], optional)
- corner_subdivisions ( int ) – Corner Subdivisions, (in [0, 10], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
