# mathutils.Vector: angle_signed ( other , fallback = None , / )

angle_signed ( other , fallback = None , / ) 

Give the signed angle between two 2D vectors, treating clockwise as the positive direction.

Parameters :

- other (Vector) – the second vector the angle is measured against

- fallback ( Any ) – handed back in place of a ValueError whenever the angle is undefined (a zero-length vector).

Returns :

the radian angle, or the supplied fallback instead

Return type :

float | Any

[Related references](INDEX.md).
