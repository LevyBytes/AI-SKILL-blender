# Rotate Node

## Rotate Node

The Rotate node rotates the input image around its center by a given angle. Inputs: Image (standard color input) and Angle (the rotation amount — positive clockwise, negative counterclockwise). Sampling — Interpolation, how pixel values are sampled when scaling or transforming: Nearest (the closest pixel's value with no smoothing, the fastest, suiting pixel art or low-res images wanting sharp blocky edges, though animated motion steps one pixel at a time and can jitter), Bilinear (an average of neighboring pixels, smoother than Nearest and a good speed/quality balance), Bicubic (a weighted average over a larger neighborhood for even smoother results, ideal for photos or gradients needing fine detail), and Anisotropic (interpolation adapted to the transform's direction and scale, cutting blur or aliasing at steep angles or uneven resolutions). Extension X/Y, the mode per axis — Clip (outside the image becomes transparent), Extend (the closest boundary pixel), or Repeat (image repetitions). Output: Image (standard color output).

Rotates an image's or texture's texture coordinates.

Inputs:
Color: the usual color input.
Turns: how many full 360° turns to rotate the coordinates about the chosen axis.
Axis: the axis to rotate the mapping about.

Properties: this node exposes no properties.

Outputs:
Color: the usual color output.

[Related references](INDEX.md).
