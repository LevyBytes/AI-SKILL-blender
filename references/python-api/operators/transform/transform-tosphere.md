# bpy.ops.transform.tosphere

bpy.ops.transform. tosphere ( * , value = 0.0 , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , gpencil_strokes = False , center_override = (0.0, 0.0, 0.0) , release_confirm = False , use_accurate = False )
Moves the selected items outward into a spherical shape around the geometric center.
Parameters:
- value ( float ) – Factor, (in [0, 1], optional)
- mirror ( bool ) – Mirror Editing, (optional)
- use_proportional_edit ( bool ) – Proportional Editing, (optional)
- proportional_edit_falloff (Literal[Proportional Falloff Items]) – Proportional Falloff, Falloff type for proportional editing mode (optional)
- proportional_size ( float ) – Proportional Size, (in [1e-06, inf], optional)
- use_proportional_connected ( bool ) – Connected, (optional)
- use_proportional_projected ( bool ) – Projected (2D), (optional)
- snap ( bool ) – Use Snapping Options, (optional)
- gpencil_strokes ( bool ) – Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)
- center_override (mathutils.Vector) – Center Override, Force using this center value (when set) (array of 3 items, in [-inf, inf], optional)
- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)
- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
bpy.ops.transform. tosphere ( * , value = 0.0 , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , gpencil_strokes = False , center_override = (0.0, 0.0, 0.0) , release_confirm = False , use_accurate = False )

Push selected items radially around their center

Parameters :

- value ( float ) – Factor, (in [0, 1], optional)

- mirror ( bool ) – Mirror Editing, (optional)

- use_proportional_edit ( bool ) – Proportional Editing, (optional)

- proportional_edit_falloff (Literal[Proportional Falloff Items]) – Proportional Falloff, Falloff type for proportional editing mode (optional)

- proportional_size ( float ) – Proportional Size, (in [1e-06, inf], optional)

- use_proportional_connected ( bool ) – Connected, (optional)

- use_proportional_projected ( bool ) – Projected (2D), (optional)

- snap ( bool ) – Use Snapping Options, (optional)

- gpencil_strokes ( bool ) – Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)

- center_override (mathutils.Vector) – Center Override, Force using this center value (when set) (array of 3 items, in [-inf, inf], optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
