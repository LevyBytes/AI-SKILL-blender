# bpy.ops.pose.selection_set_select

bpy.ops.pose. selection_set_select ( * , selection_set_index = -1 ) 

Highlight the bones within this Selection Set

Parameters :

selection_set_index ( int ) – Selection Set Index, Which Selection Set to select; -1 uses the active Selection Set (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/bone_selection_sets.py:239
bpy.ops.pose. selection_set_select ( * , selection_set_index = -1 )
Selects the bones from this Selection Set.
Parameters: selection_set_index ( int ) – Selection Set Index, Which Selection Set to select; -1 uses the active Selection Set (in [-inf, inf], optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/bone_selection_sets.py:239

[Related references](INDEX.md).
