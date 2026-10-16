# mathutils.Vector: slerp ( other , factor , fallback = None , / )

slerp ( other , factor , fallback = None , / ) 

Blend between two non-zero vectors along the sphere (spherical interpolation).

Parameters :

- other (Vector) – the target the blend runs toward.

- factor ( float ) – Blend weight, usually somewhere from 0.0 to 1.0.

- fallback ( Any ) – handed back rather than raising a ValueError when the result is undefined (a zero-length vector, or exact opposites).

Returns :

The interpolated vector.

Return type :

Vector

[Related references](INDEX.md).
