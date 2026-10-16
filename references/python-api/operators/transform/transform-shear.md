# bpy.ops.transform.shear

bpy.ops.transform. shear ( * , angle = 0.0 , orient_axis = 'Z' , orient_axis_ortho = 'X' , orient_type = 'GLOBAL' , orient_matrix = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)) , orient_matrix_type = 'GLOBAL' , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , gpencil_strokes = False , release_confirm = False , use_accurate = False )

Skew selected items along the specified axis

Parameters :

- angle ( float ) – Angle, (in [-inf, inf], optional)

- orient_axis (Literal[Axis Xyz Items]) – Axis, (optional)

- orient_axis_ortho (Literal[Axis Xyz Items]) – Axis Ortho, (optional)

- orient_type ( str ) – Orientation, Transformation orientation (optional)

- orient_matrix (mathutils.Matrix) – Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)

- orient_matrix_type ( str ) – Matrix Orientation, (optional)

- mirror ( bool ) – Mirror Editing, (optional)

- use_proportional_edit ( bool ) – Proportional Editing, (optional)

- proportional_edit_falloff (Literal[Proportional Falloff Items]) – Proportional Falloff, Falloff type for proportional editing mode (optional)

- proportional_size ( float ) – Proportional Size, (in [1e-06, inf], optional)

- use_proportional_connected ( bool ) – Connected, (optional)

- use_proportional_projected ( bool ) – Projected (2D), (optional)

- snap ( bool ) – Use Snapping Options, (optional)

- gpencil_strokes ( bool ) – Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
