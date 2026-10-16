# mathutils.geometry: mathutils.geometry. intersect_point_tri ( pt , tri_p1 , tri_p2 , tri_p3 , / )

mathutils.geometry. intersect_point_tri ( pt , tri_p1 , tri_p2 , tri_p3 , / )

Accepts 4 vectors: the first is the point, the next 3 lay out the triangle. Drops the point onto the triangle's plane and tests whether it lands inside the triangle.

Parameters :

- pt (mathutils.Vector) – Point

- tri_p1 (mathutils.Vector) – First point of the triangle

- tri_p2 (mathutils.Vector) – Second point of the triangle

- tri_p3 (mathutils.Vector) – Third point of the triangle

Returns :

Point on the triangle's plane or None if it's outside the triangle

Return type :

mathutils.Vector | None

[Related references](INDEX.md).
