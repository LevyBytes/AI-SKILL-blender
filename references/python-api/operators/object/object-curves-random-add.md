# bpy.ops.object.curves_random_add

bpy.ops.object. curves_random_add ( * , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Introduce a curves entity containing arbitrary curve data to the viewport

Parameters :

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

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
