# bpy.ops.pose.selection_set_move

bpy.ops.pose. selection_set_move ( * , direction = 'UP' ) 

Shift the active Selection Set forward or backward in its ordering

Parameters :

direction ( Literal [ 'UP' , 'DOWN' ] ) – Move Direction, Direction to move the active Selection Set: UP (default) or DOWN (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/bone_selection_sets.py:126
bpy.ops.pose. selection_set_move ( * , direction = 'UP' )
Moves the active Selection Set up or down the list of sets.
Parameters: direction ( Literal [ 'UP' , 'DOWN' ] ) – Move Direction, Direction to move the active Selection Set: UP (default) or DOWN (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/bone_selection_sets.py:126

[Related references](INDEX.md).
