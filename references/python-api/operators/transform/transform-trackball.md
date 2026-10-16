# bpy.ops.transform.trackball

bpy.ops.transform. trackball ( * , value = (0.0, 0.0) , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , gpencil_strokes = False , center_override = (0.0, 0.0, 0.0) , release_confirm = False , use_accurate = False )
Rotates the selected items in trackball style.
Parameters:
- value ( Sequence [ float ] ) – Angle, (array of 2 items, in [-inf, inf], optional)
bpy.ops.transform. trackball ( * , value = (0.0, 0.0) , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , gpencil_strokes = False , center_override = (0.0, 0.0, 0.0) , release_confirm = False , use_accurate = False )

Trackball-style rotation of selected items

Parameters :

- value ( Sequence [ float ] ) – Angle, (array of 2 items, in [-inf, inf], optional)

- snap_elements (set[Literal[Snap Element Items]]) – Snap to Elements, (optional)

- use_snap_project ( bool ) – Project Individual Elements, (optional)

- snap_target (Literal[Snap Source Items]) – Snap Base, Point on source that will snap to target (optional)

- use_snap_self ( bool ) – Target: Include Active, (optional)

- use_snap_edit ( bool ) – Target: Include Edit, (optional)

- use_snap_nonedit ( bool ) – Target: Include Non-Edited, (optional)

- use_snap_selectable ( bool ) – Target: Exclude Non-Selectable, (optional)

- snap_point (mathutils.Vector) – Point, (array of 3 items, in [-inf, inf], optional)

- snap_align ( bool ) – Align with Point Normal, (optional)

- snap_normal (mathutils.Vector) – Normal, (array of 3 items, in [-inf, inf], optional)

- gpencil_strokes ( bool ) – Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)

- cursor_transform ( bool ) – Transform Cursor, (optional)

- texture_space ( bool ) – Edit Texture Space, Edit object data texture space (optional)

- remove_on_cancel ( bool ) – Remove on Cancel, Remove elements on cancel (optional)

- use_duplicated_keyframes ( bool ) – Duplicated Keyframes, Transform duplicated keyframes (optional)

- view2d_edge_pan ( bool ) – Edge Pan, Enable edge panning in 2D view (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

- use_automerge_and_split ( bool ) – Auto Merge & Split, Forces the use of Auto Merge and Split (optional)

- translate_origin ( bool ) – Translate Origin, Translate origin instead of selection (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
