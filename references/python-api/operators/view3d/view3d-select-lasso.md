# bpy.ops.view3d.select_lasso

bpy.ops.view3d. select_lasso ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , mode = 'SET' ) 

Highlight elements via freehand selection

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) - Path, (optional)

- use_smooth_stroke ( bool ) - Stabilize Stroke, The cursor motion lags and traces a smoother trajectory (optional)

- smooth_stroke_factor ( float ) - Smooth Stroke Factor, Higher settings produce more refined motion paths (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) - Smooth Stroke Radius, Threshold spacing from last point before selection resumes (in [10, 200], optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' , 'XOR' , 'AND' ] ) - Mode, (optional)

- SET
Set - Establishes a new selection.

- ADD
Extend - Expands the current selection.

- SUB
Subtract - Removes from the current selection.

- XOR
Difference - Reverses the selection state.

- AND
Intersect - Keeps only overlapping selections.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
