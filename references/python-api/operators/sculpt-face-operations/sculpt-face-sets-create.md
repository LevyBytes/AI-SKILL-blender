# bpy.ops.sculpt.face_sets_create

bpy.ops.sculpt. face_sets_create ( * , mode = 'MASKED' )

Form a novel face set

Parameters :

mode ( Literal [ 'MASKED' , 'VISIBLE' , 'ALL' , 'SELECTION' ] ) – Mode, (optional)

- MASKED
Face Set from Masked – Create a new face set from the masked faces.

- VISIBLE
Face Set from Visible – Create a new face set from the visible vertices.

- ALL
Face Set Full Mesh – Create a unique face set with all faces in the sculpt.

- SELECTION
Face Set from Edit Mode Selection – Create a face set corresponding to the Edit Mode face selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
