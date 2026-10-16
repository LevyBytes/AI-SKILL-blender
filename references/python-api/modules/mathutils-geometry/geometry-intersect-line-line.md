# mathutils.geometry: mathutils.geometry. intersect_line_line ( v1 , v2 , v3 , v4 , / )

mathutils.geometry. intersect_line_line ( v1 , v2 , v3 , v4 , / )

Gives a tuple holding, on each line, the point that sits closest to the other line.

Parameters :

- v1 (mathutils.Vector) – First point of the first line

- v2 (mathutils.Vector) – Second point of the first line

- v3 (mathutils.Vector) – First point of the second line

- v4 (mathutils.Vector) – Second point of the second line

Returns :

The intersection on each line or None when the lines are parallel.

Return type :

tuple[mathutils.Vector, mathutils.Vector] | None

[Related references](INDEX.md).
