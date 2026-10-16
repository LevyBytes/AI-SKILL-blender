# bpy.ops.transform.rotate

bpy.ops.transform. rotate ( * , value = 0.0 , orient_axis = 'Z' , orient_type = 'GLOBAL' , orient_matrix = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)) , orient_matrix_type = 'GLOBAL' , constraint_axis = (False, False, False) , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , snap_elements = {'INCREMENT'} , use_snap_project = False , snap_target = 'CLOSEST' , use_snap_self = True , use_snap_edit = True , use_snap_nonedit = True , use_snap_selectable = False , snap_point = (0.0, 0.0, 0.0) , gpencil_strokes = False , center_override = (0.0, 0.0, 0.0) , release_confirm = False , use_accurate = False )

Revolve selected items around an axis

Parameters :

- value ( float ) – Angle, (in [-inf, inf], optional)

- orient_axis (Literal[Axis Xyz Items]) – Axis, (optional)

- orient_type ( str ) – Orientation, Transformation orientation (optional)

- orient_matrix (mathutils.Matrix) – Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)

- orient_matrix_type ( str ) – Matrix Orientation, (optional)

- constraint_axis ( Sequence [ bool ] ) – Constraint Axis, (array of 3 items, optional)

- mirror ( bool ) – Mirror Editing, (optional)

- use_proportional_edit ( bool ) – Proportional Editing, (optional)

- proportional_edit_falloff (Literal[Proportional Falloff Items]) – Proportional Falloff, Falloff type for proportional editing mode (optional)

- proportional_size ( float ) – Proportional Size, (in [1e-06, inf], optional)

- use_proportional_connected ( bool ) – Connected, (optional)

- use_proportional_projected ( bool ) – Projected (2D), (optional)

- snap ( bool ) – Use Snapping Options, (optional)

- snap_elements (set[Literal[Snap Element Items]]) – Snap to Elements, (optional)

- use_snap_project ( bool ) – Project Individual Elements, (optional)

- snap_target (Literal[Snap Source Items]) – Snap Base, Point on source that will snap to target (optional)

- use_snap_self ( bool ) – Target: Include Active, (optional)

- use_snap_edit ( bool ) – Target: Include Edit, (optional)

- use_snap_nonedit ( bool ) – Target: Include Non-Edited, (optional)

- use_snap_selectable ( bool ) – Target: Exclude Non-Selectable, (optional)

- snap_point (mathutils.Vector) – Point, (array of 3 items, in [-inf, inf], optional)

- gpencil_strokes ( bool ) – Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)

- center_override (mathutils.Vector) – Center Override, Force using this center value (when set) (array of 3 items, in [-inf, inf], optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
