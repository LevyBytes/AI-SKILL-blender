# bpy.ops.view3d.camera_background_image_add

bpy.ops.view3d. camera_background_image_add ( * , filepath = '' , relative_path = True , name = '' , session_uid = 0 ) 

Attaches a fresh background image to the active camera

Parameters :

- filepath ( str ) – Filepath, Path to image file (optional, never None, blend relative // prefix supported)

- relative_path ( bool ) – Relative Path, Select the file relative to the blend file (optional)

- name ( str ) – Name, Name of the data-block to use by the operator (optional, never None)

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
