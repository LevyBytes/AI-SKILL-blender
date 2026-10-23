# Translate Node

## Translate Node

The Translate node moves an image — also usable to add a 2D camera shake. Inputs: Image (standard color input) and X, Y (move it horizontally and vertically). Sampling — Interpolation, how pixel values are sampled when scaling or transforming: Nearest (the closest pixel's value with no smoothing, the fastest, suiting pixel art or low-res images wanting sharp blocky edges, with single-pixel jitter in animation), Bilinear (an average of neighboring pixels, smoother and a good balance), Bicubic (a weighted average over a larger neighborhood, ideal for photos or gradients), and Anisotropic (adapted to the transform's direction and scale, cutting blur or aliasing at steep angles or uneven resolutions). Extension X/Y per axis — Clip (transparent outside), Extend (closest boundary pixel), or Repeat (image repetitions). Output: Image (standard color output).

Offsets an image's or texture's texture coordinates.

Inputs:
Color: the usual color input.
Offset: how much to offset the coordinates along each of the three axes.

Properties: this node exposes no properties.

Outputs:
Color: the usual color output.

[Related references](INDEX.md).
