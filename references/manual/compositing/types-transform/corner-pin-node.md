# Corner Pin Node

## Corner Pin Node

The Corner Pin node warps a plane using explicit corner values — like the Plane Track Deform node but without "plane track" data from the Movie Clip Editor. The input Image's transformation is applied before distortion, so translations introduce clipping. Inputs: Image (standard color input); Corners (four vector inputs defining the plane warp). Sampling — Interpolation, how pixel values are interpolated when scaling or transforming: Nearest (the closest pixel's value with no smoothing, the fastest, suiting pixel art or low-res images wanting sharp blocky edges, though animated motion steps one pixel at a time and can jitter), Bilinear (an average of neighboring pixels, smoother than Nearest and a good speed/quality balance), Bicubic (a weighted average over a larger neighborhood for even smoother results, ideal for photos or gradients needing fine detail), and Anisotropic (interpolation adapted to the transform's direction and scale, cutting blur or aliasing when scaling at steep angles or uneven resolutions, useful for textures at oblique angles or detailed 3D projections). Outputs: Image (the distorted image) and Plane (a black-and-white alpha mask of the plane).

[Related references](INDEX.md).
