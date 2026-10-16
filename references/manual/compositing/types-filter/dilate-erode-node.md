# Dilate/Erode Node

## Dilate/Erode Node

The Dilate/Erode node grows or shrinks a mask with a morphological operator. Inputs: Mask (a grayscale image); Size (the surrounding area examined per pixel — i.e. how much to dilate, for positive values, or erode, for negative); and Type — Steps (set each pixel to the maximum, for dilation, or minimum, for erosion, found in a surrounding square, keeping the original gray levels and best for masks with sharp corners, while rounded shapes look more square — and despite the name it runs once regardless of Size), Threshold (force pixels fully black or white by whether they're darker or brighter than 50% gray, then take the max/min within a surrounding circle, losing gray levels and suiting rounded corners while rounding off sharp ones), Distance (take the max/min within a surrounding circle while preserving gray levels, suiting rounded corners), or Feather (blur the image); plus Falloff Size (Threshold — how much to blur the edges after dilation/erosion) and Falloff (Feather — the brightness curve of the blurred edges). Output: Mask (the resulting mask).

[Related references](INDEX.md).
