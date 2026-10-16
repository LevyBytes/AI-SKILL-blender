# bpy.ops.pose.select_hierarchy

bpy.ops.pose. select_hierarchy ( * , direction = 'PARENT' , extend = False ) 

Pick the direct parent and children of currently selected bones

Parameters :

- direction ( Literal [ 'PARENT' , 'CHILD' ] ) – Direction, (optional)

- extend ( bool ) – Extend, Extend the selection (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.pose. select_hierarchy ( * , direction = 'PARENT' , extend = False )
Selects the immediate parent/children of the selected bones.
Parameters:
- direction ( Literal [ 'PARENT' , 'CHILD' ] ) – Direction, (optional)
- extend ( bool ) – Extend, Extend the selection (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
