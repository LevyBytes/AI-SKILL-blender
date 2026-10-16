# Hue/Saturation/Value Node

## Hue/Saturation/Value Node

The Hue/Saturation/Value node transforms an image's colors within the HSV color model. Inputs: Image/Color (standard color input); Hue (the hue rotation offset, 0 being -180° and 1 being +180°, where 0 and 1 give the same result); Saturation (0 removes color for black-and-white, above 1.0 increases saturation); Value (the value shift — 0 makes the color black, 1 keeps it, higher makes it brighter); and Factor (how much the node influences the image). Output: Image/Color (standard color output). Hue/Saturation tips: hues lie on a circle, so a Hue offset of 1 (+180°) on a blue image gives the opposite color, yellow, and applying it again returns blue; grayscale images have no hue, so changing their Hue or Saturation does nothing (you can only brighten or darken via Value, and adding color needs the Mix node); and the values can be animated over time with a Time Curve node or keyframes.

The Hue/Saturation/Value Node applies a color transformation within the HSV Color Model.

Inputs:
Image/Color — the usual color input.
Hue — the hue rotation offset, from 0 (-180°) to 1 (+180°); note 0 and 1 give the same result.
Saturation — 0 drains all color, leaving black-and-white, while above 1.0 boosts saturation.
Value — the value shift: 0 makes the color black, 1 leaves it unchanged, and higher values brighten it.
Factor — how much sway the node has over the image.

Outputs:
Image/Color — the usual color output.

Hue/Saturation Tips — a few things that may help you use this node:
Hues sit on a circle — apply a Hue offset of 1 (+180°) to a blue image and you land on the opposite color, yellow; apply 1 again and you're back to blue.
Grayscale images have no hue — changing Hue or Saturation on a grayscale image does nothing; you can only brighten or darken it via Value. To add color, reach for the Mix node.
Animating the effect — the various values can be animated with a Time Curve node or by keyframing.

HSV Example — a basic example, plus an example of the Factor input used for masking.

### Hue/Saturation/Value Node 

The Hue/Saturation/Value Node implements HSV Color Model transformations.

### Inputs 

Image/Color
Standard color input.

Hue
The hue rotation offset, from 0 (-180°) to 1 (+180°). Note that 0 and 1 produce identical results.

Saturation
A value of 0 produces grayscale, eliminating color. Greater than 1.0 intensifies color saturation.

Value
The brightness offset. Zero makes the color black, 1 preserves it unchanged, and higher values increase brightness.

Factor
The degree to which this node influences the image.

### Outputs 

Image/Color
Standard color output.

### Hue/Saturation Tips 

Consider these guidelines for improved node application:

Hues are laid out on a circle
A Hue offset of 1 (+180°) applied to blue produces the opposite color—yellow. Reapplying it returns blue.

Grayscale images have no hue
Hue or Saturation adjustments have no effect on grayscale. Adjustment is limited to brightness manipulation via Value. For color introduction, employ the Mix node.

Changing the effect over time
Animate adjustments through a Time Curve node or frame-by-frame keyframing.

### HSV Example 

A basic example. 

An example of using the Factor input for masking.

[Related references](INDEX.md).
