# Curves

## Curves

### Curves

Reference

Panel :

Render ‣ Curves

Global settings apply to all particle hair systems. Strand resolution is determined by step settings in particle configuration. Each system uses the material specified in its particle settings.

Shape
Determines how curves (such as hair) render. Different techniques optimize for speed or precision based on viewing distance and angle.

Rounded Ribbons :

Render curves as flat ribbons with rounded normals, optimizing speed. Curves subdivide with a set count.

Curve Subdivisions
Subdivision count for cardinal curve calculation (power of 2).

3D Curves :

Render curves as circular 3D forms for precision when viewed up close. Subdivisions adjust automatically to achieve smoothness.

Linear 3D Curves :

Render as 3D circular geometry using linear interpolation between nodes. Faster than 3D curves but less smooth, showing visible transitions at low resolution.

This optimization uses hardware-accelerated curve operations on GPUs. Results differ between CPU and GPU renderings, unsuitable for multi-device rendering or mixed-hardware render farms.

### Viewport Display

These configure curve rendering in Material Preview mode.

Shape

Strand :

Display curves as thin strands, roughly one pixel wide. Diameter parameters are disregarded.

Strip :

Display curves as flat ribbons with rounded normals.

Additional Subdivisions
Subdivisions applied beyond curve resolution from hair system configuration. Higher values refine curve smoothness.

[Related references](INDEX.md).
