# bpy.ops.paint.hide_show

bpy.ops.paint. hide_show ( * , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , action = 'HIDE' , area = 'Inside' , use_front_faces_only = False ) 

Conceal/expose certain vertices

Parameters :

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

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

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
