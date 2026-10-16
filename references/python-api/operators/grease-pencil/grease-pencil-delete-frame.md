# bpy.ops.grease_pencil.delete_frame

bpy.ops.grease_pencil.delete_frame ( * , type = '`ACTIVE_FRAME`' )
Discard drawn frame(s)

Parameters:
type ( Literal [ '`ACTIVE_FRAME`' , '`ALL_FRAMES`' ] ) – Type, Frame removal strategy (optional)
- `ACTIVE_FRAME`: Remove the current frame on the active layer only
- `ALL_FRAMES`: Remove current frames across all layers

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
