# bpy.ops.wm.radial_control

bpy.ops.wm. radial_control ( * , data_path_primary = '' , data_path_secondary = '' , use_secondary = '' , rotation_path = '' , color_path = '' , fill_color_path = '' , fill_color_override_path = '' , fill_color_override_test_path = '' , zoom_path = '' , image_id = '' , secondary_tex = False , release_confirm = False ) 

Adjusts size-related attributes (such as brush radius) using the mouse wheel

Parameters :

- data_path_primary ( str ) – Primary Data Path, Primary path of property to be set by the radial control (optional, never None)

- data_path_secondary ( str ) – Secondary Data Path, Secondary path of property to be set by the radial control (optional, never None)

- use_secondary ( str ) – Use Secondary, Path of property to select between the primary and secondary data paths (optional, never None)

- rotation_path ( str ) – Rotation Path, Path of property used to rotate the texture display (optional, never None)

- color_path ( str ) – Color Path, Path of property used to set the color of the control (optional, never None)

- fill_color_path ( str ) – Fill Color Path, Path of property used to set the fill color of the control (optional, never None)

- fill_color_override_path ( str ) – Fill Color Override Path, (optional, never None)

- fill_color_override_test_path ( str ) – Fill Color Override Test, (optional, never None)

- zoom_path ( str ) – Zoom Path, Path of property used to set the zoom level for the control (optional, never None)

- image_id ( str ) – Image ID, Path of ID that is used to generate an image for the control (optional, never None)

- secondary_tex ( bool ) – Secondary Texture, Modify brush secondary/mask texture (optional)

- release_confirm ( bool ) – Confirm On Release, Finish operation on key release (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
