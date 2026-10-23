# bpy.ops.pose.select_all

bpy.ops.pose. select_all ( * , action = 'TOGGLE' ) 

Switch selection status for all bones

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Selection action to execute (optional)

- TOGGLE
Toggle – Toggle selection for all elements.

- SELECT
Select – Select all elements.

- DESELECT
Deselect – Deselect all elements.

- INVERT
Invert – Invert selection of all elements.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.pose. select_all ( * , action = 'TOGGLE' )
Toggles the selection status of all bones.
Parameters: action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Selection action to execute (optional)
- TOGGLE - Toggle: toggle selection for all elements.
- SELECT - Select: select all elements.
- DESELECT - Deselect: deselect all elements.
- INVERT - Invert: invert selection of all elements.
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
