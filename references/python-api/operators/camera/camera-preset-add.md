# bpy.ops.camera.preset_add

bpy.ops.camera. preset_add ( * , name = '' , remove_name = False , remove_active = False , use_focal_length = False )

Add or remove a Camera Preset

Parameters :

- name ( str ) – Name, Name of the preset, used to make the path name (optional, never None)

- remove_name ( bool ) – remove_name, (optional)

- remove_active ( bool ) – remove_active, (optional)

- use_focal_length ( bool ) – Include Focal Length, Include focal length into the preset (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/presets.py:119

[Related references](INDEX.md).
