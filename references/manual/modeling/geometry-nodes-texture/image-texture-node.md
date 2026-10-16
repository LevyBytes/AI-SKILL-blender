# Image Texture Node

## Image Texture Node

Image Texture Node

Note: Operates differently in geometry nodes vs shader nodes. Vector defaults to implicit position.

Uses an image file as texture. Samples with Vector input, outputs Color and Alpha.

Inputs
Image: Connect to Group Input node or open/select from the node directly.
Vector: Look-up coordinate. Uses Position attribute if unconnected.
Frame: For animated images, set the frame here (keyframeable).

Properties
Interpolation: Scaling method.
  Linear: Regular quality.
  Cubic: Smoother, better for bump maps.
  Closest: No interpolation; use for pixel art.
Extension: Behavior past image bounds.
  Repeat: Tile horizontally and vertically.
  Extend: Repeat edge pixels.
  Clip: Clip to bounds, exterior = transparent black.
  Mirror: Flip horizontally and vertically repeatedly.

Outputs
Color: RGBA color from the image.
Alpha: Alpha channel from image.

Examples: Image Texture displacing a plane.

[Related references](INDEX.md).
