# bpy.ops.grease_pencil.erase_lasso

bpy.ops.grease_pencil.erase_lasso ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 )
Delete points within a freehand loop

Parameters:
- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)
- use_smooth_stroke ( bool ) – Stabilize Stroke, Track mouse movement with a delayed, smoothed curve (optional)
- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Higher settings yield a more fluid path (in [0.5, 0.99], optional)
- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Minimum distance traveled before registering movement (in [10, 200], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
