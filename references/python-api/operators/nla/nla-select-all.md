# bpy.ops.nla.select_all

bpy.ops.nla. select_all ( * , action = 'TOGGLE' ) 

Toggle or alter the choice of all NLA-Sections

Parameters :

action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, What to do with each part (optional)

- TOGGLE
Switch – Flip choice for each part.

- SELECT
Activate – Mark each part.

- DESELECT
Unselect – Remove marks from each part.

- INVERT
Flip – Reverse what is and isn't marked.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
