# bpy.ops.graph.clickselect

bpy.ops.graph.clickselect(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, curves=False)

Highlight frames by engaging them

Parameters:

- wait_to_deselect_others (bool) – Wait to Deselect Others, (optional)
- use_select_on_click (bool) – Act on Click, Rather than marking on button-down, hold up to detect drag. Else mark on release (optional)
- mouse_x (int) – Mouse X, (in [-inf, inf], optional)
- mouse_y (int) – Mouse Y, (in [-inf, inf], optional)
- extend (bool) – Extend Select, Flip frame mark rather than emptying newly chosen frames exclusively (optional)
- deselect_all (bool) – Deselect On Nothing, Wipe all choices when nothing sits at the cursor (optional)
- column (bool) – Column Select, Highlight every frame that sits on the equivalent timing as the one at the cursor (optional)
- curves (bool) – Only Curves, Highlight every frame in the trajectory (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
