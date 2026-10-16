# mathutils.Matrix: inverted_safe ( )

inverted_safe ( )

Give back an inverted copy of the matrix, never raising an error. When the matrix is degenerate (say a zero scale on one axis), a small epsilon is added to its diagonal to make it invertible. Should the adjusted matrix still be degenerate, the identity matrix is returned instead.

Returns :

the inverted matrix.

Return type :

Matrix

[Related references](INDEX.md).
