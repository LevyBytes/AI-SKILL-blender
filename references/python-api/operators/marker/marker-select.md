# bpy.ops.marker.select

bpy.ops.marker. select ( * , wait_to_deselect_others = False , use_select_on_click = False , mouse_x = 0 , mouse_y = 0 , extend = False , camera = False )

Select time marker(s)

Parameters :

- wait_to_deselect_others ( bool ) – Wait to Deselect Others, (optional)

- use_select_on_click ( bool ) – Act on Click, Rather than selecting on mouse press, wait to see whether a drag follows; otherwise select on release (optional)

- mouse_x ( int ) – Mouse X, (in [-inf, inf], optional)

- mouse_y ( int ) – Mouse Y, (in [-inf, inf], optional)

- extend ( bool ) – Extend, Grow the current selection (optional)

- camera ( bool ) – Camera, Select the camera (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
