# Image Coordinates Node

## Image Coordinates Node

The Image Coordinates node outputs coordinate fields for an input image, giving each pixel's location in different coordinate spaces — useful for procedural texturing, compositing effects, or image-based masking — computed per pixel from the image resolution and placement in the compositor's virtual space. Input: Image (used to determine dimensions and placement). Outputs: Uniform (normalized coordinates centered at zero, scaled by the image's largest dimension, for aspect-ratio-independent procedural effects, like Object coordinates in shader nodes), Normalized (normalized 0-to-1 coordinates across the image, with half-pixel offsets to align to pixel centers), and Pixel (pixel-space coordinates for each pixel's center, integer-based with a half-pixel offset).

[Related references](INDEX.md).
