# bpy.ops.sculpt.face_set_edit

bpy.ops.sculpt. face_set_edit ( * , active_face_set = 1 , mode = 'GROW' , strength = 1.0 , modify_hidden = False )

Adjust the currently active face set

Parameters :

- active_face_set ( int ) – Active Face Set, (in [0, inf], optional)

- mode ( Literal [ 'GROW' , 'SHRINK' , '`DELETE_GEOMETRY`' , '`FAIR_POSITIONS`' , '`FAIR_TANGENCY`' ] ) – Mode, (optional)

- GROW
Grow Face Set – Grows the face set boundary by one face based on mesh topology.

- SHRINK
Shrink Face Set – Shrinks the face set boundary by one face based on mesh topology.

- `DELETE_GEOMETRY`
Delete Geometry – Deletes the faces that are assigned to the face set.

- `FAIR_POSITIONS`
Fair Positions – Creates the smoothest possible geometry patch from the face set minimizing changes in vertex positions.

- `FAIR_TANGENCY`
Fair Tangency – Creates the smoothest possible geometry patch from the face set minimizing changes in vertex tangents.

- strength ( float ) – Strength, (in [0, 1], optional)

- modify_hidden ( bool ) – Modify Hidden, Execute the alteration on hidden geometry (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
