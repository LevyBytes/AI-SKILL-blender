# Scale Node

## Scale Node

The Scale node resizes an image. Inputs: Image (standard color input) and Space, the coordinate space to scale relative to — Relative (percentages of the input's dimensions), Absolute (absolute pixel sizes), Scene Size (size to the scene's final render resolution — e.g. rendering 1080p at 50% render percentage gives a 1080p image with the scene scaled down 50% and the rest alpha), or Render Size (the dimensions set in the Render panel). Frame Type (Render Size — how the image fits the camera frame): Stretch (distort to fit the render size), Fit (scale until the larger axis fits), or Crop (cut to the render size's aspect ratio). X, Y (axis scale, only with Space Relative or Absolute). Sampling — Interpolation, how pixel values are sampled when scaling or transforming: Nearest (the closest pixel's value with no smoothing, the fastest, suiting pixel art or low-res images wanting sharp blocky edges, with single-pixel jitter in animation), Bilinear (an average of neighboring pixels, smoother and a good balance), Bicubic (a weighted average over a larger neighborhood for even smoother results, ideal for photos or gradients), and Anisotropic (adapted to the transform's direction and scale, cutting blur or aliasing at steep angles or uneven resolutions). Extension X/Y per axis — Clip (transparent outside), Extend (closest boundary pixel), or Repeat (image repetitions). Output: Image (standard color output). Examples: X 0.5, Y 0.5 halves the width and height — and since most nodes output an image the size of their top image input, use this node to scale a second image up to match a first before uniformly combining them.

Scales an image's or texture's texture coordinates.

Inputs:
Color: the usual color input.
Scale: how much to scale the coordinates along each of the three axes.

Properties: this node exposes no properties.

Outputs:
Color: the usual color output.

[Related references](INDEX.md).
