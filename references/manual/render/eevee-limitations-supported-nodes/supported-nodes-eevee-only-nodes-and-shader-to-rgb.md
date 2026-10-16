# Supported Nodes: EEVEE only Nodes, Shader to RGB, Specular BSDF, Other Nodes Support, Shader Nodes

## Supported Nodes

Supported Nodes — Node Compatibility

Most nodes originate from Cycles. Some functionality is absent and may or may not appear in EEVEE later.

See also
Shader Nodes.

### EEVEE only Nodes

These nodes only function when EEVEE is the active renderer and are incompatible with Cycles.

### Shader to RGB

EEVEE converts BSDF outputs to color values, enabling custom shading workflows. The Shader to RGB node handles this conversion by evaluating BSDFs similarly to blended materials and inheriting their constraints.

Transparent BSDF operates through the Shader to RGB pathway, granting access to the radiance behind objects according to material classification:

- Dithered material with Raytraced Transmission off samples the nearest light probe.
- Dithered material with Raytraced Transmission on displays other dithered materials without transmission, or falls back to the nearest probe.
- Blended material shows all dithered materials or falls back to the nearest probe.

### Specular BSDF

This node implements the specular workflow pattern found in other rendering systems.

### Other Nodes Support

Unlisted content is supported.

### Shader Nodes

Shader nodes generally behave as they do in Cycles. Consult the Cycles manual section on shading for details.

See also
Materials.

Most BSDFs are supported, though many are approximations lacking full feature parity.

Diffuse BSDF
Roughness is unavailable; only Lambertian diffusion is available.

Glass / Refraction BSDF
GGX and Multiscatter GGX distributions only.
Check Raytracing limitations.

Glossy BSDF
GGX and Multiscatter GGX distributions only.

Subsurface Scattering
Random Walk sampling, IOR, and Anisotropic modes are not available.

Transparent BSDF
Colored and additive transparency work only with blended render modes. When used with Shader to RGB, transparency can expose background radiance depending on material mode and ray-traced transmission settings.

Translucent BSDF
Does not diffuse light through the object; it lights the object with reversed normals.

Principled BSDF
Inherits limitations from Diffuse BSDF, Glossy BSDF, Refraction BSDF, and Subsurface Scattering. Anisotropy is unsupported. The Sheen layer is a crude approximation.

Volume Absorption
See Volume Limitation.

Volume Scatter
The anisotropy parameter is mixed and averaged across overlapping volumetric objects, which is non-physical and differs from Cycles.
Check Volume Limitation.

Principled Volume
Behaves as Volume Scatter; see Volume Limitation.

Holdout
Partially supported; dithered mode may produce wrong results.

Anisotropic BSDF
Unsupported.

Toon BSDF
Unsupported.

Hair BSDF
Unsupported.

Sheen BSDF
Unsupported.

Principled Hair BSDF
Unsupported.

[Related references](INDEX.md).
