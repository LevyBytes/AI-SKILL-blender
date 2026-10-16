# Vignette Node

## Vignette Node

The Vignette node darkens or fades an image's edges to draw attention to the center, often used artistically or cinematically for focus, mood, or depth. Inputs: Image (standard color input); Factor (the overall strength — 0 disables it, higher values darken the vignette more); and Feather (the softness of the transition from center to edges, higher values giving a smoother fade). Transform: Corner Roundness (the corner shape — 0 gives square corners, 1 a fully circular vignette); Scale (the vignette area's size, smaller values tightening it near the center); Offset (shift the center along X and Y to emphasize a specific area); and Angle (rotate the mask around the image center). Outputs: Image (the result with the vignette) and Mask (the generated vignette mask as grayscale, usable for custom compositing or selective application via mix nodes).

[Related references](INDEX.md).
