# bpy.ops.sequencer.select

bpy.ops.sequencer.select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, linked_handle=False, linked_time=False, side_of_frame=False, ignore_connections=False)

Choose a piece (most recent picked becomes the "active piece").

Parameters:

- wait_to_deselect_others (bool) – Wait to Deselect Others, (optional)
- use_select_on_click (bool) – Act on Click, Rather than pick on press, hold to see drag. Otherwise pick on release (optional)
- mouse_x (int) – Mouse X, (in [-inf, inf], optional)
- mouse_y (int) – Mouse Y, (in [-inf, inf], optional)
- extend (bool) – Extend, Add to choice instead of clearing prior choice (optional)
- deselect (bool) – Deselect, Remove from choice (optional)
- toggle (bool) – Toggle Selection, Switch choice state (optional)
- deselect_all (bool) – Deselect On Nothing, Clear all choice when pointer is empty (optional)
- select_passthrough (bool) – Only Select Unselected, Disregard the pick action when the piece is previously chosen (optional)
- center (bool) – Center, Use the piece midpoint when picking, in composition mode apply to grow piece choice (optional)
- linked_handle (bool) – Linked Handle, Pick locations next to the active piece (optional)
- linked_time (bool) – Linked Time, Pick other pieces or locations at the same moment, or all speed-adjustment points after the active in speed-adjustment mode (optional)
- side_of_frame (bool) – Side of Frame, Pick all pieces on same direction of the current picture as the pointer (optional)
- ignore_connections (bool) – Ignore Connections, Pick pieces independently regardless of connection state (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, linked_handle=False, linked_time=False, side_of_frame=False, ignore_connections=False)

Choose a piece (most recent picked becomes the "active piece").

Parameters:

- wait_to_deselect_others (bool) – Wait to Deselect Others, (optional)
- use_select_on_click (bool) – Act on Click, Rather than pick on press, hold to see drag. Otherwise pick on release (optional)
- mouse_x (int) – Mouse X, (in [-inf, inf], optional)
- mouse_y (int) – Mouse Y, (in [-inf, inf], optional)
- extend (bool) – Extend, Add to choice instead of clearing prior choice (optional)
- deselect (bool) – Deselect, Remove from choice (optional)
- toggle (bool) – Toggle Selection, Switch choice state (optional)
- deselect_all (bool) – Deselect On Nothing, Clear all choice when pointer is empty (optional)
- select_passthrough (bool) – Only Select Unselected, Disregard the pick action when the piece is previously chosen (optional)
- center (bool) – Center, Use the piece midpoint when picking, in composition mode apply to grow piece choice (optional)
- linked_handle (bool) – Linked Handle, Pick locations next to the active piece (optional)
- linked_time (bool) – Linked Time, Pick other pieces or locations at the same moment, or all speed-adjustment points after the active in speed-adjustment mode (optional)
- side_of_frame (bool) – Side of Frame, Pick all pieces on same direction of the current picture as the pointer (optional)
- ignore_connections (bool) – Ignore Connections, Pick pieces independently regardless of connection state (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
