# bpy.ops.sculpt.project_line_gesture

bpy.ops.sculpt. project_line_gesture ( * , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 , use_front_faces_only = False , use_limit_to_segment = False )

Project the surface onto a plane described by a line

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
bpy.ops.sculpt. project_line_gesture ( * , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 , use_front_faces_only = False , use_limit_to_segment = False )
Projects the geometry onto a plane defined by a line.
Parameters:
- xstart ( int ) – X Start, (in [-inf, inf], optional)
- xend ( int ) – X End, (in [-inf, inf], optional)
- ystart ( int ) – Y Start, (in [-inf, inf], optional)
- yend ( int ) – Y End, (in [-inf, inf], optional)
- flip ( bool ) – Flip, (optional)
- cursor ( int ) – Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
- use_front_faces_only ( bool ) – Front Faces Only, Affect only faces facing towards the view (optional)
- use_limit_to_segment ( bool ) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
