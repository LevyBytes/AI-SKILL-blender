# bpy.ops.ui.view_item_select

bpy.ops.ui. view_item_select ( * , wait_to_deselect_others = False , use_select_on_click = False , mouse_x = 0 , mouse_y = 0 , extend = False , range_select = False ) 

Makes the chosen view item active

Parameters :

- wait_to_deselect_others ( bool ) – Wait to Deselect Others, (optional)

- use_select_on_click ( bool ) – Act on Click, Instead of selecting on mouse press, wait to see if there’s drag event. Otherwise select on mouse release (optional)

- mouse_x ( int ) – Mouse X, (in [-inf, inf], optional)

- mouse_y ( int ) – Mouse Y, (in [-inf, inf], optional)

- extend ( bool ) – extend, Extend Selection (optional)

- range_select ( bool ) – Range Select, Select all between clicked and active items (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
