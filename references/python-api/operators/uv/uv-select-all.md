# bpy.ops.uv.select_all

bpy.ops.uv. select_all ( * , action = 'TOGGLE' ) 

Alters the selection state of every UV vertex

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Selection action to execute (optional)

- TOGGLE
Toggle – Flip the selection state of every element.

- SELECT
Select – Mark every element as selected.

- DESELECT
Deselect – Clear the selection on every element.

- INVERT
Invert – Swap the selection state across all elements.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
