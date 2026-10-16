# mathutils.Vector: angle ( other , fallback = None , / )

angle ( other , fallback = None , / ) 

Give the angle separating this vector and a second one.

Note

On 4D vectors only the x, y and z parts factor in.

Parameters :

- other (Vector) – the second vector the angle is measured against

- fallback ( Any ) – handed back in place of a ValueError whenever the angle is undefined (a zero-length vector).

Returns :

the radian angle, or the supplied fallback instead

Return type :

float | Any

[Related references](INDEX.md).
