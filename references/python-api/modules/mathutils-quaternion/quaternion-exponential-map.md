# mathutils.Quaternion.to_exponential_map

to_exponential_map ( ) 

Hand back the quaternion expressed as an exponential map.

The encoding holds the axis of rotation already scaled by how far the rotation turns.
Storing orientation this way makes blending across several rotations convenient.

Returns :

3D exponential map.

Return type :

Vector

Feed the result into the Quaternion constructor to recover the original quaternion.

[Related references](INDEX.md).
