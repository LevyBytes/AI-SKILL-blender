# bpy.ops.file.select

bpy.ops.file.select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, fill=False, open=True, deselect_all=False, only_activate_if_selected=False, pass_through=False)

Take action on clicks to mark and focus items

Parameters:

- wait_to_deselect_others (bool) – Wait to Deselect Others, (optional)
- use_select_on_click (bool) – Act on Click, Instead of marking on click-down, hold up to detect drag. Rather mark on release (optional)
- mouse_x (int) – Mouse X, (in [-inf, inf], optional)
- mouse_y (int) – Mouse Y, (in [-inf, inf], optional)
- extend (bool) – Extend, Grow the roster in lieu of wiping everything (optional)
- fill (bool) – Fill, Mark everything from the previous pick to here (optional)
- open (bool) – Open, Bring up a folder when picking it (optional)
- deselect_all (bool) – Deselect On Nothing, Wipe all choices when nothing sits at the cursor (optional)
- only_activate_if_selected (bool) – Only Activate if Selected, Don't tweak picks if the item at the cursor is picked already, turn on it (optional)
- pass_through (bool) – Pass Through, Permit further input processing upon success (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
