# mathutils.Matrix: invert_safe ( )

invert_safe ( )

Replace the matrix with its inverse, never raising an error. When the matrix is degenerate (say a zero scale on one axis), a small epsilon is added to its diagonal to make it invertible. Should the adjusted matrix still be degenerate, the identity matrix is used instead.

See also

Inverse Matrix on Wikipedia.

[Related references](INDEX.md).
