# bpy.ops.action.snap

bpy.ops.action. snap ( * , type = 'CFRA' )

Realign picked keyframes to specified timeline positions.

Parameters :

type ( Literal [ 'CFRA' , '`NEAREST_FRAME`' , '`NEAREST_SECOND`' , '`NEAREST_MARKER`' ] ) – Type, (optional)

- CFRA
Selection to Current Frame – Move selected keyframes to match the active frame.

- `NEAREST_FRAME`
Selection to Nearest Frame – Align selected keyframes to the nearest integer frame (useful for correcting subframe drift).

- `NEAREST_SECOND`
Selection to Nearest Second – Realign selected keyframes to whole-second marks.

- `NEAREST_MARKER`
Selection to Nearest Marker – Snap selected keyframes to the nearest marker.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
