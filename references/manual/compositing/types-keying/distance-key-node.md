# Distance Key Node

## Distance Key Node

The Distance Key node sets a pixel's alpha from the 3D distance between its color and the key color in a 3D color space — working well for isolating a specific background color (not only green). Inputs: Image (standard color input); Key Color (the color to key); Color Space (RGB or YCC — and with YCbCr only the Cb and Cr channels count toward the foreground/background distance); Tolerance (the threshold for what counts as a match — how close a pixel must be to the background to be an absolute match); and Falloff (high values make pixels close to the Key Color more transparent than those farther but still keyed, while low values make any keyed pixel transparent regardless of closeness). Outputs: Image (alpha adjusted for the keyed selection) and Matte (a black-and-white alpha mask of the key).

[Related references](INDEX.md).
