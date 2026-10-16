# bpy.ops.preferences.theme_install

bpy.ops.preferences. theme_install ( * , overwrite = True , filepath = '' , filter_folder = True , filter_glob = '*.xml' ) 

Ingest and employ a Blender XML theme file

Parameters :

- overwrite ( bool ) – Overwrite, Remove existing theme file if exists (optional)

- filepath ( str ) – filepath, (optional, never None)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_glob ( str ) – filter_glob, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:598
bpy.ops.preferences. theme_install ( * , overwrite = True , filepath = '' , filter_folder = True , filter_glob = '*.xml' )
Loads and applies a Blender XML theme file.
Parameters:
- overwrite ( bool ) – Overwrite, Remove existing theme file if exists (optional)
- filepath ( str ) – filepath, (optional, never None)
- filter_folder ( bool ) – Filter folders, (optional)
- filter_glob ( str ) – filter_glob, (optional, never None)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/userpref.py:598

[Related references](INDEX.md).
