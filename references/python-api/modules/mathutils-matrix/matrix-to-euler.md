# mathutils.Matrix: to_euler ( order = 'XYZ' , euler_compat = None , / )

to_euler ( order = 'XYZ' , euler_compat = None , / )

Give back an Euler form of the rotation matrix (3x3 or 4x4 matrix only).

Parameters :

- order ( Literal [ 'XYZ' , 'XZY' , 'YXZ' , 'YZX' , 'ZXY' , 'ZYX' ] ) – A rotation order string.

- euler_compat (Euler | None) – Optional euler argument the new euler will be made
compatible with (no axis flipping between them).
Useful for converting a series of matrices to animation curves.

Returns :

Euler representation of the matrix.

Return type :

Euler

[Related references](INDEX.md).
