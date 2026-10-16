# mathutils.geometry: mathutils.geometry. intersect_point_tri_2d ( pt , tri_p1 , tri_p2 , tri_p3 , / )

mathutils.geometry. intersect_point_tri_2d ( pt , tri_p1 , tri_p2 , tri_p3 , / )

Accepts 4 vectors (only their x and y are read): the first is the point, the next 3 lay out the triangle. Returns a non-zero value when the point falls inside the triangle, otherwise 0.

Parameters :

- pt (mathutils.Vector) – Point

- tri_p1 (mathutils.Vector) – First point of the triangle

- tri_p2 (mathutils.Vector) – Second point of the triangle

- tri_p3 (mathutils.Vector) – Third point of the triangle

Returns :

1 if inside with CCW winding, -1 if inside with CW winding, otherwise 0.

Return type :

int

[Related references](INDEX.md).
