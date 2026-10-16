# Sampling

## Sampling

Sampling — Antialiasing Control

EEVEE uses Temporal Anti-Aliasing (TAA) to suppress aliasing. Sample count determines aliasing suppression; more samples reduce artifacts at performance cost.

Reference
Panel: Render ‣ Sampling

### Viewport

Samples
Viewport sample count. Zero enables continuous resampling.

Temporal Reprojection
Attenuate noise during viewport movement or animation playback. May produce ghosting.

Jittered Shadows
Enable jittered shadows in the viewport. Final renders always use jittered shadows. Affects transparent shadows as well.

### Render

Samples
Final render sample count.

### Shadows

Rays
Rays per light for shadow computation. Higher values reduce random shadow noise.

Steps
Shadow map samples per shadow ray. Higher step counts yield softer shadows at higher cost.

Volumetric Shadows
Approximate surrounding volume light absorption, making volumes more opaque to light. Highly computationally expensive with limitations.

Steps
Volumetric shadow computation steps.

See also
Volume Limitations.

Resolution
Shadow map resolution percentage.

### Advanced

Light Threshold
Minimum light intensity for contribution. Governs distance cutoff for light influence. Lower values help performance.

See also
Custom Distance overrides this setting.

Sampling

This modifier controls stroke definition and precision for subsequent operations.

Sampling
Smaller values increase precision. Be cautious: excessively small values require substantial rendering time and memory.

[Related references](INDEX.md).
