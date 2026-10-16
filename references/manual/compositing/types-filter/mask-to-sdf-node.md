# Mask To SDF Node

## Mask To SDF Node

The Mask To SDF node builds a signed distance field (SDF) from a mask, storing for each pixel the distance to the nearest mask boundary, with the sign showing whether the pixel is inside or outside the masked region — useful for soft edges, outlines, glows, erosion/dilation, or procedural distance-based compositing. Input: Mask (the mask generating the field, where inside pixels are interior and outside ones exterior). Outputs: SDF (the signed distance to the nearest boundary pixel in pixels, negative inside the mask and positive outside) and Nearest Pixel (the integer coordinates of the nearest boundary pixel, for advanced effects needing the closest edge position).

[Related references](INDEX.md).
