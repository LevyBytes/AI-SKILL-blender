# bpy.ops.armature.select_all

bpy.ops.armature. select_all ( * , action = 'TOGGLE' )

Change selection status for every bone.

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Selection action to execute (optional)

- TOGGLE
Toggle – Change selection for all elements.

- SELECT
Select – Pick all elements.

- DESELECT
Deselect – Unselect all elements.

- INVERT
Invert – Flip selection state for all elements.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
