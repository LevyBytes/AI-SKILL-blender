# bpy.ops.curves.handle_type_set

**bpy.ops.curves.handle_type_set**( * , type = 'AUTO' )

Set the handle behavior for Bézier curves.

Parameters:
- type ( Literal [ 'AUTO' , 'VECTOR' , 'ALIGN' , '`FREE_ALIGN`' , '`TOGGLE_FREE_ALIGN`' ] ) – Type, (optional)

- AUTO
Auto – The location is automatically calculated to be smooth.

- VECTOR
Vector – The location is calculated to point to the next/previous control point.

- ALIGN
Align – The location is constrained to point in the opposite direction as the other handle.

- `FREE_ALIGN`
Free – The handle can be moved anywhere, and does not influence the point's other handle.

- `TOGGLE_FREE_ALIGN`
Toggle Free/Align – Replace Free handles with Align, and all Align with Free handles.

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
