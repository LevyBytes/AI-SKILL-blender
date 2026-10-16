# bpy.ops.object.transform_to_mouse

bpy.ops.object. transform_to_mouse ( * , name = '' , session_uid = 0 , matrix = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)) , drop_x = 0 , drop_y = 0 ) 

Relocate chosen piece(s) to the cursor spot

Parameters :

- name ( str ) – Name, Item designation to put (employs the working item when this and 'session_uid' are empty) (optional, never None)

- session_uid ( int ) – Session UUID, Session UUID of the item to put (employs the working item when this and 'name' are empty) (in [-inf, inf], optional)

- matrix (mathutils.Matrix) – Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)

- drop_x ( int ) – Drop X, X-spot (display area) to put the fresh item under (in [-inf, inf], optional)

- drop_y ( int ) – Drop Y, Y-spot (display area) to put the fresh item under (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
