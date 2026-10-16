# Transform Node

## Transform Node

The Transform node combines the Scale, Translate, and Rotate nodes. Inputs: Image (standard color input); X, Y (move the image horizontally and vertically); Angle (rotate around the center — positive counterclockwise, negative clockwise); and Scale (resize relatively, so 0.5 is half size and 2.0 is double). Sampling — Filter, how pixel values are sampled when scaling or transforming: Nearest (the closest pixel's value with no smoothing, the fastest, suiting pixel art or low-res images wanting sharp blocky edges, with single-pixel jitter in animation), Bilinear (an average of neighboring pixels, smoother and a good balance), Bicubic (a weighted average over a larger neighborhood, ideal for photos or gradients), and Anisotropic (adapted to the transform's direction and scale, cutting blur or aliasing at steep angles or uneven resolutions). Extension X/Y per axis — Clip (transparent outside), Extend (closest boundary pixel), or Repeat (image repetitions). Output: Image (standard color output).

[Related references](INDEX.md).
