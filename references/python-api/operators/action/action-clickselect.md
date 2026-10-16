# bpy.ops.action.clickselect

bpy.ops.action. clickselect ( * , wait_to_deselect_others = False , use_select_on_click = False , mouse_x = 0 , mouse_y = 0 , extend = False , deselect_all = False , column = False , channel = False )

Mark keyframes as chosen via cursor clicks.

Parameters :

- wait_to_deselect_others ( bool ) – Wait to Deselect Others, (optional)

- use_select_on_click ( bool ) – Act on Click, Instead of selecting on mouse press, wait to see if there's drag event. Otherwise select on mouse release (optional)

- mouse_x ( int ) – Mouse X, (in [-inf, inf], optional)

- mouse_y ( int ) – Mouse Y, (in [-inf, inf], optional)

- extend ( bool ) – Extend Select, Add keyframe selections instead of replacing the current set (optional)

- deselect_all ( bool ) – Deselect On Nothing, Unselect everything when the cursor finds nothing (optional)

- column ( bool ) – Column Select, Pick every keyframe on the timeline at the cursor position (optional)

- channel ( bool ) – Only Channel, Mark all keyframes in the channel beneath the cursor (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
