# mathutils.geometry: mathutils.geometry. intersect_ray_tri ( v1 , v2 , v3 , ray , orig , clip = True , / )

mathutils.geometry. intersect_ray_tri ( v1 , v2 , v3 , ray , orig , clip = True , / )

Hands back where a ray meets a triangle when such a meeting exists, otherwise None.

Parameters :

- v1 (mathutils.Vector) – Point1

- v2 (mathutils.Vector) – Point2

- v3 (mathutils.Vector) – Point3

- ray (mathutils.Vector) – Direction of the ray

- orig (mathutils.Vector) – Origin

- clip ( bool ) – When False, don't restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle.

Returns :

The point of intersection or None if no intersection is found

Return type :

mathutils.Vector | None

[Related references](INDEX.md).
