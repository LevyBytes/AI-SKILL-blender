# bpy.ops.object.add_named

bpy.ops.object. add_named ( * , linked = False , name = '' , session_uid = 0 , matrix = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)) , drop_x = 0 , drop_y = 0 ) 

Introduce a named entity

Parameters :

- linked ( bool ) – Linked, Duplicate object but not object data, linking to the original data (optional)

- name ( str ) – Name, Name of the data-block to use by the operator (optional, never None)

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- matrix (mathutils.Matrix) – Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)

- drop_x ( int ) – Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)

- drop_y ( int ) – Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
