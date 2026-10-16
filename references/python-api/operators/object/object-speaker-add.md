# bpy.ops.object.speaker_add

bpy.ops.object. speaker_add ( * , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Put a speaker into the workspace

Parameters :

- enter_editmode ( bool ) – Enter Edit Mode, Open edit mode right after inserting this item (optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, Where the fresh item sits (optional)

- WORLD
World – Position the fresh item with respect to the world axes.

- VIEW
View – Position the fresh item with respect to the viewport.

- CURSOR
3D Cursor – Employ the 3D cursor's orientation for the fresh item.

- location (mathutils.Vector) – Location, Where the inserted item goes (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, How the inserted item is oriented (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, How the inserted item is sized (array of 3 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
