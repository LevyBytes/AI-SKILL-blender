# Mix node

The Mix node interpolates A and B using Factor. Choose Float, Vector, Color, or Rotation as the data type. Color mode also exposes blend modes.

## Inputs and output

- Factor controls the interpolation between A and B.
- A and B supply the values being blended.
- Result uses the selected data type.

## Properties

- Data Type selects Float, Vector, Color, or Rotation.
- Factor Mode applies to vectors: Uniform uses one scalar factor; Non-Uniform uses separate factors for X, Y, and Z.
- Mix applies to colors and selects the blend operation.
- Clamp Factor restricts Factor to [0, 1]. Disable it to extrapolate beyond that range.
- Clamp Result applies to colors and restricts Result to [0, 1].

The color blend modes are Add, Subtract, Multiply, Screen, Divide, Difference,
Darken, Lighten, Overlay, Color Dodge, Color Burn, Hue, Saturation, Value, Color,
Soft Light, and Linear Light. Consult Color Blend Modes for their individual behavior.

## Examples

The same controls underlie the value, color, vector, and rotation configurations.
Color examples include blending a colored pattern with a constant color or a circular mask.

For an overexposed compositing result, one RGB Curves node can reduce brightness with a linear scale,
while another increases contrast with a nonlinear curve: dark values become darker and bright values brighter.
Mix their results to combine the adjustments. The Mix Color reference provides further examples.

[Related references](INDEX.md).
