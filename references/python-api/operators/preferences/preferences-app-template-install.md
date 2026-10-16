# bpy.ops.preferences.app_template_install

bpy.ops.preferences. app_template_install ( * , overwrite = True , filepath = '' , filter_folder = True , filter_glob = '*.zip' ) 

Install an application template

Parameters :

- overwrite ( bool ) – Overwrite, Remove existing template with the same ID (optional)

- filepath ( str ) – filepath, (optional, never None)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_glob ( str ) – filter_glob, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:1000

[Related references](INDEX.md).
