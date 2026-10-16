# Volumes

## Volumes

### Volumes

Reference

Panel :

Render ‣ Volumes

Biased
Standard volume rendering employs null scattering—unbiased, fewer anomalies, potentially noisier. Biased uses ray marching with step and iteration controls.

Note

The following applies to biased ray marching only.

Step distance between volume samples. Cycles computes this based on volume object voxel size and smoke simulations.

Step size increases reduce duration, sacrificing volume precision. For procedural detail-adding volume shaders, per-object, material, or world step adjustment helps.

Step Rate Render Biased
Global step size scaling across all render volumes. Increase to cut time, losing detail.

Viewport Biased
Global step size scaling for viewport volumes. Raise for quicker interaction.

Max Steps Biased
Maximum volume path steps, guarding against extreme durations with large objects or tiny steps.

[Related references](INDEX.md).
