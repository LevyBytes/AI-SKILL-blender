# Brick Texture Node

### Brick Texture Node

A procedural texture that lays down a brick pattern.

### Inputs

Color 1/2
Colour of the bricks.

Mortar
Colour of the gaps between bricks.

Scale
Overall texture scale.

Mortar Size
How wide the filler between bricks — the "mortar" — runs; 0 removes it entirely.

Mortar Smooth
Softens and blurs the boundary where mortar meets brick, which can help alongside a texture and displacement textures.

Bias
Shifts the colour mix between Color 1/2 . At -1 and 1 only a single colour shows; values in between blend the two.

Brick Width
A brick's width as a fraction of the texture scale.

Row Height
A row's height as a fraction of the texture scale.

### Properties

Offset
Sets how far successive rows are shifted.

Frequency
How often rows get offset; a value of 2 alternates offset and non-offset rows.

Squash
Scales brick width on the rows picked out by the Frequency

Frequency
How often a row is made of "squished" bricks.

### Outputs

Color
Texture color output.

Factor
Mortar mask (1 = mortar).

### Examples

Brick texture: Colors changed, Squash 0.62, Squash Frequency 3.

[Related references](INDEX.md).
