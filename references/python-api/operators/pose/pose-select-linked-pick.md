# bpy.ops.pose.select_linked_pick

bpy.ops.pose. select_linked_pick ( * , extend = False ) 

Pick bones joined by connected ancestry underneath the cursor

Parameters :

extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.pose. select_linked_pick ( * , extend = False )
Selects bones linked by connected parent/child relationships under the mouse cursor.
Parameters: extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
