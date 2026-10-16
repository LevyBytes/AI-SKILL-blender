# Combine Color Node

## Combine Color Node

The Combine Color node builds an image from its composite color channels, supporting multiple color models per the Mode property. Inputs: depend on Mode (see below), plus Alpha (the channel handling transparency). Properties: Mode, the color model to output — RGB (combine Red, Green, Blue), HSV (Hue, Saturation, Value), HSL (Hue, Saturation, Lightness), YCbCr (Luminance, Chrominance Blue, Chrominance Red), with a Color Space option (ITU 601, ITU 709, JPEG), or YUV (Luminance, U chrominance, V chrominance). Output: Image (standard image output). Examples — Blur Alpha: take the Alpha channel, blur it, and recombine it with the colors so the edges blend into a scene instead of having a hard edge (almost like anti-aliasing but in 3D), useful when adding CG to live action to remove hard edges, and animating it broadly makes the object appear to "phase" in and out. Increase Luminance: a Math (Multiply) node raises the luminance channel (Y) to brighten the image — and a tip notes that when adjusting these channels through a Color Ramp, the Cardinal scale gives accurate representation while the Exponential scale on luminance gives a high-contrast effect.

Merges four grayscale channels into one color image according to a chosen Color Model.

Inputs — these depend on the Mode property (below).
Alpha — the output color's opacity.

Properties:
Mode — the color model to use. RGB (Red, Green, Blue), HSV (Hue, Saturation, Value), or HSL (Hue, Saturation, Lightness).

Output:
Color — the usual color output.

The Combine Color node merges four grayscale inputs into a single color based on the chosen color model.

The inputs depend on the Mode (below).

Alpha: Opacity of the output.

Mode: Color space used.

RGB: Red, Green, Blue.
HSV: Hue, Saturation, Value.
HSL: Hue, Saturation, Lightness.

Color: Standard output.

[Related references](INDEX.md).
