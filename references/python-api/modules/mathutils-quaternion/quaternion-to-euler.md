# mathutils.Quaternion.to_euler

to_euler ( order = 'XYZ' , euler_compat = None , / )

Give back the Euler form of the quaternion.

Parameters :

- order ( Literal [ 'XYZ' , 'XZY' , 'YXZ' , 'YZX' , 'ZXY' , 'ZYX' ] ) – Rotation order.

- euler_compat (Euler | None) – Optional euler argument the new euler will be made
compatible with (no axis flipping between them).
Useful for converting a series of quaternions to animation curves.

Returns :

Euler representation of the quaternion.

Return type :

Euler

[Related references](INDEX.md).
