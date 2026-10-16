# Brush Settings: Color Picker, Randomize Color

### Color Picker

Color

Brushes have two colors that can be set using the Color Picker:

- Primary Color : The active color used for painting by default.

- Secondary Color : An alternate color that can be quickly accessed.

By default, painting uses the primary color. The secondary color can be used temporarily by holding Ctrl while painting. The two colors can also be swapped at any time using Swap Colors.

Tip

- Press Shift - X to sample a color at the mouse cursor position.

- Press Shift - Ctrl - X to sample the merged viewport color , including lighting, shading, and all visible layers.

The sampled color becomes the primary color of the active Paint brush.

(Swap Colors) X
Swaps the primary and secondary colors.

(Use Unified Color)
Use the same brush color across all brushes.

Note

Note that Vertex Paint works in sRGB space, and the RGB representation of the same colors will be different between the paint tools and the materials that are in linear space.

Gradient

A gradient can be used as a color source.

Gradient Colors
The Color Ramp Widget to define the gradient colors.

Mode

Pressure :

Will choose a color from the color ramp according to the stylus pressure.

Clamp :

Will alter the color along the stroke and as specified by Gradient Spacing option. With Clamp it uses the last color of the color ramp after the specified gradient.

Repeat :

Similar to Clamp . After the last color it resets the color to the first color in the color ramp and repeats the pattern.

### Randomize Color

Applies random variation to the brush color for more natural and varied strokes. Useful for hand-painting textures or adding subtle irregularities.

The randomness can affect hue, saturation, and value independently. Each channel also supports pressure sensitivity and stroke-based randomness.

Hue
Amount of random variation applied to the hue of the brush color.

(Stroke Random)
Apply a single random hue per stroke instead of varying continuously during the stroke.

(Use Pressure)
Modulate hue variation based on pen pressure.

Saturation
Amount of random variation applied to the saturation of the brush color.

(Stroke Random)
Apply a single random saturation per stroke instead of varying continuously during the stroke.

(Use Pressure)
Modulate saturation variation based on pen pressure.

Value
Amount of random variation applied to the value (brightness) of the brush color.

(Stroke Random)
Apply a single random value per stroke instead of varying continuously during the stroke.

(Use Pressure)
Modulate value variation based on pen pressure.

[Related references](INDEX.md).
