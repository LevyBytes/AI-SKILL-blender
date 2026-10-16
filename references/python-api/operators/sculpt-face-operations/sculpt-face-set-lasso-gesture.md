# bpy.ops.sculpt.face_set_lasso_gesture

bpy.ops.sculpt. face_set_lasso_gesture ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , use_front_faces_only = False )

Establish a face set in a form specified by the cursor

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, Cursor motion lags behind and pursues a softer route (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Greater levels yield softer motion (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Smallest span from prior point prior to resuming motion (in [10, 200], optional)

- use_front_faces_only ( bool ) – Front Faces Only, Influence only surfaces oriented toward the camera (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
