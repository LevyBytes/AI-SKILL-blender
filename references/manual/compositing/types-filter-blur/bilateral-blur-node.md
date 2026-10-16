# Bilateral Blur Node

## Bilateral Blur Node

The Bilateral Blur node does a high-quality adaptive blur, softening the image while keeping sharp edges — useful for smoothing noisy render passes to save computation (e.g. ray-traced ambient occlusion, blurry refractions/reflections, soft shadows) or for non-photorealistic effects. Inputs: Image (standard color input — with only this connected, it blurs based on the edges in the source); Determinator (if connected, the source defining edges/borders for the blur, a big advantage when the source image is too noisy but normals plus the Z-buffer can still define exact object borders); Size (the blur size in pixels); and Threshold (pixels enter the blur area when the average difference between their determinator and the center pixel's is below this). Output: Image (standard color output).

[Related references](INDEX.md).
