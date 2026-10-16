# Color Correction Node

## Color Correction Node

The Color Correction node adjusts an image's color separately across tonal ranges (highlights, midtones, shadows). Inputs: Image (standard color input) and Mask (how much the node influences the output). Master (targeting the whole tonal range): Saturation (adjust saturation), Contrast (adjust contrast), Gamma (exponential gamma correction affecting midtones, like Power in Color Balance), Gain (a multiplier with stronger effect on highlights, like Slope in Color Balance), and Offset (a value, possibly negative, added linearly to lighten or darken). Highlights / Midtones / Shadows: each range supports the same controls as Master. Tonal Ranges: Midtones Start, Midtones End define where the range splits into highlights, midtones, and shadows (with a smooth 0.2-unit transition between ranges). Channels: Red, Green, Blue choose which RGB channels the correction affects. Output: Color (standard color output).

[Related references](INDEX.md).
