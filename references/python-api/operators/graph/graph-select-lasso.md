# bpy.ops.graph.select_lasso

bpy.ops.graph.select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET', include_handles=True, use_curve_selection=True)

Highlight frame points utilizing noose marking

Parameters:

- path (bpy_prop_collection[OperatorMousePath]) – Path, (optional)
- use_smooth_stroke (bool) – Stabilize Stroke, Mark lags at your cursor and adheres a sleeker course (optional)
- smooth_stroke_factor (float) – Smooth Stroke Factor, Taller amounts provide a sleeker stroke (in [0.5, 0.99], optional)
- smooth_stroke_radius (int) – Smooth Stroke Radius, Least separation from the preceding spot ahead of marking continues (in [10, 200], optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)

- SET
Set – Set a new selection.

- ADD
Extend – Extend existing selection.

- SUB
Subtract – Subtract existing selection.

- include_handles (bool) – Include Handles, Are grips checked separately alongside the pick requirement, independently from their components. When deactivated, grips are (un)marked in unison with their components (optional)
- use_curve_selection (bool) – Select Curves, Grant marking every frame of a trajectory by marking the trajectory itself (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
