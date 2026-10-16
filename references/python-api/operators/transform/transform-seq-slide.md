# bpy.ops.transform.seq_slide

bpy.ops.transform. seq_slide ( * , value = (0.0, 0.0) , use_restore_handle_selection = False , snap = False , texture_space = False , remove_on_cancel = False , use_duplicated_keyframes = False , view2d_edge_pan = False , release_confirm = False , use_accurate = False )

Move a sequence strip in the timeline

Parameters :

- value (mathutils.Vector) – Offset, (array of 2 items, in [-inf, inf], optional)

- use_restore_handle_selection ( bool ) – Restore Handle Selection, Restore handle selection after tweaking (optional)

- snap ( bool ) – Use Snapping Options, (optional)

- texture_space ( bool ) – Edit Texture Space, Edit object data texture space (optional)

- remove_on_cancel ( bool ) – Remove on Cancel, Remove elements on cancel (optional)

- use_duplicated_keyframes ( bool ) – Duplicated Keyframes, Transform duplicated keyframes (optional)

- view2d_edge_pan ( bool ) – Edge Pan, Enable edge panning in 2D view (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
