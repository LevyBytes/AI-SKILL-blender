# Toon BSDF

## Toon BSDF

### Toon BSDF

Cycles Only

The Toon BSDF builds Diffuse and Glossy materials that carry a stylized, cartoon-style lighting response.

### Inputs

Color
Surface tint, or in physics terms, the per-wavelength chance that light bounces back.

Size
A figure from 0.0 to 1.0 that maps to a reflection angle from 0° to 90°.

Smooth
The angular span over which reflection eases from full down to nothing.

Normal
Shading normal; leaving it unconnected falls back to the geometry's default shading normal.

### Properties

Component
Which material component the toon effect builds on.

Diffuse :

Use shading based on the Diffuse BSDF.

Glossy :

Use shading based on the Glossy BSDF for specular reflection.

### Outputs

BSDF
Standard shader output.

### Examples

Example of Toon Shader.

[Related references](INDEX.md).
