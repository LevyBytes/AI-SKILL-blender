# Mix Node

## Mix Node

The Mix node blends value, color, and vector inputs by a factor controlling the interpolation, with extra blend modes in Color mode. Inputs: Factor (how much A and B mix) and A/B (the two inputs). Properties: Data Type (float, vector, color, or rotation); Factor Mode (Vector only — Uniform, one float, or Non-Uniform, a per-XYZ vector); Mix (Color only — the blend mode from the menu, see Color Blend Modes), with Add, Subtract, Multiply, Screen, Divide, Difference, Darken, Lighten, Overlay, Color Dodge, Color Burn, Hue, Saturation, Value, Color, Soft Light, Linear Light; Clamp Factor (limit the factor to 0.0-1.0, otherwise Extrapolation); and Clamp Result (Color only — limit the Result to 0.0-1.0). Output: Result (the mix in the chosen type). See the Mix Color Node for more examples.

Blends two images together, much as an image editor blends two layers.

Inputs:
Factor: the foreground image's opacity.
A: the background image; it sets the output's dimensions.
B: the foreground image.
Bear in mind that, unlike image editors where the foreground layer sits on top, Blender's foreground slot is the bottom one.

Properties:
Blending Mode: the blend to apply.
  Mix: plain alpha blending, usually called Normal in image editors.
  Darken: per color component, keeps the smaller of the two blended values.
  Multiply: multiplies the colors component by component; blending with white (1.0) does nothing, while blending with black (0.0) always yields black.
  Color Burn: inverts the background color, divides by the foreground color, and inverts the result.
  Lighten: per color component, keeps the larger of the two blended values.
  Screen: inverts both colors, multiplies, then inverts again.
  Color Dodge: divides the background color by the inverted foreground color.
  Add: sums the two colors.
  Overlay: uses Multiply blending when the foreground color's lightness is below 0.5, Screen blending when above.
  Soft Light: like Overlay, but gentler.
  Linear Light: uses Linear Burn (background + foreground - 1) when the foreground color's lightness is below 0.5, Linear Dodge (background + foreground) when above.
  Difference: per component, subtracts the lower value from the higher.
  Exclusion: adds the two colors, then subtracts twice their product.
  Subtract: takes the foreground color away from the background.
  Divide: splits the background color by the foreground.
  Hue: takes the background's saturation and value and the foreground's hue.
  Saturation: takes the background's hue and value and the foreground's saturation.
  Color: takes the background's value and the foreground's hue and saturation.
  Value: takes the background's hue and saturation and the foreground's value.
Use Alpha: whether to use the foreground image's alpha channel while mixing; the background's alpha is always used.
Clamp: clamps the output to the [0.0, 1.0] range.

Outputs:
Image: the mix result.

Examples: below are blending-mode examples plus some practical uses, such as blending a colored pattern with a flat color and a circular mask.

Fixing overexposure: the setup below shows how to rescue an overexposed render by darkening it and lifting contrast. The top RGB Curves Node darkens the image by scaling every color value down linearly; the bottom curve node raises contrast by pushing small values lower and large values higher; the Mix node then blends the pair.

Watermark Images — long ago a pattern was stamped into the wet paper pulp as it dried, leaving a sign of who made the paper and where, barely visible except in just the right light — probably the first subliminal advertising. Nowadays people watermark images to claim them as personal intellectual property, for subliminal promotion of the author or host, or simply to follow an image's spread across the web. Blender gives you a full toolset both to encode your watermark and to tell whether an image carries it.
  Encoding your Watermark in an Image: first build your own watermark: a name, a word, or a shape or image that's hard to replicate. Neutral gray works best with the suggested method, but you're free to use other colors or patterns, from a single pixel to a whole gradient. In the example we encode it at a set spot in the image with the Translate node, which helps later since we only check one location for the mark; we then run the color image through the RGB to BW node to get grayscale numbers, which feed the Map Range node to cut the mark to a tenth of its original strength. The Add node (a Mix node set to Add) sums the matching pixels, making the marked ones ever so slightly brighter. Of course, if you want the mark noticed, scale it less or give it a contrasting color; there are plenty of other approaches using different mix settings and fancier rigs, so experiment.
  Decoding an Image for your Watermark: when you spot an image you think is yours, use the node tree below to compare it against your stock (non-watermarked) original; here the Mix node sits on Difference while the Map Value node boosts whatever differs, so the original mark clearly stands out.

[Related references](INDEX.md).
