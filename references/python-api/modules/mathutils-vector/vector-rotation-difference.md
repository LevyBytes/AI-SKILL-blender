# mathutils.Vector: rotation_difference ( other , / )

rotation_difference ( other , / ) 

Give a quaternion describing how to turn from this vector to another.

Parameters :

other (Vector) – second vector.

Returns :

how much rotation separates the pair of vectors.

Return type :

Quaternion

Note

Calling this on 2D vectors triggers an AttributeError .

[Related references](INDEX.md).
