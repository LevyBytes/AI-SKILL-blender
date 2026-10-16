# Image Kernels

## Image Kernels

An image kernel is a small matrix of numbers that processes an image through a mathematical operation called convolution, where each kernel value sets how much a neighboring pixel contributes to the output pixel. Kernels are fundamental to image processing, used for blurring, sharpening, and edge detection by weighting and combining pixel neighborhoods to produce new detail. Concept: convolving an image with a kernel centers the kernel over each pixel, multiplies each neighborhood pixel by the matching kernel value, and sums the results into the output pixel's color, repeating for every pixel; the kernel values may be positive, negative, or fractional, and their pattern sets the effect. Common examples — Blur: a simple blur uses evenly weighted positive values, e.g. a 3x3 average blur kernel
```text
1/9 1/9 1/9
1/9 1/9 1/9
1/9 1/9 1/9
```
that softens the image by averaging neighbors. Sharpen: a sharpening kernel boosts edge contrast by emphasizing the center pixel against its neighbors:
```text
0 -1 0
-1 5 -1
0 -1 0
```
Edge Detection: edge kernels highlight brightness transitions by measuring differences between adjacent pixels, e.g. the Laplacian kernel
```text
0 -1 0
-1 4 -1
0 -1 0
```
or the Sobel kernel (horizontal edges):
```text
-1 -2 -1
0 0 0
1 2 1
```
Normalization: kernels are often normalized so all values sum to 1, preventing overall brightening or darkening — e.g. dividing each blur-kernel element by the total keeps brightness consistent after convolution. Creating a kernel in the Compositor: kernels can be built directly from Blender's nodes without an external image, useful for procedural or parameterized filters, blurs, and glare patterns editable interactively — start with a constant image (an Image Node at a small resolution like 9x9 or 15x15, or a solid color from an RGB node); shape the kernel by editing pixel values (use Ellipse Mask or Blur nodes for soft circular falloffs, combine masks with Mix nodes for complex or directional shapes like a star or streak, and scale strength with a Math node in Multiply mode or normalize by dividing by the total); then feed the procedural image into the Convolve Node's Kernel input, where its pattern and brightness control the effect. Tips: small images (under 20x20) make efficient, responsive kernels; use Normalize Kernel in the Convolve node to keep brightness balanced; animated masks or procedural noise make dynamic or flickering effects; and kernels with positive and negative values emphasize edges or textures.

[Related references](INDEX.md).
