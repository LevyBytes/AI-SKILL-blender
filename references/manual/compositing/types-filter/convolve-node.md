# Convolve Node

## Convolve Node

The Convolve node performs a 2D convolution on an image using a custom Image Kernel, enabling effects like blurring, sharpening, and edge detection depending on the kernel values — it multiplies a neighborhood of pixels around each pixel by the kernel values and sums them for the output color, a common image-processing way to emphasize or suppress spatial features. Inputs: Image (the image to process); Kernel (the convolution kernel, given as a constant value or an input image whose pixel values define the weights); and Normalize Kernel (a factor deciding whether to auto-normalize the kernel — divide by its total sum — to keep brightness consistent). Properties: Kernel Data Type — Float (a numeric kernel from the Kernel input socket) or Image (a full image as the kernel for more complex patterns). Output: Image (the convolved result). Usage covers blurring (an evenly weighted positive kernel), sharpening (a high central value with negative surroundings), and edge detection (Sobel or Laplacian kernels) — and when designing custom kernels, balance the size and values to avoid over-brightening or darkening, with Normalize Kernel often recommended.

[Related references](INDEX.md).
