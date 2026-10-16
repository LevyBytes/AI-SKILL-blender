# White Noise Texture Node

### White Noise Texture Node

**Note:** This node originates as a port from shader nodes; the manual references the shader version.
This node accepts field inputs and outputs.
The Vector input defaults to an implicit position attribute value when unconnected.

A random number generator based on an input Seed, the White Noise Texture node outputs a value between zero and one. The seed input type depends on the Dimensions setting: it can be a scalar, 2D vector, 3D vector, or 4D vector.
The output is a scalar random number in the [0, 1] range.

### Inputs

Dynamic inputs appear based on node properties.

**Vector**
Seed vector for 2D, 3D, and 4D modes.

**W**
Seed scalar for 1D and 4D modes.

### Properties

**Dimensions**
Space dimensionality for noise evaluation.

- **1D:** Uses the W input as seed.
- **2D:** Uses X and Y components of Vector as seed.
- **3D:** Uses Vector as seed.
- **4D:** Uses both Vector and W as seed.

### Outputs

**Value**
A scalar random output.

**Color**
A random color output.

### Notes

Minimal seed differences yield entirely different outputs.
Bad precision has serious implications.
Mitigation approaches:

- **Eliminate problematic seed components.** If a problematic seed is constant, reduce dimensions or multiply by zero.
- **Add an arbitrary offset.** Boundary-related issues often resolve with a constant offset.
- **Use absolute value.** Signed zero ambiguity unifies with absolute value.

| Precision loss from signed zeros on Z | Fix: remove Z axis |
| --- | --- |
| Fix: add constant offset | Fix: apply absolute value |

[Related references](INDEX.md).
