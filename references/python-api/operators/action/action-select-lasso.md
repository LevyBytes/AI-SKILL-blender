# bpy.ops.action.select_lasso

bpy.ops.action. select_lasso ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , mode = 'SET' )

Choose keyframe points with a freehand lasso.

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, Selection trails behind cursor movement for a smoother trajectory (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Greater numbers produce smoother paths (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Minimum offset from the prior point before the selection advances (in [10, 200], optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Establish a new selection.

- ADD
Extend – Enlarge the current selection.

- SUB
Subtract – Shrink the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
