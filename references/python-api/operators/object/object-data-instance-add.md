# bpy.ops.object.data_instance_add

bpy.ops.object. data_instance_add ( * , name = '' , session_uid = 0 , type = 'ACTION' , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) , drop_x = 0 , drop_y = 0 ) 

Introduce an entity representation duplicate

Parameters :

- name ( str ) – Name, Name of the data-block to use by the operator (optional, never None)

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- type (Literal[Id Type Items]) – Type, (optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, The alignment of the new object (optional)

- WORLD
World – Align the new object to the world.

- VIEW
View – Align the new object to the view.

- CURSOR
3D Cursor – Use the 3D cursor orientation for the new object.

- location (mathutils.Vector) – Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)

- drop_x ( int ) – Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)

- drop_y ( int ) – Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
