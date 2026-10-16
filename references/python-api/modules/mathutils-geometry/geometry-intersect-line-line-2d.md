# mathutils.geometry: mathutils.geometry. intersect_line_line_2d ( lineA_p1 , lineA_p2 , lineB_p1 , lineB_p2 , / )

mathutils.geometry. intersect_line_line_2d ( lineA_p1 , lineA_p2 , lineB_p1 , lineB_p2 , / )

Accepts 2 segments (laid out by 4 vectors) and gives back a vector at their crossing point, or None.

Warning

Despite its name, this function works on segments, and not on lines.

Parameters :

- lineA_p1 (mathutils.Vector) – First point of the first segment

- lineA_p2 (mathutils.Vector) – Second point of the first segment

- lineB_p1 (mathutils.Vector) – First point of the second segment

- lineB_p2 (mathutils.Vector) – Second point of the second segment

Returns :

The point of intersection or None when not found

Return type :

mathutils.Vector | None

[Related references](INDEX.md).
