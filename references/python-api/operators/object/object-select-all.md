# bpy.ops.object.select_all

bpy.ops.object. select_all ( * , action = 'TOGGLE' ) 

Modify visibility selection across all objects in the viewport

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Modify all highlighting (optional)

- TOGGLE
Toggle – Flip highlight state on every element.

- SELECT
Select – Highlight every element.

- DESELECT
Deselect – Remove highlighting from every element.

- INVERT
Invert – Flip highlight state on every element.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
