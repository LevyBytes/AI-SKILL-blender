# mathutils.Matrix: classmethod Shear ( plane , size , factor , / )

classmethod Shear ( plane , size , factor , / )

Build a matrix that stands in for a shear transformation.

Parameters :

- plane ( Literal [ 'X' , 'Y' , 'XY' , 'XZ' , 'YZ' ] ) – An axis string,
where a single axis is for a 2D matrix only.

- size ( int ) – The size of the shear matrix to construct [2, 4].

- factor ( float | Sequence [ float ] ) – The factor of shear to apply. For a 2 size matrix use a single float. For a 3 or 4 size matrix pass a pair of floats corresponding with the plane axis.

Returns :

A new shear matrix.

Return type :

Matrix

[Related references](INDEX.md).
