# mathutils.geometry: mathutils.geometry. intersect_line_plane ( line_a , line_b , plane_co , plane_no , no_flip = False , / )

mathutils.geometry. intersect_line_plane ( line_a , line_b , plane_co , plane_no , no_flip = False , / )

Work out where a line (given as 2 vectors) meets a plane. Gives back a vector at the crossing, or None.

Parameters :

- line_a (mathutils.Vector) – First point of the line

- line_b (mathutils.Vector) – Second point of the line

- plane_co (mathutils.Vector) – A point on the plane

- plane_no (mathutils.Vector) – The direction the plane is facing

- no_flip ( bool ) – Currently ignored.

Returns :

The point of intersection or None when not found

Return type :

mathutils.Vector | None

[Related references](INDEX.md).
