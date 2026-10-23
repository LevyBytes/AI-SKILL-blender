# Vector Rotate Node

## Vector Rotate Node

The Vector Rotate node rotates a vector around a pivot point (Center). Inputs: Vector (the vector to rotate), Center (the point to rotate around), Axis (the axis to rotate around), Angle (the rotation amount), and Rotation (when Type is Euler, rotate by these angles around X, then Y, then Z). Properties: Type — X/Y/Z Axis (rotate around that axis by the Angle), Axis Angle (rotate around an arbitrary axis from the Axis input by the Angle), or Euler (rotate about the Center point by the per-axis Rotation vector) — plus Invert (invert the rotation angle). Output: Vector (the rotated vector).

Applies rotational transformation to a vector around a pivot (Center) using the chosen rotation method.

Inputs:
- Vector: The vector undergoing rotation
- Center: Pivot location for rotation
- Axis: Rotation axis direction
- Angle: Magnitude of rotation
- Rotation: When Type is Euler, rotation angles around X then Y then Z axes

Properties:
Type - Rotation method:

X/Y/Z Axis: Rotate around the defined axis by the amount specified in Angle

Axis Angle: Rotate around an arbitrary axis (from Axis input) by the amount in Angle

Euler: Rotate about center point (from Center input) by angles in Rotation input vector (applied in X, Y, Z order)

Invert: Inverts the rotation angle

Outputs:
- Vector: The rotated vector

### Vector Rotate Node

This node allows rotation of a vector about a pivot location (Center).

### Inputs

Vector
Vector to be rotated.

Center
Point to pivot around.

Axis
Rotation axis.

Angle
Rotation magnitude.

Rotation
When Type is set to Euler, rotate the input vector by these angles around the X, Y, then Z axes in that order.

### Properties

Type
The angle input type.

X/Y/Z Axis :

Rotates the vector around the defined axis by the amount specified in Angle.

Axis Angle :

Rotates the vector around an arbitrary axis specified by the Axis input. The rotation magnitude is defined by Angle.

Euler :

Rotates the vector about a center point specified by the Center input. Each axis rotation is defined by the Rotation input vector.

Invert
Inverts the rotation magnitude.

### Outputs

Vector
The rotated vector.

### Examples

Vector Rotate node example.

[Related references](INDEX.md).
