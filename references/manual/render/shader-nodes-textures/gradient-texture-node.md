# Gradient Texture Node

### Gradient Texture Node

This node produces interpolated colour and intensity values driven by the input vector.

### Inputs

Vector
Where the texture is sampled; with nothing plugged in it falls back to Generated coordinates.

### Properties

Gradient Type
Sets which kind of gradient is produced.

Linear :

Passes the input X coordinate straight out.

Quadratic :

Takes the input X coordinate and interpolates it quadratically.

Easing :

Blends quadratic and linear interpolation to ease the input X coordinate into a smooth gradient.

Diagonal :

Averages the input X and Y coordinates.

Spherical :

Builds an inverse gradient from the length of the input vector, peaking at (0, 0, 0).

Quadratic Sphere :

Like Spherical, but interpolated quadratically.

Radial :

Returns a value from the input's angle around the Z axis.

### Outputs

Color
Texture color output.

Factor
Texture intensity output.

### Examples

Gradient texture using object coordinates.

[Related references](INDEX.md).
