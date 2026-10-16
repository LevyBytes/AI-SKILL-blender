# Performance: Memory, Viewport, Compositor, Denoise Nodes

### Memory

Shadow Pool
Larger pool size accommodates more shadows but may exceed GPU memory, reducing performance. Increasing may resolve the Shadow buffer full error.

See also
Shadow documentation.

Light Probes Volume Pool
Larger pool size permits more irradiance grids but may exceed GPU memory, reducing performance.

### Viewport

Pixel Size
Control viewport rendering resolution. Speeds up viewport rendering, particularly useful for high-DPI displays.

### Compositor

Device
Select the compositing device.

CPU:
Composite on the CPU.

GPU:
Composite on the GPU.

Precision GPU
Set compositor intermediate precision.

Auto:
Full precision for final renders; half precision otherwise.

Full:
Full precision for final renders and viewport.

### Denoise Nodes

Denoising Device
Select the device for Denoise node processing in the compositor.

Auto:
Use the compositor's device.

CPU:
Process denoise on the CPU.

GPU:
Process denoise on the GPU if available, otherwise fall back to CPU.

Preview Quality
Quality level during viewport compositing or interactive render preview when Denoise node quality follows scene settings.

High:
Highest quality output; longer processing time.

Balanced:
Balance performance and quality; typically half the time of High while retaining most quality.

Fast:
Quick output; noticeable quality reduction.

Final Quality
Quality level during final render when Denoise node quality follows scene settings.

High:
Highest quality output; longer processing time.

Balanced:
Balance performance and quality; typically half the time of High while retaining most quality.

Fast:
Quick output; noticeable quality reduction.

[Related references](INDEX.md).
