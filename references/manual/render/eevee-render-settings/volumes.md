# Volumes

## Volumes

Volumes: Volumetric Effects

Reference
Panel: Properties ‣ Render ‣ Volumes

EEVEE simulates volumetric scattering by evaluating volume objects within the view frustum.

This employs several 3D textures with substantial video memory demands. Adjust Resolution and Steps to tune dimensions.

Resolution
Volumetric effect quality. Lower resolution increases memory usage and visual quality.

Steps
Volumetric effect computation steps. Higher counts increase memory usage and quality. Samples distribute along view depth.

Distribution
Interpolate between linear and exponential sample spacing. Higher values concentrate samples nearer the camera.

Max Depth
Maximum surface intersection count for accurate volume intersection. Artifacts appear if exceeded.

### Custom Range

EEVEE auto-computes optimal depth range for volume sampling. Sometimes this produces sub-optimal sampling with elevated noise, particularly with World volume shaders or many overlapping volume objects. Enable custom depth range to constrain computation to a depth interval, boosting precision.

Start
Volumetric effect starting distance.

End
Volumetric effect ending distance.

See also
Limitations.

[Related references](INDEX.md).
