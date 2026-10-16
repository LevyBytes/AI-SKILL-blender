# bpy.ops.grease_pencil.delete

bpy.ops.grease_pencil.delete ( * , mode = 'ALL' )
Erase selected lines or points

Parameters:
mode ( Literal [ 'ALL' , 'STROKES' , 'FILLS' ] ) – Mode, Which category to remove (optional)
- ALL: Discard all selected strokes and fills
- STROKES: Discard strokes only, preserve fills
- FILLS: Discard fills only, preserve strokes

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
