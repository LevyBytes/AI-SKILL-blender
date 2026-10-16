# Refraction BSDF

## Refraction BSDF

### Refraction BSDF

Sharp or microfacet-distributed glossy refraction comes from the Refraction BSDF, meant for matter that lets light pass through. Treat it as a component rather than a standalone shader; on its own it darkens the edges of glossy refraction, so blend it with a glossy node through a Fresnel factor for good results.

### Inputs

Color
Surface tint, or in physics terms, the per-wavelength chance that light is refracted.

Roughness
Sets how crisp the refraction looks: dead sharp at 0.0, and progressively blurrier as the number climbs.

Normal
Shading normal; leaving it unconnected falls back to the geometry's default shading normal.

### Properties

Distribution
Microfacet distribution to use.

GGX :

GGX microfacet distribution.

Beckmann :

Cycles Only
Beckmann microfacet distribution.

### Outputs

BSDF
Standard shader output.

### Examples

Refraction Shader.

[Related references](INDEX.md).
