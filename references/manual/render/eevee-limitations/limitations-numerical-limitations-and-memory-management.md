# Limitations: Numerical Limitations, Memory Management, CPU Rendering, Multiple GPU Support, Headless Rendering

### Numerical Limitations

- EEVEE operates on half-precision (16-bit) floating point by default, except shader node tree evaluation uses single-precision (32-bit).
- Render output maintains half-precision (16-bit) resolution.
- Combined and Light data passes clamp negative values to zero.

### Memory Management

GPU memory is handled by the GPU driver. Theoretically, only resources needed for a single draw call must fit. Complex scenes cause the driver to manage memory by swapping. In practice, excessive GPU memory use risks driver crash, freeze, or application termination.

No standard exists to predict whether resources will fit or render successfully.

### CPU Rendering

As a rasterization renderer, EEVEE relies exclusively on GPU processing. CPU rendering is not planned, as it would be inefficient. CPU involvement remains necessary for scene preparation before each frame.

### Multiple GPU Support

No current support exists for multi-GPU systems.

### Headless Rendering

Headless rendering is not available on Windows headless systems.

[Related references](INDEX.md).
