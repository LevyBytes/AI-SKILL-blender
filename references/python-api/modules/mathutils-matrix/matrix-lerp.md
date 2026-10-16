# mathutils.Matrix: lerp ( other , factor , / )

lerp ( other , factor , / )

Give back the interpolation between two matrices. This relies on polar decomposition, per "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.

Parameters :

- other (Matrix) – value to interpolate with.

- factor ( float ) – The interpolation value in [0.0, 1.0].

Returns :

The interpolated matrix.

Return type :

Matrix

[Related references](INDEX.md).
