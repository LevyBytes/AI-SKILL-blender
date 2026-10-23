# Separate Color Node

## Separate Color Node

The Separate Color node splits an image into its composite color channels, outputting multiple color models per the Mode property. Input: Image (standard image input). Properties: Mode, the color model to output — RGB (three outputs: Red, Green, Blue), HSV (Hue, Saturation, Value), HSL (Hue, Saturation, Lightness), YCbCrA (Luminance, Chrominance Blue, Chrominance Red), with a Color Space option (ITU 601, ITU 709, JPEG), or YUV (Luminance, U chrominance, V chrominance). Outputs: depend on Mode (above), plus Alpha (the transparency channel). Examples — Blur Alpha: take the Alpha channel, blur it, and recombine it so edges blend into a scene rather than ending hard (almost like 3D anti-aliasing), useful when adding CG to live action, and animating it broadly makes the object appear to "phase" in and out. Increase Luminance: a Math (Multiply) node raises the luminance channel (Y) to brighten the image — and when adjusting these channels through a Color Ramp, the Cardinal scale is accurate while the Exponential scale on luminance gives high contrast.

Splits an image into its channels according to a chosen Color Model.

Inputs:
Color: the usual color input.

Properties:
Mode: the color model to output. RGB (Red, Green, Blue), HSV (Hue, Saturation, Value), or HSL (Hue, Saturation, Lightness).

Outputs: these depend on the Mode property (above).
Alpha: the opacity value.

The Separate Color node splits a color into its channels per a given color model.

Color: Standard input.

Mode: Color space to output.

RGB: Red, Green, Blue.
HSV: Hue, Saturation, Value.
HSL: Hue, Saturation, Lightness.

The outputs depend on Mode (above).
Alpha: Opacity value.

### Separate Color Node 

Decomposes image channels according to a specified Color Model.

### Inputs 

Color
Standard color input.

### Properties 

Mode
The color space for channel output.

RGB :

Red, Green, Blue.

HSV :

Hue, Saturation, Value.

HSL :

Hue, Saturation, Lightness.

### Outputs 

Channel outputs depend on the Mode property (see above).

Alpha
The opacity value.

[Related references](INDEX.md).
