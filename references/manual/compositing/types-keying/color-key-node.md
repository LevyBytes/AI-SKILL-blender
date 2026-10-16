# Color Key Node

## Color Key Node

The Color Key node does chroma keying — removing parts of an image by color — commonly to drop green- or blue-screen backgrounds, making a matte where the selected colors turn transparent. Inputs: Image (standard color input); Key Color (the target color to key out, typically the background, e.g. pure green or blue); Hue (the tolerance for hue difference from the key color — wider keys out more similar hues); Saturation (the tolerance for saturation difference, helping avoid removing unintended desaturated areas like skin or clothing); and Value (the tolerance for brightness difference, useful when lighting or background luminance is uneven). Outputs: Image (alpha adjusted for the keyed selection) and Matte (a black-and-white alpha mask of the key).

[Related references](INDEX.md).
