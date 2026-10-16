# bpy.ops.uv.align

bpy.ops.uv. align ( * , axis = '`ALIGN_AUTO`' , position_mode = 'MEAN' ) 

Lines up the chosen UV vertices along a straight line

Parameters :

- axis ( Literal [ '`ALIGN_S`' , '`ALIGN_T`' , '`ALIGN_U`' , '`ALIGN_AUTO`' , '`ALIGN_X`' , '`ALIGN_Y`' ] ) – Axis, Axis to align UV locations on (optional)

- `ALIGN_S`
Straighten – Snap UV vertices to the line running between the two endpoints.

- `ALIGN_T`
Straighten X – Snap UV vertices to that endpoint line by shifting them horizontally.

- `ALIGN_U`
Straighten Y – Snap UV vertices to that endpoint line by shifting them vertically.

- `ALIGN_AUTO`
Align Auto – Pick automatically whichever direction is already closest to aligned.

- `ALIGN_X`
Align Vertically – Place UV vertices along a vertical line.

- `ALIGN_Y`
Align Horizontally – Place UV vertices along a horizontal line.

- position_mode ( Literal [ 'MEAN' , 'MIN' , 'MAX' ] ) – Position Mode, Method of calculating the alignment position (optional)

- MEAN
Mean – Line the UVs up on their average position.

- MIN
Minimum – Line the UVs up on their minimum position.

- MAX
Maximum – Line the UVs up on their maximum position.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
