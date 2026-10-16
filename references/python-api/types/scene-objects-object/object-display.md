# bpy.types.Object: display, display_bounds_type, display_type

display 

The object's display options for the 3D viewport (readonly, never None)

Type :

ObjectDisplay
display_bounds_type 

Which boundary shape the object draws (default 'BOX' )

- BOX
Box – Display bounds as box.

- SPHERE
Sphere – Display bounds as sphere.

- CYLINDER
Cylinder – Display bounds as cylinder.

- CONE
Cone – Display bounds as cone.

- CAPSULE
Capsule – Display bounds as capsule.

Type :

Literal[‘BOX’, ‘SPHERE’, ‘CYLINDER’, ‘CONE’, ‘CAPSULE’]
display_type 

The style used to draw the object in the viewport (default 'TEXTURED' )

- BOUNDS
Bounds – Display the bounds of the object.

- WIRE
Wire – Display the object as a wireframe.

- SOLID
Solid – Display the object as a solid (if solid drawing is enabled in the viewport).

- TEXTURED
Textured – Display the object with textures (if textures are enabled in the viewport).

Type :

Literal[‘BOUNDS’, ‘WIRE’, ‘SOLID’, ‘TEXTURED’]

[Related references](INDEX.md).
