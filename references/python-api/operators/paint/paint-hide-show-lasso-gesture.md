# bpy.ops.paint.hide_show_lasso_gesture

bpy.ops.paint. hide_show_lasso_gesture ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , action = 'HIDE' , area = 'Inside' , use_front_faces_only = False ) 

Conceal/expose certain vertices

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, Choosing delays behind cursor and adheres to a uniformer trajectory (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Increased quantities yield a uniformer stroke (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Reduced gap from preceding spot prior to choosing persists (in [10, 200], optional)

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
