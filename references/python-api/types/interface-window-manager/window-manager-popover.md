# bpy.types.WindowManager: popover_begin__internal, popover_end__internal, popover

classmethod popover_begin__internal ( * , ui_units_x = 0 , from_active_button = False )

popover_begin__internal

Parameters :

- ui_units_x ( int ) – ui_units_x, (in [0, inf], optional)

- from_active_button ( bool ) – Use Button, Use the active button for positioning (optional)

Returns :

(never None)

Return type :

UIPopover
classmethod popover_end__internal ( menu , * , keymap = None )

popover_end__internal

Parameters :

- menu (UIPopover) – (never None)

- keymap (KeyMap) – Key Map, Active key map (optional)
popover ( draw_func , * , ui_units_x = 0 , keymap = None , from_active_button = False )

[Related references](INDEX.md).
