# Shader To RGB Node

## Shader To RGB Node

### Shader To RGB Node 

EEVEE Only

The Shader to RGB node enables non-photorealistic rendering through additional effects applied to BSDF outputs. For instance, connecting a color ramp to a diffuse BSDF output creates a flexible cartoon renderer.

Using this function departures from PBR, producing unpredictable results when combined with features such as ambient occlusion, contact shadows, soft shadows, and screen space refraction.

Several effects require multiple passes to stabilize; arbitrary modifications to noisy data may prevent smooth convergence.

Warning

When a Shader to RGB node is present, upstream BSDFs become invisible to:

- Screen Space Reflection

- Subsurface Scattering

- Alpha Clip and Alpha Hashed blend modes

Shader to RGB node rendering fails to produce expected results in render passes.

### Inputs 

Shader
Connect any shader—BSDF or Emission—here.

### Properties 

This node has no properties.

### Outputs 

Color
Computed surface color from BSDFs and ambient illumination.

Alpha
Transparency from embedded Transparent BSDFs.

### Examples 

Simple toon shading with Shader to RGB and freestyle.

[Related references](INDEX.md).
