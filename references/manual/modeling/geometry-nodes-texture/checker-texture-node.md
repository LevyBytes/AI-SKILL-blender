# Checker Texture Node

## Checker Texture Node

The Checker Texture node adds a checkerboard texture. Inputs: Vector (the texture coordinate to sample at, defaulting to Generated coordinates if unconnected — and note this node can have precision issues with some vector inputs, with mitigations on the White Noise Texture page); Color1, Color 2 (the checker colors); and Scale (overall texture scale — the bounding box of the face divided by the scale, so a scale of 15 gives 15 alternating patterns over the UV bounding box, and other nodes like the Math Node can drive different patterns into this socket). This node has no properties. Outputs: Color (the texture color) and Factor (the Checker 1 mask, 1 = Checker 1).

Checker Texture Node

Note: Ported from shader nodes; manual references shader version. Accepts field inputs/outputs. Vector defaults to implicit position.

Tip: Texture nodes exceed geometry resolution, causing Moiré or aliasing.

Produces checkerboard texture.

Inputs
Vector: Sample coordinate; defaults to Generated coordinates if unconnected. Warning: Precision issues with some inputs (see White Noise Texture notes).
Color1, Color 2: Checker colors.
Scale: Overall scale. A factor of the bounding box divided by scale. Example: scale 15 = 15 patterns across the UV box. Vary patterns via Math node or other inputs.

Outputs
Color: Texture color output.
Factor: Checker 1 mask (1 = Checker 1).

Examples: Default Checker texture.

[Related references](INDEX.md).
