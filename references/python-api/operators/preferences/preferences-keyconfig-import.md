# bpy.ops.preferences.keyconfig_import

bpy.ops.preferences. keyconfig_import ( * , filepath = 'keymap.py' , filter_folder = True , filter_text = True , filter_python = True , keep_original = True ) 

Ingest key setup from a Python file

Parameters :

- filepath ( str ) – filepath, (optional, never None)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_text ( bool ) – Filter text, (optional)

- filter_python ( bool ) – Filter Python, (optional)

- keep_original ( bool ) – Keep Original, Keep original file after copying to configuration folder (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:259
bpy.ops.preferences. keyconfig_import ( * , filepath = 'keymap.py' , filter_folder = True , filter_text = True , filter_python = True , keep_original = True )
Imports the key configuration from a Python script.
Parameters:
- filepath ( str ) – filepath, (optional, never None)
- filter_folder ( bool ) – Filter folders, (optional)
- filter_text ( bool ) – Filter text, (optional)
- filter_python ( bool ) – Filter Python, (optional)
- keep_original ( bool ) – Keep Original, Keep original file after copying to configuration folder (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/userpref.py:259

[Related references](INDEX.md).
