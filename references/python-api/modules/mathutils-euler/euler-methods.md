# mathutils.Euler: methods

copy ( )

Returns a copy of this euler.

Returns :

A copy of the euler.

Return type :

Euler

Note

reach for this when you need a standalone copy of a wrapped euler that no longer points back at the source.
freeze ( )

Lock this object so it can no longer change.

Once locked, it becomes hashable and usable as a dictionary or set member.

Returns :

An instance of this object.

Return type :

Self
make_compatible ( other , / )

Bring this euler into line with another so that interpolating across the two behaves the way you'd expect.

Parameters :

other (Euler) – Other euler rotation.

Note

the rotation order is not taken into account for this function.
rotate ( other , / )

Rotate the euler by some other mathutils value.

Parameters :

other (Euler | Quaternion | Matrix) – rotation component of mathutils value
rotate_axis ( axis , angle , / )

Turn the euler by a set amount, then wrap the outcome so it stays a single distinct euler rotation (no 720 degree pitches).

Parameters :

- axis ( Literal [ 'X' , 'Y' , 'Z' ] ) – An axis string.

- angle ( float ) – angle in radians.
to_matrix ( )

Give the euler back as a matrix.

Returns :

A 3x3 rotation matrix representation of the euler.

Return type :

Matrix
to_quaternion ( )

Give the euler back as a quaternion.

Returns :

Quaternion representation of the euler.

Return type :

Quaternion
zero ( )

Reset every value to zero.

[Related references](INDEX.md).
