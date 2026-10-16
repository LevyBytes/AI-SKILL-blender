# mathutils.geometry: mathutils.geometry. intersect_point_line ( pt , line_p1 , line_p2 , / )

mathutils.geometry. intersect_point_line ( pt , line_p1 , line_p2 , / )

Accepts a point and a line, returning the nearest point on the line plus how far along it sits from the line's first point. Here 0.0 marks the first point and 1.0 the second; anything outside [0, 1] is extrapolated.

Parameters :

- pt (mathutils.Vector) – Point

- line_p1 (mathutils.Vector) – First point of the line

- line_p2 (mathutils.Vector) – Second point of the line

Returns :

The closest point on the line and its parametric distance from the first point.

Return type :

tuple[mathutils.Vector, float]

[Related references](INDEX.md).
