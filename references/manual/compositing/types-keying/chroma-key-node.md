# Chroma Key Node

## Chroma Key Node

The Chroma Key node decides whether a pixel is foreground or background (and so transparent) from its chroma values — use it, for example, to composite footage shot before a green or blue screen. Inputs: Image (standard color input); Key Color (the background color, usually picked with the color picker from the original image); Minimum (an angle on the color wheel for how tolerant the keying color is — larger angles allow more variation to count as background); Maximum (the level considered pure background — higher cutoffs make more pixels fully transparent if within the angle tolerance); and Falloff (raise it to make nearby pixels partly transparent for a smoother edge blend). Outputs: Image (alpha adjusted for the keyed selection) and Matte (a black-and-white alpha mask of the key).

[Related references](INDEX.md).
