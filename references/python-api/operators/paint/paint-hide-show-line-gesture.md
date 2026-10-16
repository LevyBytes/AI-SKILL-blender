# bpy.ops.paint.hide_show_line_gesture

bpy.ops.paint. hide_show_line_gesture ( * , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 , action = 'HIDE' , area = 'Inside' , use_front_faces_only = False , use_limit_to_segment = False ) 

Conceal/expose certain vertices

Parameters :

- xstart ( int ) – X Start, (in [-inf, inf], optional)

- xend ( int ) – X End, (in [-inf, inf], optional)

- ystart ( int ) – Y Start, (in [-inf, inf], optional)

- yend ( int ) – Y End, (in [-inf, inf], optional)

- flip ( bool ) – Flip, (optional)

- cursor ( int ) – Cursor, Pointer styling to utilize through the dynamic activity (in [0, inf], optional)

- action ( Literal [ 'HIDE' , 'SHOW' ] ) – Visibility Action, If to conceal or expose vertices (optional)

- HIDE
Hide – Conceal vertices.

- SHOW
Show – Expose vertices.

- area ( Literal [ 'OUTSIDE' , 'Inside' ] ) – Visibility Area, Whichever vertices to conceal or expose (optional)

- OUTSIDE
Outside – Conceal or expose vertices outside the choosing.

- Inside
Inside – Conceal or expose vertices inside the choosing.

- use_front_faces_only ( bool ) – Front Faces Only, Modify merely faces addressing toward the observation (optional)

- use_limit_to_segment ( bool ) – Limit to Segment, Employ the motion activity exclusively to the zone that stays enclosed within the progression devoid of magnifying its consequence to the full progression (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
