# Align Rotation to Vector Node

## Align Rotation to Vector Node

Rotates an Euler orientation toward a specified direction, blended by a factor.

**Inputs**

Rotation
The Euler rotation to realign. (Must be a rotation input, not a direction vector like normal.)

Factor
How much to rotate toward the vector. Zero disables the node; one aligns perfectly.

Vector
Target direction in object-local space. Zero-vector points mean no rotation.

**Properties**

Axis
Which local axis rotates toward the vector.

Pivot

Auto: Finds the optimal rotation angle, minimizing rotation magnitude.

X, Y, Z: Rotates around a specific local axis.

**Outputs**

Rotation
The rotated Euler value.

[Related references](INDEX.md).
