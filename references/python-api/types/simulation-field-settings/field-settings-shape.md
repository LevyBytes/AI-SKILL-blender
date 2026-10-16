# bpy.types.FieldSettings: shape

shape

Which geometry decides where the effector force comes from (default 'POINT' )

- POINT
Point – The field emanates from the object's center.

- LINE
Line – The field emanates from the object's local Z axis.

- PLANE
Plane – The field emanates from the object's local XY plane.

- SURFACE
Surface – The field emanates from the object's surface.

- POINTS
Every Point – The field emanates from every vertex of the object.

Type :

Literal[‘POINT’, ‘LINE’, ‘PLANE’, ‘SURFACE’, ‘POINTS’]

[Related references](INDEX.md).
