# mathutils.Matrix: classmethod OrthoProjection ( axis , size , / )

classmethod OrthoProjection ( axis , size , / )

Build a matrix that stands in for an orthographic projection.

Parameters :

- axis ( Literal [ 'X' , 'Y' , 'XY' , 'XZ' , 'YZ' ] | Sequence [ float ] ) – An axis string,
where a single axis is for a 2D matrix.
Or a vector for an arbitrary axis

- size ( int ) – The size of the projection matrix to construct [2, 4].

Returns :

A new projection matrix.

Return type :

Matrix

[Related references](INDEX.md).
