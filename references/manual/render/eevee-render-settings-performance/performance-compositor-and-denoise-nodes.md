# Performance: Compositor, Denoise Nodes

### Compositor

Device
Compositing processor.

CPU :

CPU compositing.

GPU :

GPU compositing.

Precision GPU
Compositor intermediate precision level.

Auto :

Full precision for final renders, half otherwise.

Full :

Full precision throughout.

### Denoise Nodes

Denoising Device
Processing backend for Denoise compositor nodes.

Auto :

Inherit from compositor device.

CPU :

CPU denoising.

GPU :

GPU denoising if accessible, fallback to CPU.

Preview Quality
Denoise node quality during viewport and interactive compositing if set to Follow Scene .

High :

Maximum quality, extended duration.

Balanced :

Speed-quality compromise, typically half the time of High while preserving quality.

Fast :

Quick processing with noticeable quality loss.

Final Quality
Denoise node quality during final rendering if set to Follow Scene .

High :

Maximum quality, extended duration.

Balanced :

Speed-quality compromise, typically half the time of High while preserving quality.

Fast :

Quick processing with noticeable quality loss.

Performance: Optimization Settings

Reference
Panel: Properties ‣ Render ‣ Performance

High Quality Normals
Employ higher-precision normals and tangents for enhanced visual quality on dense meshes with high-frequency textures, at memory cost.

[Related references](INDEX.md).
