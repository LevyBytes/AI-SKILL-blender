# bpy.ops.sculpt.face_set_line_gesture

bpy.ops.sculpt. face_set_line_gesture ( * , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 , use_front_faces_only = False , use_limit_to_segment = False )

Create a face set on one side of a line described by the cursor

Parameters :

- xstart ( int ) – X Start, (in [-inf, inf], optional)

- xend ( int ) – X End, (in [-inf, inf], optional)

- ystart ( int ) – Y Start, (in [-inf, inf], optional)

- yend ( int ) – Y End, (in [-inf, inf], optional)

- flip ( bool ) – Flip, (optional)

- cursor ( int ) – Cursor, Pointer appearance during the interactive operation (in [0, inf], optional)

- use_front_faces_only ( bool ) – Front Faces Only, Influence only surfaces oriented toward the camera (optional)

- use_limit_to_segment ( bool ) – Limit to Segment, Confine the gesture activity to the zone within the segment without extending along the complete line (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
