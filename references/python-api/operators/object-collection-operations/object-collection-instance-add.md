# bpy.ops.object.collection_instance_add

bpy.ops.object. collection_instance_add ( * , name = 'Collection' , collection = '' , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) , session_uid = 0 , drop_x = 0 , drop_y = 0 ) 

Introduce a collection replica

Parameters :

- name ( str ) – Name, Collection name to add (optional, never None)

- collection ( str ) – Collection, (optional)

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

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- drop_x ( int ) – Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)

- drop_y ( int ) – Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
