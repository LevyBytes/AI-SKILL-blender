# mathutils.Quaternion: overview

class mathutils. Quaternion ( seq = (1.0, 0.0, 0.0, 0.0) , angle = 0.0 , / )

A handle onto Blender's Quaternions.

Parameters :

- seq ( Sequence [ float ] ) – A (w, x, y, z) quaternion, a 3D exponential map vector,
or a 3D axis vector (when angle is also provided).

- angle ( float ) – rotation angle, in radians

The constructor takes arguments in various forms:

(), no args
Create an identity quaternion

( wxyz )
Create a quaternion from a (w, x, y, z) vector.

( exponential_map )
Create a quaternion from a 3d exponential map vector.

See also

[Related references](INDEX.md).
