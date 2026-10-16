# Checker Texture Node

### Checker Texture Node

A texture that lays down a checkerboard.

### Inputs

Vector
Where the texture is sampled; with nothing plugged in it falls back to Generated coordinates.

Warning

Some vector inputs can give this node precision trouble. The notes on the White Noise Texture cover ways to work around it.

Color1, Color 2
Colour of the two checker squares.

Scale
Overall texture scale. It works as the face's bounding box divided by the scale, so a value of 15 lays 15 alternating squares across the whole UV bounding box. Feeding other nodes into this socket — the Math Node, for one — produces different patterns.

### Properties

This node has no properties.

### Outputs

Color
Texture color output.

Factor
Checker 1 mask (1 = Checker 1).

### Examples

Default Checker texture.

[Related references](INDEX.md).
