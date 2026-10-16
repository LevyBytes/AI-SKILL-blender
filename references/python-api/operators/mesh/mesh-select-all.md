# bpy.ops.mesh.select_all

bpy.ops.mesh. select_all ( * , action = 'TOGGLE' ) 

Toggle or alter the selection state of mesh elements

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, What to do with each element (optional)

- TOGGLE
Toggle – Flip selection for each part.

- SELECT
Select – Mark each part as picked.

- DESELECT
Deselect – Remove marks from each part.

- INVERT
Invert – Reverse what is and isn't picked.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
