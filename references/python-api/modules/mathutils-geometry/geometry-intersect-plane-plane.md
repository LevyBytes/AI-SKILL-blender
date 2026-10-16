# mathutils.geometry: mathutils.geometry. intersect_plane_plane ( plane_a_co , plane_a_no , plane_b_co , plane_b_no , / )

mathutils.geometry. intersect_plane_plane ( plane_a_co , plane_a_no , plane_b_co , plane_b_no , / )

Give back where two planes cross.

Parameters :

- plane_a_co (mathutils.Vector) – Point on the first plane

- plane_a_no (mathutils.Vector) – Normal of the first plane

- plane_b_co (mathutils.Vector) – Point on the second plane

- plane_b_no (mathutils.Vector) – Normal of the second plane

Returns :

The line of the intersection represented as a point and a vector or None if the intersection can't be calculated

Return type :

tuple[mathutils.Vector, mathutils.Vector] | tuple[None, None]

[Related references](INDEX.md).
