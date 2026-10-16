# Brick Texture Node

## Brick Texture Node

The Brick Texture node adds a procedural texture of bricks. Inputs: Color 1/2 (the brick colors); Mortar (the color between bricks); Scale (overall texture scale); Mortar Size (the size of the filling, the "mortar," between bricks — 0 means none); Mortar Smooth (blur/soften the edge between mortar and bricks, useful with textures and displacement); Bias (the color variation between Color 1/2 — -1 and 1 use only one of the two colors, values between mix them); Brick Width (the brick width relative to the texture scale); and Row Height (the brick row height relative to the texture scale). Properties: Offset (the brick offset of the rows); Frequency (how often rows are offset — 2 gives an even/uneven row pattern); Squash (a factor adjusting brick width for particular rows set by Frequency); and Frequency (how often rows hold squished bricks). Outputs: Color (the texture color) and Factor (the mortar mask, 1 = mortar).

Brick Texture Node

Note: Ported from shader nodes; manual and images reference the shader version. Accepts field inputs/outputs. Vector input defaults to implicit position.

Tip: Texture nodes create details finer than geometry resolution. May cause Moiré patterns or aliasing.

Produces procedural brick texture.

Inputs
Color 1/2: Brick color.
Mortar: Color between bricks.
Scale: Overall texture scale.
Mortar Size: Grout width; 0 = no mortar.
Mortar Smooth: Softens the mortar/brick edge. Useful with displacement.
Bias: Color mix between Color 1/2. −1 and 1 use single colors; in-between values mix.
Brick Width: Brick width.
Row Height: Height of brick rows.

Properties
Offset: Determines the brick offset of the various rows.
Frequency: Determines the offset frequency. A value of 2 gives an even/uneven pattern of rows.
Squash: Amount of brick squashing.
Frequency: Brick squashing frequency.

Outputs
Color: Texture color output.
Factor: Mortar mask (1 = mortar).

Examples: Brick texture with colors changed, Squash 0.62, Squash Frequency 3.

[Related references](INDEX.md).
