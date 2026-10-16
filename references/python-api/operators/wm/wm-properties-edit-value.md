# bpy.ops.wm.properties_edit_value

bpy.ops.wm. properties_edit_value ( * , data_path = '' , property_name = '' , eval_string = '' ) 

Updates the value of a custom property

Parameters :

- data_path ( str ) – Property Edit, Property data_path edit (optional, never None)

- property_name ( str ) – Property Name, Property name edit (optional, never None)

- eval_string ( str ) – Value, Value for custom property types that can only be edited as a Python expression (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:2096

[Related references](INDEX.md).
