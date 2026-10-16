# mathutils.geometry: mathutils.geometry. intersect_sphere_sphere_2d ( p_a , radius_a , p_b , radius_b , / )

mathutils.geometry. intersect_sphere_sphere_2d ( p_a , radius_a , p_b , radius_b , / )

Hands back the 2 points where a pair of circles cross.

Parameters :

- p_a (mathutils.Vector) – Center of the first circle

- radius_a ( float ) – Radius of the first circle

- p_b (mathutils.Vector) – Center of the second circle

- radius_b ( float ) – Radius of the second circle

Returns :

The 2 intersection points or None when there is no intersection.

Return type :

tuple[mathutils.Vector, mathutils.Vector] | tuple[None, None]

[Related references](INDEX.md).
