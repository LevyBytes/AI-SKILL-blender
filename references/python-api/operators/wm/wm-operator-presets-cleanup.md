# bpy.ops.wm.operator_presets_cleanup

bpy.ops.wm. operator_presets_cleanup ( * , operator = '' , properties = None ) 

Eliminates obsolete operator settings from presets that could generate issues

Parameters :

- operator ( str ) – operator, (optional, never None)

- properties ( bpy_prop_collection [ OperatorFileListElement ]) – properties, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/presets.py:924

[Related references](INDEX.md).
