# mathutils.Quaternion.to_swing_twist

to_swing_twist ( axis , / ) 

Separate the rotation into a swing part (pinned to zero about the named axis)
together with whatever twist angle is left over.

Parameters :

axis ( Literal [ 'X' , 'Y' , 'Z' ] ) – Twist axis as a string.

Returns :

Swing, twist angle.

Return type :

tuple[Quaternion, float]

[Related references](INDEX.md).
