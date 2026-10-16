# mathutils.geometry: mathutils.geometry. intersect_point_quad_2d ( pt , quad_p1 , quad_p2 , quad_p3 , quad_p4 , / )

mathutils.geometry. intersect_point_quad_2d ( pt , quad_p1 , quad_p2 , quad_p3 , quad_p4 , / )

Accepts 5 vectors (only their x and y are read): the first is the point, the next 4 lay out the quad. Returns a non-zero value when the point falls inside the quad, otherwise 0. Only convex quads free of singular edges are handled.

Parameters :

- pt (mathutils.Vector) – Point

- quad_p1 (mathutils.Vector) – First point of the quad

- quad_p2 (mathutils.Vector) – Second point of the quad

- quad_p3 (mathutils.Vector) – Third point of the quad

- quad_p4 (mathutils.Vector) – Fourth point of the quad

Returns :

1 if inside with CCW winding, -1 if inside with CW winding, otherwise 0.

Return type :

int

[Related references](INDEX.md).
