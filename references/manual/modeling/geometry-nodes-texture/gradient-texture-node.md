# Gradient Texture Node

## Gradient Texture Node

The Gradient Texture node makes interpolated color and intensity values from the input vector. Input: Vector (the coordinate to sample at, defaulting to Generated coordinates if unconnected). Properties: Gradient Type — Linear (output the input X coordinate directly), Quadratic (interpolate X quadratically), Easing (a mix of quadratic and linear for a smooth gradient from X), Diagonal (average X and Y), Spherical (an inverse gradient from the input vector's length, peaking at (0, 0, 0)), Quadratic Sphere (Spherical but interpolated quadratically), and Radial (a value from the input's angle around the Z axis). Outputs: Color (the texture color) and Factor (the texture intensity).

Gradient Texture Node

Note: Ported from shader nodes; manual references shader version. Accepts field inputs/outputs. Vector defaults to implicit position.

Generates interpolated color and intensity from the input vector.

Inputs
Vector: Sample coordinate; defaults to Generated if unconnected.

Properties
Type: Gradient type.
  Linear: Outputs input X directly.
  Quadratic: Interpolates X quadratically.
  Easing: Mixes quadratic and linear for smooth gradient.
  Diagonal: Averages X and Y.
  Spherical: Inverse gradient by vector length; max at (0,0,0).
  Quadratic Sphere: Spherical with quadratic interpolation.
  Radial: Value based on angle around Z axis.

Outputs
Color: Texture color output.
Factor: Texture intensity output.

Examples: Gradient texture using object coordinates.

[Related references](INDEX.md).
