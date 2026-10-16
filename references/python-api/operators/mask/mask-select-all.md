# bpy.ops.mask.select_all

bpy.ops.mask. select_all ( * , action = 'TOGGLE' )

Change selection of all curve points

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Which selection action to run (optional)

- TOGGLE
Toggle – Flip the selection state of every element.

- SELECT
Select – Select every element.

- DESELECT
Deselect – Deselect every element.

- INVERT
Invert – Swap which elements are selected.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
