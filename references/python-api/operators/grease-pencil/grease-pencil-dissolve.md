# bpy.ops.grease_pencil.dissolve

bpy.ops.grease_pencil.dissolve ( * , type = 'POINTS' )
Discard marked points without severing the stroke into segments

Parameters:
type ( Literal [ 'POINTS' , 'BETWEEN' , 'UNSELECT' ] ) – Type, Point removal strategy (optional)
- POINTS: Erase highlighted points only
- BETWEEN: Erase points lying between highlighted ones
- UNSELECT: Erase every point except highlighted ones

Returns:
Result of the operator call.

Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
