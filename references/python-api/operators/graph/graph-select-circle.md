# bpy.ops.graph.select_circle

bpy.ops.graph.select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', include_handles=True, use_curve_selection=True)

Highlight frame points utilizing round marking

Parameters:

- x (int) – X, (in [-inf, inf], optional)
- y (int) – Y, (in [-inf, inf], optional)
- radius (int) – Radius, (in [1, inf], optional)
- wait_for_input (bool) – Wait for Input, (optional)
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
