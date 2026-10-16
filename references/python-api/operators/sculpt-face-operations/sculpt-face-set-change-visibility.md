# bpy.ops.sculpt.face_set_change_visibility

bpy.ops.sculpt. face_set_change_visibility ( * , mode = 'TOGGLE' , active_face_set = 0 )

Regulate whether face sets display on the sculpted form

Parameters :

- mode ( Literal [ 'TOGGLE' , '`SHOW_ACTIVE`' , '`HIDE_ACTIVE`' ] ) – Mode, (optional)

- TOGGLE
Toggle Visibility – Hide all face sets except for the active one.

- `SHOW_ACTIVE`
Show Active Face Set – Show the active face set.

- `HIDE_ACTIVE`
Hide Active Face Set – Hide the active face set.

- active_face_set ( int ) – Active Face Set, (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
