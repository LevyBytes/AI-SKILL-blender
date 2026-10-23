# Separate Cylindrical Node

## Separate Cylindrical Node

The Separate Cylindrical node turns a Cartesian vector (X, Y, Z) into cylindrical coordinates (R, Φ, Z), outputting each component — the inverse of the Combine Cylindrical node — useful for analyzing geometry or making procedural effects that depend on radial distance, angular position, or height, like spiral deformations, cylindrical gradients, or radial masks. Input: Vector (the Cartesian vector to convert). Outputs: R (the radial distance from the origin in the X-Y plane), Phi (the angular position around the Z axis), and Z (the vertical component, the input's Z coordinate directly).

Converts a vector from Cartesian (X, Y, Z) to cylindrical (R, Φ, Z) coordinates.
Inverse of Combine Cylindrical.

Useful for analyzing geometry or building procedural effects based on
radial distance, angular position, or height: spirals, cylindrical gradients, radial masks, etc.

**Inputs**

Vector
The Cartesian vector to convert.

**Outputs**

R
Radial distance in the X-Y plane.

Phi
Angular position around the Z axis.

Z
Vertical component (same as input Z).

### Separate Cylindrical Node

This node converts a vector from Cartesian coordinates (X, Y, Z) to cylindrical form (R, Φ, Z), outputting each independently. It provides the inverse of the Combine Cylindrical node.

This node suits analyzing geometry or building procedural elements based on radial distance, angular position, or altitude—for instance, spiral distortions, cylindrical gradations, or radial masks.

### Inputs

Vector
The input vector to decompose from Cartesian to cylindrical form.

### Outputs

R
Radial distance from the origin in the X-Y plane.

Phi
Angular position around the Z axis.

Z
Vertical component, directly corresponding to the input Z.

[Related references](INDEX.md).
