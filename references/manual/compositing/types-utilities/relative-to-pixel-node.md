# Relative To Pixel Node

## Relative To Pixel Node

The Relative To Pixel node converts values relative to the image size into pixel units — useful for screen-space operations needing absolute pixels, like blurring or positioning effects. Inputs: Value (a float or vector relative to the image size, to convert to pixels) and Image (used to determine the resolution, defining the reference size). Properties: Data Type (Float or Vector) and Reference Dimension — Per Dimension (scale X and Y independently by image width and height), X (scale by width), Y (scale by height), Greater (scale by the larger dimension), Smaller (scale by the smaller), or Diagonal (scale by the image's diagonal length). Output: Value (the input converted from relative to absolute pixels, matching the chosen Data Type).

[Related references](INDEX.md).
