# bpy.ops.mesh.select_mode

bpy.ops.mesh. select_mode ( * , use_extend = False , use_expand = False , type = 'VERT' , action = 'TOGGLE' ) 

Adjust what kind of parts can be selected

Parameters :

- use_extend ( bool ) – Extend, (optional)

- use_expand ( bool ) – Expand, (optional)

- type (Literal[Mesh Select Mode Items]) – Type, (optional)

- action ( Literal [ 'DISABLE' , 'ENABLE' , 'TOGGLE' ] ) – Action, What to do with the pick style (optional)

- DISABLE
Disable – Turn off the pick style.

- ENABLE
Enable – Turn on the pick style.

- TOGGLE
Toggle – Flip the pick style.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
