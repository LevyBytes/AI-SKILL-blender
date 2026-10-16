# bpy.ops.gizmogroup.gizmo_select

bpy.ops.gizmogroup.gizmo_select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False)

Mark the presently pointed gizmo

Parameters:

- extend (bool) – Extend, Grow the roster in lieu of wiping everything (optional)
- deselect (bool) – Deselect, Purge from the roster (optional)
- toggle (bool) – Toggle Selection, Flip the mark (optional)
- deselect_all (bool) – Deselect On Nothing, Wipe all marks when nothing sits at the cursor (optional)
- select_passthrough (bool) – Only Select Unselected, Skip the mark work when the part is picked already (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
