# bpy.ops.grease_pencil.set_handle_type

bpy.ops.grease_pencil.set_handle_type ( * , type = 'AUTO' )
Configure handle behavior for Bézier curves

Parameters:
type ( Literal [ 'AUTO' , 'VECTOR' , 'ALIGN' , '`FREE_ALIGN`' , '`TOGGLE_FREE_ALIGN`' ] ) – Type, (optional)
- AUTO: Positioning is computed automatically for smoothness
- VECTOR: Positioning follows the direction toward the adjacent control point
- ALIGN: Handle is mirrored in direction opposite to the other handle
- `FREE_ALIGN`: Handle moves independently without affecting the paired handle
- `TOGGLE_FREE_ALIGN`: Swap free handles with aligned ones and vice versa

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
