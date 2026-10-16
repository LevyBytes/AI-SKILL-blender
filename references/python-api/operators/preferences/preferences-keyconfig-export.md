# bpy.ops.preferences.keyconfig_export

bpy.ops.preferences. keyconfig_export ( * , all = False , filepath = '' , filter_folder = True , filter_text = True , filter_python = True ) 

Transmit key setup to a Python file

Parameters :

- all ( bool ) – All Keymaps, Write all keymaps (not just user modified) (optional)

- filepath ( str ) – filepath, (optional, never None)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_text ( bool ) – Filter text, (optional)

- filter_python ( bool ) – Filter Python, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:324
bpy.ops.preferences. keyconfig_export ( * , all = False , filepath = '' , filter_folder = True , filter_text = True , filter_python = True )
Exports the key configuration to a Python script.
Parameters:
- all ( bool ) – All Keymaps, Write all keymaps (not just user modified) (optional)
- filepath ( str ) – filepath, (optional, never None)
- filter_folder ( bool ) – Filter folders, (optional)
- filter_text ( bool ) – Filter text, (optional)
- filter_python ( bool ) – Filter Python, (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/userpref.py:324

[Related references](INDEX.md).
