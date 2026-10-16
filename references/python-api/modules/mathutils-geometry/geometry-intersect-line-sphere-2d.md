# mathutils.geometry: mathutils.geometry. intersect_line_sphere_2d ( line_a , line_b , sphere_co , sphere_radius , clip = True , / )

mathutils.geometry. intersect_line_sphere_2d ( line_a , line_b , sphere_co , sphere_radius , clip = True , / )

Accepts a line (as 2 points) plus a circle (a point and a radius) and hands back where they meet.

Parameters :

- line_a (mathutils.Vector) – First point of the line

- line_b (mathutils.Vector) – Second point of the line

- sphere_co (mathutils.Vector) – The center of the circle

- sphere_radius ( float ) – Radius of the circle

- clip ( bool ) – When False, don't restrict the intersection to the line segment.

Returns :

The intersection points as a pair of vectors (each is None when not found).

Return type :

tuple[mathutils.Vector | None, mathutils.Vector | None]

[Related references](INDEX.md).
