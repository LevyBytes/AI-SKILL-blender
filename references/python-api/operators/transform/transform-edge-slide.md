# bpy.ops.transform.edge_slide

bpy.ops.transform. edge_slide ( * , value = 0.0 , single_side = False , use_even = False , flipped = False , use_clamp = True , mirror = False , snap = False , snap_elements = {'INCREMENT'} , use_snap_project = False , snap_target = 'CLOSEST' , use_snap_self = True , use_snap_edit = True , use_snap_nonedit = True , use_snap_selectable = False , snap_point = (0.0, 0.0, 0.0) , correct_uv = True , release_confirm = False , use_accurate = False )

Glide an edge loop along a mesh surface

Parameters :

- value ( float ) – Factor, (in [-10, 10], optional)

- single_side ( bool ) – Single Side, (optional)

- use_even ( bool ) – Even, Make the edge loop match the shape of the adjacent edge loop (optional)

- flipped ( bool ) – Flipped, When Even mode is active, flips between the two adjacent edge loops (optional)

- use_clamp ( bool ) – Clamp, Clamp within the edge extents (optional)

- mirror ( bool ) – Mirror Editing, (optional)

- snap ( bool ) – Use Snapping Options, (optional)

- snap_elements (set[Literal[Snap Element Items]]) – Snap to Elements, (optional)

- use_snap_project ( bool ) – Project Individual Elements, (optional)

- snap_target (Literal[Snap Source Items]) – Snap Base, Point on source that will snap to target (optional)

- use_snap_self ( bool ) – Target: Include Active, (optional)

- use_snap_edit ( bool ) – Target: Include Edit, (optional)

- use_snap_nonedit ( bool ) – Target: Include Non-Edited, (optional)

- use_snap_selectable ( bool ) – Target: Exclude Non-Selectable, (optional)

- snap_point (mathutils.Vector) – Point, (array of 3 items, in [-inf, inf], optional)

- correct_uv ( bool ) – Correct UVs, Correct UV coordinates when transforming (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
