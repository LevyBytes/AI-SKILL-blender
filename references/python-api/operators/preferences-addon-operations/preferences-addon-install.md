# bpy.ops.preferences.addon_install

bpy.ops.preferences. addon_install ( * , overwrite = True , enable_on_install = False , target = '' , filepath = '' , filter_folder = True , filter_python = True , filter_glob = '*.py;*.zip' ) 

Setup a new add-on

Parameters :

- overwrite ( bool ) – Overwrite, Remove existing add-ons with the same ID (optional)

- enable_on_install ( bool ) – Enable on Install, Enable after installing (optional)

- target ( str ) – Target Path, (optional)

- filepath ( str ) – filepath, (optional, never None)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_python ( bool ) – Filter Python, (optional)

- filter_glob ( str ) – filter_glob, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:712

[Related references](INDEX.md).
