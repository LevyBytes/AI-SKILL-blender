# bpy.ops.paint.hide_show_polyline_gesture

bpy.ops.paint. hide_show_polyline_gesture ( * , path = None , action = 'HIDE' , area = 'Inside' , use_front_faces_only = False ) 

Conceal/expose certain vertices

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

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
