# bpy.ops.object.lightprobe_add

bpy.ops.object. lightprobe_add ( * , type = 'SPHERE' , radius = 1.0 , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Insert a light-sampling instrument into the scene

Parameters :

- type ( Literal [ 'SPHERE' , 'PLANE' , 'VOLUME' ] ) – Type, (optional)

- SPHERE
Sphere – Probe capturing directional brightness samples everywhere around a point.

- PLANE
Plane – Probe sampling incoming radiance across a flat area.

- VOLUME
Volume – Probe for storing coarse radiance within a bounded region.

- radius ( float ) – Radius, (in [0, inf], optional)

- enter_editmode ( bool ) – Enter Edit Mode, Switch to edit mode immediately after creation (optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, Direction the inserted object will face (optional)

- WORLD
World – Orient the object to global axes.

- VIEW
View – Orient the object to match the camera view.

- CURSOR
3D Cursor – Use the 3D cursor's orientation for the object.

- location (mathutils.Vector) – Location, Placement point for the newly inserted object (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, Orientation to apply when inserting the object (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, Size scaling during insertion (array of 3 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
