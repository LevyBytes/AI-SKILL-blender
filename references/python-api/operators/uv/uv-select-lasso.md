# bpy.ops.uv.select_lasso

bpy.ops.uv. select_lasso ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , mode = 'SET' ) 

Selects UVs by drawing a freehand lasso

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Begin a brand-new selection.

- ADD
Extend – Grow the current selection.

- SUB
Subtract – Shrink the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
