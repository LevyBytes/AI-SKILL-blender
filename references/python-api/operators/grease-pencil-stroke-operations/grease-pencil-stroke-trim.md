# bpy.ops.grease_pencil.stroke_trim

bpy.ops.grease_pencil.stroke_trim ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 )
Erase stroke points lying between crossing segments

Parameters:
- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)
- use_smooth_stroke ( bool ) – Stabilize Stroke, Apply delayed smoothing to the selection trace (optional)
- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Higher settings yield smoother traces (in [0.5, 0.99], optional)
- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Minimum distance traveled before registering movement (in [10, 200], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
