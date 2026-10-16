# mathutils.Matrix: classmethod Rotation ( angle , size , axis , / )

classmethod Rotation ( angle , size , axis , / )

Build a matrix that stands in for a rotation.

Parameters :

- angle ( float ) – The angle of rotation desired, in radians.

- size ( int ) – The size of the rotation matrix to construct [2, 4].

- axis ( Literal [ 'X' , 'Y' , 'Z' ] | Sequence [ float ] ) – an axis string or a 3D Vector Object
(optional when size is 2).

Returns :

A new rotation matrix.

Return type :

Matrix

[Related references](INDEX.md).
