# Stabilize 2D Node

## Stabilize 2D Node

The Stabilize 2D node stabilizes footage per the settings in Movie Clip Editor ‣ Properties ‣ Stabilization ‣ 2D Stabilization (see 2D Stabilization). Inputs: Image (standard color input) and Invert (reverse the stabilization — if the calculated move was up by 5 units, this moves down by 5). Sampling — Filter, how pixel values are interpolated when scaling or transforming: Nearest (the closest pixel's value with no smoothing, the fastest, suiting pixel art or low-res images wanting sharp blocky edges, though animated motion steps one pixel at a time and can jitter), Bilinear (an average of neighboring pixels, smoother than Nearest and a good speed/quality balance), Bicubic (a weighted average over a larger neighborhood for even smoother results, ideal for photos or gradients needing fine detail), and Anisotropic (interpolation adapted to the transform's direction and scale, cutting blur or aliasing when scaling at steep angles or uneven resolutions, useful for textures at oblique angles or detailed 3D projections). Properties: Movie Clip (the clip whose stabilization to use). Output: Image (standard color output).

[Related references](INDEX.md).
