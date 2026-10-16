# bpy.ops.mask.select_lasso

bpy.ops.mask. select_lasso ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , mode = 'SET' )

Select curve points using lasso selection

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, The selection trails the mouse and follows a smoother route (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Larger values produce a smoother stroke (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Shortest distance from the last point before selection carries on (in [10, 200], optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Start a fresh selection.

- ADD
Extend – Add to the current selection.

- SUB
Subtract – Remove from the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
