# bpy.ops.object.grease_pencil_add

bpy.ops.object. grease_pencil_add ( * , type = 'EMPTY' , use_in_front = True , stroke_depth_offset = 0.05 , use_lights = True , stroke_depth_order = '3D' , radius = 1.0 , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Insert a Grease Pencil sketch layer into the workspace

Parameters :

- type (Literal[Object Gpencil Type Items]) – Type, (optional)

- use_in_front ( bool ) – Show In Front, Render Line Art Grease Pencil atop all objects in the viewport (optional)

- stroke_depth_offset ( float ) – Stroke Offset, Vertical spacing parameter for the Line Art modifier (in [0, inf], optional)

- use_lights ( bool ) – Use Lights, Illumination affects this Grease Pencil layer (optional)

- stroke_depth_order ( Literal [ '2D' , '3D' ] ) – Stroke Depth Order, Determines ordering approach for strokes in three-dimensional areas (for layers not shown 'In Front') (optional)

- 2D
2D Layers – Render strokes using layer stacking to determine sequence.

- 3D
3D Location – Display strokes using true spatial positioning.

- radius ( float ) – Radius, (in [0, inf], optional)

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
