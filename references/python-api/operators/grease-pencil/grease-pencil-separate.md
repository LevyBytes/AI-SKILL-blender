# bpy.ops.grease_pencil.separate

bpy.ops.grease_pencil.separate ( * , mode = 'SELECTED' )
Isolate the highlighted geometry into its own Grease Pencil object

Parameters:
mode ( Literal [ 'SELECTED' , 'MATERIAL' , 'LAYER' ] ) – Mode, (optional)
- SELECTED: Isolate highlighted geometry
- MATERIAL: Isolate by material assignment
- LAYER: Isolate by layer membership

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
