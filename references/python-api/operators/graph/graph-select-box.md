# bpy.ops.graph.select_box

bpy.ops.graph.select_box(*, axis_range=False, include_handles=True, tweak=False, use_curve_selection=True, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

Highlight every frame in the given zone

Parameters:

- axis_range (bool) – Axis Range, (optional)
- include_handles (bool) – Include Handles, Are grips checked separately alongside the pick requirement, independently from their components. When deactivated, grips are (un)marked in unison with their components (optional)
- tweak (bool) – Tweak, Business has been engaged utilizing a press-drag occurrence (optional)
- use_curve_selection (bool) – Select Curves, Grant marking every frame of a trajectory by marking the computed trajectory (optional)
- xmin (int) – X Min, (in [-inf, inf], optional)
- xmax (int) – X Max, (in [-inf, inf], optional)
- ymin (int) – Y Min, (in [-inf, inf], optional)
- ymax (int) – Y Max, (in [-inf, inf], optional)
- wait_for_input (bool) – Wait for Input, (optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)

- SET
Set – Set a new selection.

- ADD
Extend – Extend existing selection.

- SUB
Subtract – Subtract existing selection.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
