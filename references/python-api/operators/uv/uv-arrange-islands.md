# bpy.ops.uv.arrange_islands

bpy.ops.uv. arrange_islands ( * , initial_position = '`BOUNDING_BOX`' , axis = 'Y' , align = 'MIN' , order = '`LARGE_TO_SMALL`' , margin = 0.05 ) 

Lays the chosen UV islands out along a line

Parameters :

- initial_position ( Literal [ '`BOUNDING_BOX`' , '`UV_GRID`' , '`ACTIVE_UDIM`' , 'CURSOR' ] ) – Initial Position, Initial position to arrange islands from (optional)

- `BOUNDING_BOX`
Bounding Box – Start the layout from the bounding box of the islands.

- `UV_GRID`
UV Grid – Start the layout from the UV Tile Grid.

- `ACTIVE_UDIM`
Active UDIM – Start the layout from the Active UDIM.

- CURSOR
2D Cursor – Start the layout from the 2D cursor.

- axis ( Literal [ 'X' , 'Y' ] ) – Axis, Axis to arrange UV islands on (optional)

- X
X – Lay the UV islands out along the X axis.

- Y
Y – Lay the UV islands out along the Y axis.

- align ( Literal [ 'MIN' , 'MAX' , 'CENTER' , 'NONE' ] ) – Align, Location to align islands on (optional)

- MIN
Min – Snap the islands to their own min edge.

- MAX
Max – Snap the islands to their own max edge.

- CENTER
Center – Snap the islands to the center of the biggest island.

- NONE
None – Leave the island alignment untouched.

- order ( Literal [ '`LARGE_TO_SMALL`' , '`SMALL_TO_LARGE`' , 'Fixed' ] ) – Order, Order of islands (optional)

- `LARGE_TO_SMALL`
Largest to Smallest – Order islands big-first down to small.

- `SMALL_TO_LARGE`
Smallest to Largest – Order islands small-first up to large.

- Fixed
Fixed – Leave the island order as it is.

- margin ( float ) – Margin, Space between islands (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
