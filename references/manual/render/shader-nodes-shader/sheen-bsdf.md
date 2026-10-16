# Sheen BSDF

## Sheen BSDF

### Sheen BSDF

Cycles Only

The Sheen BSDF adds a reflective response to surfaces carrying fine microscopic structure, such as cloth or a coating of dust. It is built to sit as a layer over another shader, for instance a dielectric or metallic base.

### Inputs

Color
Surface tint, or in physics terms, the per-wavelength chance that light bounces back.

Roughness
Tunes how much colour returns toward the camera: raise it for more colour and a dusty look, lower it for a softer, darker, fuzzier appearance.

Normal
Shading normal; leaving it unconnected falls back to the geometry's default shading normal.

### Properties

Distribution
Sheen shading model.

Ashikhmin :

Classic Ashikhmin velvet, used in Blender versions prior to 4.0

Microfiber :

Microflake-based model of multiple scattering between normal-oriented fibers.

### Outputs

BSDF
Standard shader output.

### Examples

| Description | Description |
| --- | --- |
| The Sheen shader example. | The Sheen shader behavior. |

[Related references](INDEX.md).
