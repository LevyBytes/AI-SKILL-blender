# bpy.ops.grease_pencil.layer_merge

bpy.ops.grease_pencil.layer_merge ( * , mode = 'ACTIVE' )
Fuse layers together following the chosen strategy

Parameters:
mode ( Literal [ 'ACTIVE' , 'GROUP' , 'ALL' ] ) – Mode, (optional)
- ACTIVE: Combine the current layer with the one immediately below
- GROUP: Combine all layers within the active group
- ALL: Combine every layer into a single one

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
