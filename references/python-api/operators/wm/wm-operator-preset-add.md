# bpy.ops.wm.operator_preset_add

bpy.ops.wm. operator_preset_add ( * , name = '' , remove_name = False , remove_active = False , operator = '' ) 

Adds or removes an Operator Preset

Parameters :

- name ( str ) – Name, Title of the preset, becomes the path name (optional, never None)

- remove_name ( bool ) – remove_name, (optional)

- remove_active ( bool ) – remove_active, (optional)

- operator ( str ) – Operator, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/presets.py:119

[Related references](INDEX.md).
