# bpy.ops.object.effector_add

bpy.ops.object. effector_add ( * , type = 'FORCE' , radius = 1.0 , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Introduce a blank entity housing a force mechanism to the viewport

Parameters :

- type ( Literal [ 'FORCE' , 'WIND' , 'VORTEX' , 'MAGNET' , 'HARMONIC' , 'CHARGE' , 'LENNARDJ' , 'TEXTURE' , 'GUIDE' , 'BOID' , 'TURBULENCE' , 'DRAG' , 'FLUID' ] ) – Type, (optional)

- radius ( float ) – Radius, (in [0, inf], optional)

- enter_editmode ( bool ) – Enter Edit Mode, Enter edit mode when adding this object (optional)

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
