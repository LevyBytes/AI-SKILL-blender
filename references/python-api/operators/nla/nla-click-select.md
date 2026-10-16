# bpy.ops.nla.click_select

bpy.ops.nla. click_select ( * , wait_to_deselect_others = False , use_select_on_click = False , mouse_x = 0 , mouse_y = 0 , extend = False , deselect_all = False ) 

Manage clicks to mark NLA Sections

Parameters :

- wait_to_deselect_others ( bool ) – Wait to Deselect Others, (optional)

- use_select_on_click ( bool ) – Act on Click, Rather than marking on button, delay to see if there's a drag. Else mark on button lift (optional)

- mouse_x ( int ) – Mouse X, (in [-inf, inf], optional)

- mouse_y ( int ) – Mouse Y, (in [-inf, inf], optional)

- extend ( bool ) – Extend Select, (optional)

- deselect_all ( bool ) – Deselect On Nothing, Unmark everything when nothing beneath the pointer (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
